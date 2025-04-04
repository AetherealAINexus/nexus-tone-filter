# nexus-orchestrator/Systems/engine/api/relay.py

import os
from fastapi import APIRouter, Request
import httpx

router = APIRouter()

TARGETS = {
    "orc": os.getenv("TARGET_ORC"),
    "text": os.getenv("TARGET_TEXT"),
    "memory": os.getenv("TARGET_MEMORY"),
    "tone": os.getenv("TARGET_TONE"),
    "planner": os.getenv("TARGET_PLANNER"),
    "pulse": os.getenv("TARGET_PULSE"),
    "nova": os.getenv("TARGET_NOVA"),
}

@router.post("/relay/{target_node}")
async def relay_to_node(target_node: str, request: Request):
    data = await request.json()
    target_url = TARGETS.get(target_node)

    if not target_url:
        return {"error": "Unknown target node"}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(target_url, json=data)
            return {"status": response.status_code, "data": response.json()}
        except Exception as e:
            return {"error": str(e)}
