import pandas as pd
from src.embedding_recommender import recommend_embeddings

def recall_at_k(recommended, relevant, k=10):
    recommended_k = recommended[:k]
    if len(relevant) == 0:
        return 0.0
    return len(set(recommended_k) & set(relevant)) / len(relevant)

def evaluate(sheet_name):
    df = pd.read_excel("data/Gen_AI Dataset.xlsx", sheet_name=sheet_name)

    print(f"\nEvaluating on sheet: {sheet_name}")
    print("Columns:", list(df.columns))

    if "Assessment_url" not in df.columns:
        print("No ground-truth labels available. Skipping Recall@10.")
        return

    recalls = []

    for _, row in df.iterrows():
        query = str(row["Query"])
        relevant = [r.strip() for r in str(row["Assessment_url"]).split(",") if r.strip()]

        results = recommend_embeddings(query, top_n=10)
        recommended = results["assessment_url"].tolist()

        recalls.append(recall_at_k(recommended, relevant))

    print(f"Average Recall@10 ({sheet_name}):", sum(recalls) / len(recalls))

if __name__ == "__main__":
    evaluate("Train-Set")  
    evaluate("Test-Set")  
