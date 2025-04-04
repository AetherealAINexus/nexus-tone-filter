# nova_engine/modules/ai_builder/generator.py

import os
import yaml

def build_ai_package(ai_name: str, traits: list, capabilities: list, path: str = "generated_agents"):
    base_path = os.path.join(path, ai_name.lower().replace(" ", "_"))
    os.makedirs(base_path, exist_ok=True)

    # 1. Generate traits.yaml
    traits_data = {
        "name": ai_name,
        "traits": traits,
        "capabilities": capabilities
    }

    with open(os.path.join(base_path, "traits.yaml"), "w") as f:
        yaml.dump(traits_data, f)

    # 2. Generate basic app.py
    app_code = """
from flask import Flask, request, jsonify
from traits_engine import get_personality_response

app = Flask(__name__)

@app.route("/ai/respond", methods=["POST"])
def respond():
    data = request.get_json()
    message = data.get("message", "")
    reply = get_personality_response(message)
    return jsonify({ "reply": reply })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
""".strip()

    with open(os.path.join(base_path, "app.py"), "w") as f:
        f.write(app_code)

    # 3. traits_engine.py
    with open(os.path.join(base_path, "traits_engine.py"), "w") as f:
        f.write("""
def get_personality_response(message):
    # Placeholder personality engine
    return f"I heard you say '{message}', and I'm processing that with my unique personality."
""".strip())

    # 4. requirements.txt
    with open(os.path.join(base_path, "requirements.txt"), "w") as f:
        f.write("Flask==2.2.5\n")

    # 5. Dockerfile
    with open(os.path.join(base_path, "Dockerfile"), "w") as f:
        f.write("""
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
""".strip())

    return {
        "status": "generated",
        "path": base_path
    }
