import os

# Get the file extension from the user
file_extension = input("Enter the file extension (including the dot, e.g., '.txt'): ")

# Initialize a counter for matching files
matching_files = 0

# Get the current working directory
current_dir = os.getcwd()

# Loop through all files in the directory
for filename in os.listdir(current_dir):
  # Check if the file has the specified extension and contains at least one digit
  if filename.endswith(file_extension): #and any(char.isdigit() for char in filename):
    matching_files += 1

# Print the results
print(f"There are {matching_files} files with extension '{file_extension}' in the current directory.")
