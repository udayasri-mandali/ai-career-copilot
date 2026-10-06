from app.job_analyzer import extract_requirements
from sentence_transformers import SentenceTransformer
from app.pdf_reader import extract_text_from_pdf
from app.resume_search import chunk_resume,search_resume
from app.llm import explain_match
model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
import gradio as gr

def analyze(Resume,JOB_Description):
    resume_text = extract_text_from_pdf(Resume)
    chunks = chunk_resume(resume_text)
    chunk_embeddings=model.encode(chunks)
    requirements = extract_requirements(JOB_Description)
    Analyses = []
    for requirement in requirements:

        results = search_resume(
            requirement,
            chunks,
            model,
            chunk_embeddings,
            top_k=3,
        )

        #print("\nRequirement:")
        #print(requirement)

        if not results:
            #print("\nAnalysis:")
            #print("No relevant evidence was found in the resume.")
            Analyses.append("No relevant evidence was found in the resume.")
            #print("-" * 60)
            continue

        evidence = "\n".join(
            result["text"]
            for result in results
        )

        explanation = explain_match(
            requirement,
            evidence,
        )

        #print("\nAnalysis:")
        #print(explanation)

        #print("-" * 60)
        Analyses.append(
            f"Requirement:\n{requirement}\n\n"
            f"Analysis:\n{explanation}")
        #output.append(explanation)

    return "\n\n".join(Analyses)
demo=gr.Interface(fn=analyze,
                  inputs=[
                      gr.File(),
                      gr.Textbox()
                      
                  ],
                  outputs="text")

demo.launch()