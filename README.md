

# SHL GenAI Assessment Recommendation Engine

## Overview
This project implements a **GenAI-powered assessment recommendation system** that suggests the most relevant SHL assessments based on a given **job requirement, role description, or skill set**.

The system simulates a real-world recruiter workflow where a user provides free-text input (job role, skills, or requirements) and receives a ranked list of suitable SHL assessments.

The solution includes:
- A **web-based frontend** for easy interaction
- A **REST API** for programmatic access
- A **quantitative evaluation pipeline**

---

## Problem Statement
Given a textual job requirement or skill description, recommend the most appropriate SHL assessments using **Natural Language Processing (NLP)** and **GenAI-based semantic retrieval techniques**.

---

## Data Sources

### 1. SHL Product Catalogue (Public)
The dataset was manually curated using publicly available information from **SHL’s official product catalogue** for academic and evaluation purposes.

Each assessment includes:
- Assessment Name  
- Category  
- Job Level  
- Skills Tested  
- Relevant Job Roles  
- Description  
- Duration  

Source:  
https://www.shl.com/solutions/products/product-catalog/

---

### 2. SHL Provided Evaluation Dataset
File: `Gen_AI Dataset.xlsx`

Sheets:
- **Train-Set**  
  Contains job queries with ground-truth assessment URLs (used for evaluation)

- **Test-Set**  
  Contains query-only inputs (used for inference, no labels available)

---

## Approach

### Step 1: Text Representation
Each assessment is converted into a unified text representation by combining:
- Skills tested  
- Assessment name  
- Category  
- Job level  
- Description  

This creates a semantically rich document suitable for embedding-based retrieval.

---

### Step 2: GenAI Embedding-Based Retrieval
- Sentence Transformers are used to generate dense semantic embeddings
- The user query is embedded using the same model
- Cosine similarity is used to rank assessments
- Top-N most relevant assessments are returned

---

### Step 3: Recommendation Logic
- Recommendations are generated **only when a meaningful query is provided**
- Empty or null inputs do **not** produce recommendations
- Prevents random or misleading outputs

---

## System Components

### 1. Web Application (Streamlit)
- User-friendly interface for entering job requirements
- Displays ranked assessment recommendations
- Suitable for recruiters and evaluators

### 2. REST API (FastAPI)
- Accepts job queries via HTTP requests
- Returns recommendations in JSON format
- Enables system-to-system integration

---

## API Endpoints

### Health Check
```

GET /health

````

Response:
```json
{
  "status": "ok"
}
````

---

### Recommendation Endpoint

```
POST /recommend
```

Request Body:

```json
{
  "query": "Automation test engineer selenium",
  "top_n": 5
}
```

Response:

```json
{
  "recommendations": [
    {
      "assessment_name": "Automata Selenium",
      "category": "technical",
      "job_level": "entry",
      "skills_tested": "selenium automation testing",
      "similarity_score": 0.82
    }
  ]
}
```

Interactive API documentation (Swagger UI):

```
http://127.0.0.1:8000/docs
```

---

## Installation & Requirements

### System Requirements

* Python **3.9+**
* pip
* Git
* Internet connection (for model download)

---

### Python Dependencies

All required libraries are listed in `requirements.txt`, including:

* pandas
* numpy
* scikit-learn
* sentence-transformers
* streamlit
* fastapi
* uvicorn

---

### Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/GautamKumarTiwary/shl.git
cd shl
```

---

#### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate     # Windows
# source venv/bin/activate  # Linux / Mac
```

---

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

### Run Frontend (Web App)

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

### Run Backend API

```bash
uvicorn api.main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

### How to Use the API

You can test the API directly in Swagger UI:

1. Open `/docs`
2. Select `POST /recommend`
3. Enter query text and `top_n`
4. Execute and view JSON results

---

## Evaluation

### Metric Used

* **Recall@10**

### Evaluation Strategy

* **Train-Set**
  Used to compute Recall@10 as it contains ground-truth assessment URLs

* **Test-Set**
  Contains only queries; used for inference to simulate real-world deployment

Run evaluation:

```bash
python -m src.evaluation
```

---

## Project Structure

```
shl/
│
├── app.py                 
├── api/
│   └── main.py             
├── src/
│   ├── embedding_recommender.py
│   ├── preprocess.py
│   └── evaluation.py
├── data/
│   ├── shl_assessments.csv
│   └── Gen_AI Dataset.xlsx
├── requirements.txt
├── README.md
```