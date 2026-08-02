"""Podman-deployable FastAPI service for Hyper-Prompt Routing."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
import sys
sys.path.insert(0, "..")
from core.evaluate import evaluate_prompt

app = FastAPI(title="Hyper-Prompt Router", version="0.1.0")

class EvalRequest(BaseModel):
    prompt: str
    constraints: Optional[Dict[str, Any]] = None

@app.post("/evaluate")
def evaluate(req: EvalRequest):
    try:
        result = evaluate_prompt(req.prompt, req.constraints)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok", "service": "hyper-prompt-router"}
