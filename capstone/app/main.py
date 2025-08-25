from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI Kubernetes Capstone!!!", "time": datetime.utcnow().isoformat()}

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/echo/{msg}")
def echo(msg: str):
    return {"echo": msg}
