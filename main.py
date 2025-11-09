import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# ---- env vars (set on Railway later) ----
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")
VANNA_MODEL  = os.getenv("VANNA_MODEL", "mixtral-8x7b-32768")

app = FastAPI(title="Vanna AI Service", version="1.0.0")

ALLOWED_ORIGINS = [
    "https://<your-vercel-app>.vercel.app",  # <-- replace
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryIn(BaseModel):
    query: str

@app.get("/")
def health():
    return {"ok": True, "service": "vanna", "model": VANNA_MODEL}

@app.post("/chat-with-data")
def chat_with_data(in_: QueryIn):
    # TODO: call real Vanna/Groq here using env vars above.
    # keep response shape your frontend expects
    return {
        "query": in_.query,
        "sql": "SELECT 1 AS ok",
        "results": [{"ok": 1}],
        "columns": ["ok"],
        "rowCount": 1,
        "executionTime": 5
    }
