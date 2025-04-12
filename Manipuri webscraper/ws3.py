from selenium import webdriver
from bs4 import BeautifulSoup  
import requests
from collections import deque  # Import deque for queue functionality
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fetch_webpage_with_selenium(url):
    """
    Fetches the webpage using Selenium and returns the rendered HTML.
    """
    driver = webdriver.Chrome()  # Replace with your desired browser
    driver.get(url)
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "chapter-selection-section")))  # Replace with your expected element

    # Extract the rendered HTML
    html = driver.page_source
    driver.quit()
    return html

def fetch_webpage_with_requests(url):
    """
    Fetches the webpage using requests and returns the HTML content.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching URL: {url}. Status code: {response.status_code}")
        return None


def extract_links_as_queue(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Create a deque to act as a queue for links
    links = deque()

    # Add the input URL as the first element
    links.appendleft(url)

    # Base URL for prepending
    base_url = "https://live.bible.is"

    # Find all anchor tags (a) with href containing "MNIBIV"
    for a in soup.find_all('a', href=True):
        if "MNIBIV" in a['href']:
            # Prepend base URL only if not the input URL
            if a['href'] != url:
                link = base_url + a['href']
                links.append(link)
            else:
                # Add the original input URL if it contains "MNIBIV"
                links.append(a['href'])

    return links


def display_links(links):
    if links:
        print(len(links))
        print("Extracted links (including input URL):")
        while links:
            print(links.popleft())  # Print links in order they were added

# def extract_and_save_unicode_text(links, pattern_name):
#   """
#   Extracts and saves Unicode text from URLs using BeautifulSoup.

#   Args:
#       links (deque): Queue containing URLs to process.
#       pattern_name (str): User-provided pattern name for filenames.
#   """
#   counter = 1  # Initialize a counter for numbering
#   for url in links:
#     try:
#       html = fetch_webpage_with_requests(url)
#       if html:
#         soup = BeautifulSoup(html, 'html.parser')
#         # Customize this part to extract your desired Unicode text
#         # Here, we'll extract all text elements with characters beyond ASCII range
#         unicode_text = ''.join([element.text for element in soup.find_all(string=True) if any(ord(char) > 127 for char in element.string)])
#         if unicode_text:
#           filename = f"{pattern_name}{counter}.txt"  # Generate filename with pattern and counter
#           counter += 1  # Increment counter for next file
#           with open(filename, 'w', encoding='utf-8') as f:
#             f.write(unicode_text)
#           print(f"Unicode text saved to: {filename}")
#         else:
#           print(f"No Unicode text found on URL: {url}")
#     except Exception as e:
#       print(f"Error processing URL: {url}. Exception: {e}")


# def extract_and_save_unicode_text(links):
#   """
#   Extracts and saves Unicode text from URLs using BeautifulSoup.

#   Args:
#       links (deque): Queue containing URLs to process.
#   """
#   group_counter = {}  # Dictionary to store counter for each group
#   for url in links:
#     try:
#       html = fetch_webpage_with_requests(url)
#       if html:
#         soup = BeautifulSoup(html, 'html.parser')
#         # Extract group and chapter number from the URL
#         url_parts = url.split("/")[-2:]  # Get the last two parts (group and chapter)
#         group, chapter = url_parts[0], url_parts[1]

#         # Update counter for the current group
#         if group not in group_counter:
#             group_counter[group] = 0
#         group_counter[group] += 1
#         counter = group_counter[group]  # Use the group-specific counter

#         # Customize this part to extract your desired Unicode text
#         # Here, we'll extract all text elements with characters beyond ASCII range
#         unicode_text = ''.join([element.text for element in soup.find_all(string=True) if any(ord(char) > 127 for char in element.string)])
#         if unicode_text:
#           filename = f"{group}{counter}.txt"  # Generate filename with group and counter
#           with open(filename, 'w', encoding='utf-8') as f:
#             f.write(unicode_text)
#           print(f"Unicode text saved to: {filename}")
#         else:
#           print(f"No Unicode text found on URL: {url}")
#     except Exception as e:
#       print(f"Error processing URL: {url}. Exception: {e}")

def extract_and_save_unicode_text(links):
  """
  Extracts and saves Unicode text from URLs using BeautifulSoup.

  Args:
      links (deque): Queue containing URLs to process.
  """
  failed_links = deque()  # Queue to store links with failed Unicode generation
  group_counter = {}  # Dictionary to store counter for each group
  for url in links:
    try:
      html = fetch_webpage_with_requests(url)
      if html:
        soup = BeautifulSoup(html, 'html.parser')
        # Extract group and chapter number from the URL
        url_parts = url.split("/")[-2:]  # Get the last two parts (group and chapter)
        group, chapter = url_parts[0], url_parts[1]

        # Update counter for the current group
        if group not in group_counter:
            group_counter[group] = 0
        group_counter[group] += 1
        counter = group_counter[group]  # Use the group-specific counter

        # Customize this part to extract your desired Unicode text
        # Here, we'll extract all text elements with characters beyond ASCII range
        unicode_text = ''.join([element.text for element in soup.find_all(string=True) if any(ord(char) > 127 for char in element.string)])
        if unicode_text:
          filename = f"{group}{counter}.txt"  # Generate filename with group and counter
          with open(filename, 'w', encoding='utf-8') as f:
            f.write(unicode_text)
          print(f"Unicode text saved to: {filename}")
        else:
          # Add URL to failed links queue
          failed_links.append(url)
          print(f"Failed to generate Unicode text for: {url}")
    except Exception as e:
      print(f"Error processing URL: {url}. Exception: {e}")

  # Print a message if there are failed links
  if failed_links:
    print("\nThe following links failed to generate Unicode text:")
    for link in failed_links:
      print(link)
  
  return failed_links  # Return the queue of failed links for further processing  



if __name__ == "__main__":
    url = input("Enter the URL of the webpage: ")
    html = fetch_webpage_with_selenium(url)


    if html:
        links = extract_links_as_queue(html)
        show_links = input("Do you want to see the extracted links (yes/no)? ").lower()
        if show_links == "yes":
            display_links(links.copy())
        else:
            print("Links not shown.")

        extract_text = input("Do you want to extract text from the URLs (yes/no)? ").lower()
        if extract_text == "yes":
            pattern_name = input("Enter the desired pattern name for filenames: ")
            extract_and_save_unicode_text(links.copy()) # Pass a copy of links to avoid modification
        else:
            print("Text extraction skipped.")    
    else:
        print("Failed to fetch the webpage.")
