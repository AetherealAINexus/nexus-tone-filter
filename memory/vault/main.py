from flask import Flask, request, jsonify
from core import Vault

app = Flask(__name__)
vault = Vault()

@app.route("/vault/get", methods=["GET"])
def get():
    key = request.args.get("key")
    return jsonify({key: vault.retrieve(key)})

@app.route("/vault/set", methods=["POST"])
def set_val():
    data = request.get_json()
    key, val = data.get("key"), data.get("value")
    return jsonify({"status": vault.store(key, val)})

if __name__ == "__main__":
    app.run(port=5051)