from fastapi import FastAPI
from starlette.requests import Request
import os
import yaml

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
    print(f"[🌐 Booting as {config.get('name', 'Unknown Role')}...]")

@app.get("/ping")
async def ping():
    return {"message": "🛰️ Hello from Nexus Comms!"}

@app.post("/echo")
async def echo(request: Request):
    data = await request.json()
    return {"echo": data}
