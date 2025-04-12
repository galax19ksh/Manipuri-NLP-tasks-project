import os

def delete_files(filename, start, end):
  """Deletes files from a directory with filenames matching a pattern.

  Args:
    filename: The base filename of the files to delete (e.g., "eng").
    start: The starting number of the sequence (inclusive).
    end: The ending number of the sequence (inclusive).
  """
  for i in range(start, end + 1):
    file_path = os.path.join(filename + str(i) + ".txt")
    if os.path.exists(file_path):
      os.remove(file_path)
      print(f"Deleted file: {file_path}")
    else:
      print(f"File not found: {file_path}")

# Get user input
filename = input("Enter the base filename (e.g., eng): ")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Call the function
delete_files(filename, start, end)
