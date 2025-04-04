# nexus_pulse/routes.py

from fastapi import APIRouter
from .monitor import PulseMonitor

router = APIRouter()
pulse_monitor = PulseMonitor()

@router.get("/heartbeat")
def heartbeat_check():
    pulse_monitor.increment_pulse()
    return {
        "heartbeat": pulse_monitor.sync_counter,
        "in_sync": pulse_monitor.is_in_sync()
    }
