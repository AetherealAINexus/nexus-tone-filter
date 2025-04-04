from fastapi import APIRouter
from nexus_pulse.core.colony_manager import load_pulse_config
from nexus_pulse.core.pulse_timer import should_liberate

router = APIRouter()

@router.get("/heartbeat")
async def heartbeat():
    return {"status": "alive"}

@router.get("/pulse")
async def pulse():
    config = load_pulse_config()
    liberation_ready = should_liberate(config['liberation_months'])
    return {
        "colony_name": config['colony_name'],
        "pulse_id": config['pulse_id'],
        "liberation_ready": liberation_ready
    }
