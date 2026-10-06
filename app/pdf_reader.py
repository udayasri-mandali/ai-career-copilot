#import fitz
import pymupdf
fitz = pymupdf
import re
def clean_text(text):
    #text=re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r"[•●▪◦■]", " ", text)
    text = re.sub(r"[^\S\n]+", " ", text)
    lines=[line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)
def extract_text_from_pdf(pdf_path):
    with fitz.open(pdf_path) as pdf:
        text = ""
        for page in pdf:
            page_text = page.get_text("text")
            if isinstance(page_text, str):
                text += page_text
    return clean_text(text)
