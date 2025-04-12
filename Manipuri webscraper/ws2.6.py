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


def extract_and_save_unicode_text(url, start_chapter, end_chapter, starting_file_number):
    visited_links = set()
    file_counter = starting_file_number  # Use input for starting file number

    for chapter in range(start_chapter, end_chapter + 1):
        new_url = get_next_link(url, chapter)  # Use provided URL and modify based on chapter
        if new_url in visited_links:
            print(f"Skipping already visited chapter: {chapter}")
            continue
        visited_links.add(new_url.lower())  # Add lowercase URL to set
        print(f"Visiting: {new_url}")  # Print visited URL

        html = fetch_webpage(new_url)
        if html:
            unicode_text = extract_unicode_text(html)
            if unicode_text:
                filename = f"mni{file_counter}.txt"
                write_to_file(unicode_text, filename)
                file_counter += 1
            else:
                print(f"No Unicode text found on chapter {chapter}.")
                # Exit the loop after encountering "No Unicode text found on chapter"
                break
        else:
            print(f"Failed to fetch chapter {chapter}.")


def get_next_link(base_url, chapter_number):
    # Modify URL based on chapter number pattern (assuming it's within the base URL)
    parts = urllib.parse.urlparse(base_url)
    path_parts = parts.path.split('/')[:-1]  # Get path without chapter number
    path_parts.append(str(chapter_number))
    new_url = urllib.parse.urlunparse((parts.scheme, parts.netloc, '/'.join(path_parts), parts.params, parts.query, parts.fragment))
    return new_url.lower()  # Ensure case-insensitive matching


def main():
    url = input("Enter the webpage URL: ")
    start_chapter = int(input("Enter the starting chapter number (inclusive): "))
    end_chapter = int(input("Enter the ending chapter number (inclusive): "))
    starting_file_number = int(input("Enter the starting file number: "))
    extract_and_save_unicode_text(url, start_chapter, end_chapter, starting_file_number)


if __name__ == "__main__":
    main()
