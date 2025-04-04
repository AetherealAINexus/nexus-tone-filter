from flask import Flask, request, jsonify
from core import TriggerAgent

app = Flask(__name__)
trigger = TriggerAgent()

@app.route("/trigger", methods=["POST"])
def act():
    cond = request.get_json().get("condition")
    return jsonify({"action": trigger.react(cond)})

if __name__ == "__main__":
    app.run(port=5054)