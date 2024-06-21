import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        # Open the PDF file
        document = fitz.open(pdf_path)
        # Iterate over each page
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def read_pdfs_in_directory(directory_path):
    pdf_texts = {}
    for filename in os.listdir(directory_path):
        print(f"Lendo {filename}")
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(directory_path, filename)
            pdf_texts[filename] = extract_text_from_pdf(pdf_path)
    return pdf_texts

def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Specify the directory containing the PDF files
directory_path = './data/pdf/'
text_path = './data/extracted/'

# Read all PDFs in the directory
pdf_texts = read_pdfs_in_directory(directory_path)

# Save each extracted text to a corresponding .txt file
for pdf_filename, text in pdf_texts.items():
    text_filename = os.path.splitext(pdf_filename)[0] + ".txt"
    print(f"Gravando {text_filename}")
    save_text_to_file(text, os.path.join(text_path, text_filename))

print("Text extraction complete!")
