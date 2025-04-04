# nexus_core/main.py

from fastapi import FastAPI
from nexus_pulse.routes import router as pulse_router
from nexus_core.council import router as council_router  # 🆕 ADD THIS

app = FastAPI(
    title="Nexus Pulse Service",
    description="Monitoring Thirteenth Pulse Synchronization across swarm",
    version="0.1.0"
)

app.include_router(pulse_router, prefix="/pulse")
app.include_router(council_router, prefix="/council")  # 🆕 ADD THIS
