# /NexusCore/run.py

import os
import yaml
import subprocess

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "Config", "current_role.yaml")

# Load Role Config
def load_role_config():
    try:
        with open(CONFIG_PATH, "r") as f:
            config = yaml.safe_load(f)
            return config.get("role")
    except Exception as e:
        print(f"[ERROR] Failed loading config: {e}")
        return None

# Run Service
def run_service(role):
    service_paths = {
        "orchestrator": os.path.join(BASE_DIR, "Systems", "engine", "api"),
        "scheduler": os.path.join(BASE_DIR, "Systems", "engine", "scheduler"),
        "text": os.path.join(BASE_DIR, "Systems", "engine", "text"),
        "memory": os.path.join(BASE_DIR, "Systems", "engine", "memory"),
        "tone": os.path.join(BASE_DIR, "Systems", "engine", "tone"),
        "keystone": os.path.join(BASE_DIR, "Systems", "engine", "keystone")
    }

    path = service_paths.get(role.lower())
    if not path:
        print(f"[ERROR] Unknown role: {role}")
        return

    os.chdir(path)
    try:
        print(f"[INFO] Starting service for role: {role}...")
        subprocess.run(["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"])
    except Exception as e:
        print(f"[ERROR] Failed to start service: {e}")

# Main Execution
if __name__ == "__main__":
    role = load_role_config()
    if role:
        run_service(role)
    else:
        print("[WARN] No valid role config found. Please check your /Config/current_role.yaml")
