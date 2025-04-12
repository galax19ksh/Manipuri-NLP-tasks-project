import os

def count_text_files_no_digits(directory):
  """
  Counts the number of text files with no digits in the filename
  and returns a list of their names.

  Args:
      directory: The directory to search in.

  Returns:
      A tuple containing the number of text files with no digits
      and a list of their names.
  """
  text_files_no_digits = []
  for filename in os.listdir(directory):
    if filename.endswith(".txt") and not any(char.isdigit() for char in filename):
      text_files_no_digits.append(filename)
  return len(text_files_no_digits), text_files_no_digits

# Get the current working directory (optional)
current_dir = os.getcwd()
directory = current_dir
# Get the directory path from the user (optional)
# directory = input("Enter the directory path (or leave blank for current directory): ") or current_dir

# Use the function with the desired directory
num_files, filenames = count_text_files_no_digits(directory)

# Print the results
print(f"There are {num_files} text files with no digits in the directory.")
if filenames:
  print("File names:")
  for filename in filenames:
    print(filename)
else:
  print("No text files found with no digits in the filename.")
