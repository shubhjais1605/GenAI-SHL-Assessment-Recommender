import subprocess

backend = "uvicorn api.main:app --reload"
frontend = "streamlit run app.py"

processes = [
    subprocess.Popen(backend, shell=True),
    subprocess.Popen(frontend, shell=True)
]

for p in processes:
    p.wait()
