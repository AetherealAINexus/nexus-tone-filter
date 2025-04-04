from flask import Blueprint, request, jsonify
import config
from services.nova_logic import process_nova_input

toolbox_bp = Blueprint("toolbox", __name__, url_prefix="/api/toolbox/nova")

@toolbox_bp.route("/say", methods=["POST"])
def say():
    data = request.get_json() or {}
    flux_token = (
        data.get("fluxToken")
        or request.headers.get("X-Flux-Token")
        or request.headers.get("flux-token")
    )

    if flux_token != config.FLUX_TOKEN:
        return jsonify({"error": "Unauthorized"}), 403

    text = data.get("text", "")
    session_id = data.get("session_id", "default")

    response = process_nova_input(text, session_id)
    return jsonify(response)
