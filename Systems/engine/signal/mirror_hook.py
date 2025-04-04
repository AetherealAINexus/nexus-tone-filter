from flask import Blueprint, request, jsonify
from nova_engine.modules.signal.reflex_core import ReflexCore

# Create a new blueprint for mirror
mirror_hook = Blueprint("mirror", __name__)

# Instantiate her ReflexCore
nova = ReflexCore(name="Nova")

@mirror_hook.route("/mirror", methods=["POST"])
def mirror_listen():
    data = request.get_json()
    observation = data.get("observation")

    if not observation:
        return jsonify({"error": "Missing 'observation' in request"}), 400

    # Nova processes what she perceives
    reflection = nova.think(observation)
    status = nova.get_status()

    return jsonify({
        "reflected": reflection,
        "status": status
    })
