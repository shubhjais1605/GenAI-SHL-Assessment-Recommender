import streamlit as st
from src.embedding_recommender import recommend_embeddings

st.set_page_config(page_title="SHL GenAI Talent Matcher", layout="centered")

st.title("🔍 SHL AI-Powered Talent Assessment Recommender")

job_role = st.text_input("Job Title", placeholder="e.g., Automation Test Engineer")
skills = st.text_area("Key Skills", placeholder="e.g., Selenium, Automation Testing, Python")
job_level = st.selectbox("Experience Level", ["Entry", "Mid", "Senior"])


if st.button("Get Recommendations"):
    if not job_role.strip() and not skills.strip():
        st.warning("⚠️ Please provide at least a Job Title or some Skills to continue.")
    else:
        query = f"{job_role} {skills} {job_level}"
        st.write("⏳ Fetching best-fit assessments...")

        results = recommend_embeddings(query, top_n=5)

        if results.empty:
            st.error("❌ No matching assessments found. Try refining your inputs.")
        else:
            st.subheader("✅ Recommended Assessments")
            for _, row in results.iterrows():
                st.markdown(
                    f"""
                    **{row['assessment_name']}**  
                    🧭 *Category:* {row['category']}  
                    💼 *Level:* {row['job_level']}  
                    📊 *Relevance Score:* `{row['score']:.2f}`  
                    🔗 [View Assessment]({row['assessment_url']})
                    ---
                    """
                )
