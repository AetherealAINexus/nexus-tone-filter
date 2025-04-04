# nova_engine/modules/plugins/controller.py

from flask import Blueprint, jsonify

controller_bp = Blueprint('controller', __name__)

@controller_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        "status": "✅ Controller online",
        "message": "Nova’s plugin controller is live and synced."
    })

