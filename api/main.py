from fastapi import FastAPI
from pydantic import BaseModel
from src.embedding_recommender import recommend_embeddings

app = FastAPI(title="SHL Assessment Recommendation API")

class QueryRequest(BaseModel):
    query: str
    top_n: int = 5

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend")
def recommend(req: QueryRequest):
    results = recommend_embeddings(req.query, top_n=req.top_n)

    return {
        "query": req.query,
        "recommendations": [
            {
                "assessment_name": row["assessment_name"],
                "assessment_url": row["assessment_url"],
                "category": row["category"],
                "job_level": row["job_level"],
                "score": round(row["score"], 4)
            }
            for _, row in results.iterrows()
        ]
    }
