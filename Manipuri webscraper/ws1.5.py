import requests
from bs4 import BeautifulSoup
import urllib.parse  # Import for urljoin

def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return None

def extract_unicode_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Extract text from HTML elements containing Unicode characters
    unicode_text = ''.join([element.text for element in soup.find_all(string=True) if any(ord(char) > 127 for char in element.string)])
    return unicode_text

def write_to_file(text, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Unicode text saved to '{filename}'")
    except IOError as e:
        print("Error writing to file:", e)

def get_next_page_link(soup, visited_links, current_url):  # Define current_url argument
    # Find links to the next page
    links = []
    for a in soup.find_all('a', href=True):
        link = a['href']
        if link.startswith('http'):
            links.append(link)
        else:
            # Handle relative paths based on the base URL
            base_url = soup.base.get('href') if soup.base else current_url  # Use current_url
            links.append(urllib.parse.urljoin(base_url, link))

    # Filter out links already visited and non-HTML pages
    next_page_link = None
    for link in links:
        if link not in visited_links and link.endswith(('.htm', '.html')):
            next_page_link = link
            break
    return next_page_link

def extract_and_save_unicode_text(url, visited_links, file_counter):
    visited_links.add(url)
    html = fetch_webpage(url)
    if html:
        unicode_text = extract_unicode_text(html)
        if unicode_text:
            filename = f"mni{file_counter}.txt"  # Format filename with counter
            write_to_file(unicode_text, filename)
            file_counter += 1  # Increment counter for next file
        else:
            print("No Unicode text found on the webpage.")

        # Find and process the next page link if available (recursive call)
        soup = BeautifulSoup(html, 'html.parser')
        next_page_link = get_next_page_link(soup, visited_links.copy(), url)  # Pass current_url as url
        if next_page_link:
            extract_and_save_unicode_text(next_page_link, visited_links, file_counter)
    else:
        print("Failed to fetch the webpage.")

def main():
    url = input("Enter the URL of the starting webpage: ")
    visited_links = set()  # Keep track of visited URLs to avoid repetition
    file_counter = 1  # Start counter for file naming
    extract_and_save_unicode_text(url, visited_links, file_counter)

    # Print visited links after processing
    print("\nVisited Links:")
    for link in visited_links:
        print(link)

if __name__ == "__main__":
    main()
