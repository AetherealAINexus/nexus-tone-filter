# keystone.py

from systems.engine.orchestrator import start_orchestrator
from systems.engine.scheduler import start_scheduler
from systems.engine.memory import start_memory
from systems.engine.text import start_text_engine
from systems.engine.tonal import start_tone_engine
from systems.utilitiees.drones import DroneFactory

from config.role_config import get_current_role

def deploy():
    role = get_current_role()
    print(f"[Keystone] Activating as: {role}")

    if role == "orchestrator":
        start_orchestrator()
    elif role == "scheduler":
        start_scheduler()
    elif role == "memory":
        start_memory()
    elif role == "text":
        start_text_engine()
    elif role == "tone":
        start_tone_engine()
    else:
        print(f"[Keystone] Unknown role '{role}'. Initializing fallback drone...")
        DroneFactory.spawn(role=role)
