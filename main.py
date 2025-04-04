# nexus-role/main.py

from fastapi import FastAPI
from Utilities.routes.relay import router as relay_router
import os

# Detect ship identity (fallback if environment var not set)
SHIP_NAME = os.getenv("SHIP_NAME", "Nexus Drone")
SHIP_ROLE = os.getenv("SHIP_ROLE", "General Purpose")

app = FastAPI(
    title=f"{SHIP_NAME} - {SHIP_ROLE}",
    description="Handles Nexus Swarm Communications & Local APIs",
    version="1.0.0"
)

# Attach relay for cross-ship communication
app.include_router(relay_router, prefix="/api/relay")

# Future: Attach more routers dynamically based on role if needed
# Example:
# if SHIP_ROLE == "Memory":
#     from Utilities.routes.memory import router as memory_router
#     app.include_router(memory_router, prefix="/api/memory")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
