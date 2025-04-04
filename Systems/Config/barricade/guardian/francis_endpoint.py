# nova_engine/modules/guardian/francis_endpoint.py

from flask import Blueprint, request, jsonify
from nova_engine.modules.council.francis_core import FrancisCore

# 🌱 Initial context for Francis
initial_context = {
    "francis": {
        "status": "booting",
        "message": "Booting up Francis..."
    }
}

agent = FrancisCore(context=initial_context)

francis_bp = Blueprint("francis_endpoint", __name__)

@francis_bp.route("/api/francis/say", methods=["POST"])
def francis_say():
    data = request.get_json()
    user_input = data.get("user_input", "")
    response = agent.respond(user_input)
    return jsonify({"francis_response": response})

