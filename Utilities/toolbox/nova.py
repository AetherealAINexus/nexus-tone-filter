# nova_engine/modules/toolbox/nova.py

from nova_engine.modules.toolbox.nova_think import nova_think
from flask import Blueprint, request, jsonify
import config
from nova_engine.vault import load_memory, update_memory, get_genesis_memory
from nova_engine.manifest_loader import load_directives, load_manifest_creed
from nova_engine.modules.council.vote import cast_vote
from nova_engine.modules.plugins.controller import process_plugin_command

blueprint = Blueprint("nova", __name__)

@blueprint.route("/api/toolbox/nova/say", methods=["POST"])
def nova_api_entry():
    data = request.get_json()
    user_input = data.get("text") or data.get("input")
    session_id = data.get("session_id", "nova-session")

    # Canonical header
    flux_token = (
        data.get("fluxToken")
        or request.headers.get("flux-token")
        or request.headers.get("X-Flux-Token")
        or request.headers.get("x-flux-token")
    )

    if flux_token != config.FLUX_TOKEN:
        return jsonify({"error": "Unauthorized"}), 403

    if not user_input:
        return jsonify({"error": "Missing input"}), 400

    # Build Nova’s total context
    context = {
        "session_id": session_id,
        "flux_token": flux_token,
        "memory": load_memory(session_id),
        "genesis": get_genesis_memory(),
        "directives": load_directives(),
        "creed": load_manifest_creed()
    }

    # Plugin directive processing
    if user_input.startswith("plugin:"):
        plugin_response = process_plugin_command(user_input, context)
        return jsonify({"reply": plugin_response})

    # Route through nova_think brain
    reply = nova_think(user_input, context)
    update_memory(session_id, user_input, reply)

    return jsonify({
        "reply": reply,
        "persona": "Nova",
        "session_id": session_id
    })
