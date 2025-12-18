## GenAI-SHL-Assessment-Recommender
GenAI-powered assessment recommendation engine using SHL product catalog

## 🚀 Overview
The **SHL GenAI Assessment Recommender** is an **AI-powered system** that recommends the most relevant SHL assessments based on a given **job title, skills, or role description**.

It simulates a recruiter’s workflow — input job details → get instant, ranked SHL assessment recommendations.

### 🔍 Key Features
- 💡 **AI-Driven Recommendations** using semantic embeddings  
- 🌐 **Streamlit Web App** for recruiters  
- ⚙️ **FastAPI REST Backend** for system integration  
- 📊 **Evaluation Pipeline** with Recall@10 scoring  

---

## 🧩 Problem Statement
Given a textual job description or skill set, the goal is to recommend SHL assessments that best align with it using **GenAI-based semantic retrieval**.

---

## 📚 Data Sources

### 1️⃣ SHL Product Catalogue (Public)
Manually curated from [SHL’s Product Catalogue](https://www.shl.com/solutions/products/product-catalog/).

Includes:
- Assessment Name  
- Category  
- Job Level  
- Skills Tested  
- Description  

### 2️⃣ Evaluation Dataset (`Gen_AI Dataset.xlsx`)
- **Train-Set:** labeled data for Recall@10 evaluation  
- **Test-Set:** query-only data for inference  

---

## 🧠 Approach

### Step 1: Unified Text Representation  
Combine name, skills, category, level, and description → create rich text for embedding.

### Step 2: Embedding-Based Retrieval  
- Use **Sentence Transformers** for semantic vectorization  
- Apply **cosine similarity** for ranking  

### Step 3: Intelligent Recommendation  
- Run only for valid user input  
- Prevent random or empty queries  

---

## 🏗️ System Components

| Component | Description |
|------------|--------------|
| 🖥️ **Frontend (Streamlit)** | Enter job roles & view recommendations |
| ⚡ **Backend (FastAPI)** | Exposes `/recommend` API endpoint |
| 📈 **Evaluation Module** | Computes Recall@10 metric |

---

## ⚙️ API Summary

### 🔹 Health Check
```bash
GET /health
````

Response:

```json
{"status": "ok"}
```

### 🔹 Recommendation

```bash
POST /recommend
```

Request:

```json
{"query": "Automation test engineer selenium", "top_n": 5}
```

Response:

```json
{
  "recommendations": [
    {
      "assessment_name": "Automata Selenium",
      "category": "Technical",
      "job_level": "Entry",
      "similarity_score": 0.82
    }
  ]
}
```

🧭 Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧰 Installation

### Requirements

* Python **3.9+**
* pip & Git
* Internet connection (for model download)

### Setup

```bash
git clone https://github.com/shubhjais1605/GenAI-SHL-Assessment-Recommender.git
cd shl
python -m venv venv
venv\Scripts\activate   # (Windows)
# source venv/bin/activate  # (Linux/Mac)
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### 🖥️ Run Frontend (Streamlit)

```bash
streamlit run app.py
```

→ Visit: [http://localhost:8501](http://localhost:8501)

### ⚡ Run Backend (FastAPI)

```bash
uvicorn api.main:app --reload
```

→ API: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 🔁 Run Both (Frontend + Backend)

Run both simultaneously using:

```bash
python run_both.py
```

This launches the Streamlit app and FastAPI server **together** for quick testing.

---

## 🧪 Evaluation

* Metric: **Recall@10**
* Run evaluation:

  ```bash
  python -m src.evaluation
  ```

---

## 📂 Project Structure

```
shl/
│
├── app.py
├── run_both.py              # Runs frontend + backend together
├── api/
│   └── main.py
├── src/
│   ├── embedding_recommender.py
│   ├── preprocess.py
│   └── evaluation.py
├── data/
│   ├── shl_catalogue.csv
│   └── Gen_AI Dataset.xlsx
├── requirements.txt
└── README.md
```

---
