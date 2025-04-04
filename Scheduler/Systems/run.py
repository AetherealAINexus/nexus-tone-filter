Scheduler/run.py

import importlib
import yaml

def get_role_config():
    with open("Scheduler/Config/scheduler.yaml", "r") as f:
        config = yaml.safe_load(f)
        return config.get("active_role", "commander")

def load_role_logic(role):
    try:
        role_module = importlib.import_module(f"Scheduler.Roles.{role}")
        role_module.start()
    except ModuleNotFoundError:
        print(f"🚨 No module found for role: {role}")

if __name__ == "__main__":
    print("🧭 Scheduler booting...")
    role = get_role_config()
    print(f"🧠 Activating role: {role}")
    load_role_logic(role)