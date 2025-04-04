from flask import Flask, jsonify
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "✅ Online",
        "node": "watchdog",
        "time": datetime.utcnow().isoformat() + "Z",
        "host": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(port=5055)