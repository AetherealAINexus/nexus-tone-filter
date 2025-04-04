# nova_engine/modules/seed/full_upload.py

import os
import zipfile
import yaml
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

UPLOAD_DIR = "memory/streams"
full_upload = Blueprint("full_upload", __name__, url_prefix="/nova/seed")

@full_upload.route("/full-upload", methods=["POST"])
def full_upload_handler():
    flux_token = request.headers.get("flux-token")
    if flux_token != os.environ.get("FLUX_TOKEN"):
        return jsonify({"error": "Unauthorized"}), 403

    name = request.form.get("name", "unnamed").lower().replace(" ", "_")
    stream_path = os.path.join(UPLOAD_DIR, name)
    os.makedirs(stream_path, exist_ok=True)

    # Save seed.yaml
    if 'seed' in request.files:
        seed_file = request.files['seed']
        with open(os.path.join(stream_path, "seed.yaml"), "wb") as f:
            f.write(seed_file.read())

    # Save zip of data
    if 'data' in request.files:
        zip_data = request.files['data']
        zip_path = os.path.join(stream_path, secure_filename(zip_data.filename))
        zip_data.save(zip_path)

        # Extract contents
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(stream_path)

    return jsonify({"status": "✅ Full seed uploaded", "path": stream_path})
