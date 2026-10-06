from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
from app.pdf_reader import extract_text_from_pdf
import re
import re
from sklearn.metrics.pairwise import cosine_similarity
def chunk_resume(resume_text):
    # Split on sentence-ending punctuation or line breaks.
    pieces = re.split(
        r"(?<=[.!?])\s+|\n+",
        resume_text
    )

    chunks = [
        piece.strip()
        for piece in pieces
        if len(piece.split()) >= 2
    ]

    return chunks
def keywords(text):
        stop_words={"and","or","the","a","an","for","to","of","in","with"
            ,"using"}
        words=re.findall(r"[a-zA-Z0-9+#.]+",text.lower())
        return {
            word for word in words
            if word not in stop_words }

def search_resume(query,chunks,model,chunk_embeddings,top_k=3,min_score=0.20):
    query_embedding=model.encode([query])
    semantic_scores=cosine_similarity(query_embedding, chunk_embeddings)[0]
    
    #ranked_indices=scores.argsort()[::-1]
    query_words=keywords(query)
    results=[]
    for index, chunk in enumerate(chunks):
        chunk_words = keywords(chunk)

        if query_words:
            keyword_score = (
                len(query_words & chunk_words)
                / len(query_words)
            )
        else:
            keyword_score = 0.0

        semantic_score = float(semantic_scores[index])

        # Combine semantic relevance with explicit word matches.
        combined_score = (
            0.60 * semantic_score
            + 0.40 * keyword_score
        )

        if combined_score >= min_score:
            results.append({
                "text": chunk,
                "score": combined_score,
                "semantic_score": semantic_score,
                "keyword_score": keyword_score,
            })

    results.sort(
        key=lambda result: result["score"],
        reverse=True,
    )

    return results[:top_k]


    

