## This is the basic code for pdf2text mainly used for testing single page


import PyPDF2

def extract_text_to_file(pdf_filepath, output_filepath):
  """
  Extracts text from a PDF file and saves it to a text file.

  Args:
      pdf_filepath: Path to the PDF file.
      output_filepath: Path to the output text file.
  """
  with open(pdf_filepath, 'rb') as pdf_file, open(output_filepath, 'w', encoding='utf-8') as text_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)

    for page_num in range(num_pages):
      page = pdf_reader.pages[page_num]
      text = page.extract_text()
      text_file.write(text)

# Example usage
pdf_filepath = "path/to/pdf"
output_filepath = "path/to/output/textfile"
extract_text_to_file(pdf_filepath, output_filepath)

print(f"Text extracted from '{pdf_filepath}' and saved to '{output_filepath}'.")
