# THis is same as pdf3text.py except it displays progress when run. It also has been updated for error handling.
import os
import PyPDF2

def extract_text_to_file(pdf_filepath, output_dir, output_filename=None):
  """
  Extracts text from a PDF file and saves it to a text file, with progress indication.

  Args:
      pdf_filepath: Path to the PDF file.
      output_dir: Path to the directory where the extracted text file will be saved.
      output_filename (optional): Custom filename for the output text file.
  """
  try:
    with open(pdf_filepath, 'rb') as pdf_file:
      pdf_reader = PyPDF2.PdfReader(pdf_file)
      num_pages = len(pdf_reader.pages)

      text = ""
      for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
        print(f"Extracting text from page {page_num+1} of {num_pages} in {os.path.basename(pdf_filepath)}...", end="\r")

    if not output_filename:
      # Use original filename without extension for output text file
      filename, _ = os.path.splitext(os.path.basename(pdf_filepath))
      output_filepath = os.path.join(output_dir, filename + ".txt")
    else:
      output_filepath = os.path.join(output_dir, output_filename)

    with open(output_filepath, 'w', encoding='utf-8') as text_file:
      text_file.write(text)
      print(f"Extracted text from '{pdf_filepath}' and saved to '{output_filepath}'.")
  except Exception as e:
    print(f"Error processing file '{pdf_filepath}': {e}")

def process_pdf_directory(pdf_dir, output_dir):
  """
  Processes all PDF files in a directory and extracts text to a separate directory, with progress indication.

  Args:
      pdf_dir: Path to the directory containing PDF files.
      output_dir: Path to the directory where extracted text files will be saved.
  """
  num_files = len([f for f in os.listdir(pdf_dir) if f.endswith(".pdf")])
  processed_files = 0

  for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
      pdf_filepath = os.path.join(pdf_dir, filename)
      extract_text_to_file(pdf_filepath, output_dir)
      processed_files += 1
      print(f"Processed {processed_files} out of {num_files} files.")

# Example Usage
pdf_directory = "/mnt/mydisk/Manipuri MT/WebScrap/Newspaper to text /mn Newspaper 2023-2024june"
output_directory = "/mnt/mydisk/Manipuri MT/WebScrap/Newspaper to text /mn newspaper 2023- text raw"
process_pdf_directory(pdf_directory, output_directory)
