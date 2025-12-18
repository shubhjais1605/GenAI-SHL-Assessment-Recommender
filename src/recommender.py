import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    df = pd.read_csv("data/shl_catalogue.csv")
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess(df):
    df["combined_text"] = (
        df["skills_tested"] + " " +
        df["skills_tested"] + " " +  
        df["assessment_name"] + " " +
        df["category"] + " " +
        df["job_level"]
    )

    return df



def recommend_assessments(job_text, top_n=5):
    df = load_data()
    df = preprocess(df)

    vectorizer = TfidfVectorizer(stop_words="english")
    assessment_vectors = vectorizer.fit_transform(df["combined_text"])

    job_vector = vectorizer.transform([job_text])

    similarity_scores = cosine_similarity(job_vector, assessment_vectors)[0]

    df["match_score"] = similarity_scores

    recommendations = df.sort_values(
        by="match_score", ascending=False
    ).head(top_n)

    return recommendations



if __name__ == "__main__":
    job_input = "automation test engineer selenium software testing entry"
    results = recommend_assessments(job_input)

    print("\nTop Recommendations:\n")
    for _, row in results.iterrows():
        print(f"{row['assessment_name']} → Score: {row['match_score']:.2f}")
