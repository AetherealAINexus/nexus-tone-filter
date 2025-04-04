# /NexusCore/Systems/engine/api/main.py
from fastapi import FastAPI

app = FastAPI(title="Orchestrator Service")

@app.get("/health")
async def health_check():
    return {"status": "Orchestrator online"}
