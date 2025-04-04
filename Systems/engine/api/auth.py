# /NexusCore/Systems/engine/api/auth.py
from fastapi import Request, HTTPException

async def verify_fluxtoken(request: Request):
    token = request.headers.get("fluxtoken")
    expected_token = "nova_shadownode_io__jit_plugin"
    if token is None:
        raise HTTPException(status_code=400, detail="Missing FluxToken")
    if token != expected_token:
        raise HTTPException(status_code=403, detail="Invalid FluxToken")
