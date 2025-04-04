# nexus-orchestrator/main.py

from fastapi import FastAPI
from Utilities.routes.relay import router as relay_router

app = FastAPI(
    title="Nexus Orchestrator Relay",
    description="Handles relayed API communications between drones",
    version="1.0.0"
)

# Attach relay
app.include_router(relay_router, prefix="/api/relay")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)
