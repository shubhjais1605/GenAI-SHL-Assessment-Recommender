from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from src.recommender import load_data, preprocess

model = SentenceTransformer("all-MiniLM-L6-v2")

def recommend_embeddings(query, top_n=5):
    df = load_data()
    df = preprocess(df)

    doc_embeddings = model.encode(df["combined_text"].tolist(), convert_to_tensor=True)
    query_embedding = model.encode(query, convert_to_tensor=True)

    scores = cosine_similarity(
        query_embedding.cpu().numpy().reshape(1, -1),
        doc_embeddings.cpu().numpy()
    )[0]

    df["score"] = scores
    return df.sort_values("score", ascending=False).head(top_n)

if __name__ == "__main__":
    print(recommend_embeddings("selenium automation testing"))
