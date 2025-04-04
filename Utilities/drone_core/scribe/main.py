from flask import Flask, request, jsonify
from core import Scribe

app = Flask(__name__)
scribe = Scribe()

@app.route("/log", methods=["POST"])
def log():
    msg = request.get_json().get("message")
    return jsonify({"status": scribe.write(msg)})

if __name__ == "__main__":
    app.run(port=5053)