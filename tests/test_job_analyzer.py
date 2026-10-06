from app.job_analyzer import extract_requirements
from sentence_transformers import SentenceTransformer
from app.pdf_reader import extract_text_from_pdf
from app.resume_search import chunk_resume,search_resume
from app.llm import explain_match
job_description = """
Requirements:
Strong Python programming skills
Experience with machine learning algorithms
Knowledge of SQL and data analysis
Understanding of Transformer architecture
Experience with problem solving
"""
pdf_path = r"C:\\Users\\udaya\\Downloads\\Mandali Udaya Sri.pdf"
resume_text = extract_text_from_pdf(pdf_path)
chunks = chunk_resume(resume_text)
model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
chunk_embeddings=model.encode(chunks)


requirements = extract_requirements(job_description)


for requirement in requirements:

    results = search_resume(
        requirement,
        chunks,
        model,
        chunk_embeddings,
        top_k=3,
    )

    print("\nRequirement:")
    print(requirement)

    if not results:
        print("\nAnalysis:")
        print("No relevant evidence was found in the resume.")
        print("-" * 60)
        continue

    evidence = "\n".join(
        result["text"]
        for result in results
    )

    explanation = explain_match(
        requirement,
        evidence,
    )

    print("\nAnalysis:")
    print(explanation)

    print("-" * 60)

