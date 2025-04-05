from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import os
import yaml
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
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

# Load the Ship Standard Mind
print("🛠️ Loading Nexus Bridge Mind: Standard Model (Gemma 2B-it)")
model_id = "google/gemma-2b-it"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)
model.eval()
print("✅ Nexus Bridge Mind online across ALL ships!")

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

@app.post("/bridge/infer")
async def infer_bridge(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "").strip()

@app.post("/generate")
async def generate_prompt(data: dict):
    prompt = data.get("prompt", "")
    if not prompt:
        return {"error": "No prompt provided."}
    
    response = bridge_core.generate_response(prompt)
    return {"response": response}


    if not prompt:
        return JSONResponse(content={"error": "Prompt is required"}, status_code=400)

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=100)

    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response_text}
