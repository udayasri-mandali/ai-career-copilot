from sentence_transformers import SentenceTransformer, util
from app.pdf_reader import extract_text_from_pdf
from app.resume_search import chunk_resume, search_resume

pdf_path="C:\\Users\\udaya\\Downloads\\Mandali Udaya Sri.pdf"
resume_text = extract_text_from_pdf(pdf_path)
chunks = chunk_resume(resume_text)
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
chunk_embeddings = model.encode(chunks)

requirements = [
    "Python programming",
    "Data structures and algorithms",
    "Machine learning algorithms",
    "Model evaluation",
    "Large language models",
    "Transformer architecture",
    "Retrieval augmented generation",
    "Semantic search",
    "Agentic AI and autonomous tool use",
    "Data cleaning",
    "SQL querying",
    "Data analysis",
]


for requirement in requirements:
    print(f"\n{'=' * 60}")
    print("Requirement:", requirement)

    results = search_resume(
        requirement,
        chunks,
        model,
        chunk_embeddings,
    )
    #for result in results:
        #print(f"Score: {result['score']:.4f}")
        #print("Evidence:", result["text"])
        #print(
        #"Semantic:",
        #result["keyword_score"])

    