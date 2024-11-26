#import os
from pathlib import Path
#from PyPDF2 import PdfReader
import pdfplumber

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF using pdfplumber.
    """
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def save_uploaded_file(upload, destination_path: str):
    """
    Save uploaded file to a destination.
    """
    Path(destination_path).parent.mkdir(parents=True, exist_ok=True)
    with open(destination_path, "wb") as f:
        f.write(upload.read())
