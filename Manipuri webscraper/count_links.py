def count_links_in_file(filename):
  """Counts the number of lines containing 'https' or 'http' in a file.

  Args:
    filename: The name of the file to read.

  Returns:
    The number of lines containing 'https' or 'http'.
  """

  link_count = 0
  try:
    with open(filename, 'r') as file:
      for line in file:
        if "https" in line or "http" in line:
          link_count += 1
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  else:
    return link_count

# Example usage
filename = input("Enter the filename: ")
number_of_links = count_links_in_file(filename)

if number_of_links is not None:
  print(f"Number of lines containing links in '{filename}': {number_of_links}")
