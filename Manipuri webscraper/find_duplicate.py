import os
from collections import defaultdict

def find_repeated_filenames(directory):
  """
  Finds and returns a dictionary containing repeated filenames as keys
  and a list of their paths as values.

  Args:
      directory: The directory to search in.

  Returns:
      A dictionary where keys are repeated filenames and values are lists
      containing their paths in the directory.
  """
  repeated_files = defaultdict(list)
  for root, _, files in os.walk(directory):
    for filename in files:
      filepath = os.path.join(root, filename)
      repeated_files[filename].append(filepath)
  return {key: value for key, value in repeated_files.items() if len(value) > 1}

# Get the directory path from the user (optional)
# directory = input("Enter the directory path: ")

# Use the function with the desired directory (or current directory by default)
repeated_files = find_repeated_filenames(os.getcwd())

# Print the results
if repeated_files:
  print("Following filenames have duplicates:")
  for filename, paths in repeated_files.items():
    print(f"\t- {filename}")
    for path in paths:
      print(f"\t\t- {path}")
else:
  print("No repeated filenames found in the directory.")
