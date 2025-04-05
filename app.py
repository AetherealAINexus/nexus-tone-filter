from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import os
import yaml
from llm_bridge import NexusBridgeCore

bridge_core = NexusBridgeCore()

app = FastAPI(title="Nexus Comms Core")

# Load Nucleus Role Config
def load_config():
    role = os.getenv("NEXUS_ROLE", "orchestrator")
    config_path = f"./Config/nucleus/{role}_config.yaml"
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    return {}

@app.on_event("startup")
async def startup_event():
    config = load_config()
    print(f"[🌐 Ship Role: {config.get('name', 'Unknown')}] Online and Operational")

@app.get("/ping")
async def ping():
    return {"message": "🛰️ Hello from Nexus Standard Core!"}

@app.post("/echo")
async def echo(request: Request):
    data = await request.json()
    return {"echo": data}

@app.post("/generate")
async def generate_prompt(data: dict):
    prompt = data.get("prompt", "")
    if not prompt:
        return {"error": "No prompt provided."}
    
    response = bridge_core.generate_response(prompt)
    return {"response": response}
