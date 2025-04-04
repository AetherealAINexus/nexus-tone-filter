from flask import Flask, request, jsonify
from core import Medic

app = Flask(__name__)
medic = Medic()

@app.route("/medic/repair", methods=["POST"])
def repair():
    data = request.get_json()
    node, issue = data.get("node"), data.get("issue")
    return jsonify({"result": medic.heal(node, issue)})

@app.route("/medic/status", methods=["GET"])
def status():
    return jsonify({"status": medic.heartbeat_check()})

if __name__ == "__main__":
    app.run(port=5065)