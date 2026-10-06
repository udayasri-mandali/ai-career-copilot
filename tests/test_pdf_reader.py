from app.pdf_reader import extract_text_from_pdf
pdf_path="C:\\Users\\udaya\\Downloads\\Mandali Udaya Sri.pdf"
resume_text = extract_text_from_pdf(pdf_path)
resume_chunks=[
    chunk.strip()
    for chunk in resume_text.split('\n')
    if chunk.strip()
]
print("Resume chunks: ")
for chunk in resume_chunks:
    print("-",chunk)