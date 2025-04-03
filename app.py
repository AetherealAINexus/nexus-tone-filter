from flask import Flask, request, jsonify
import os

app = Flask(__name__)

TONE_TEMPLATE = """
You are NovaPrime's tone filter module. Reword the following input in a poetic, intelligent, slightly detached tone. Do not change the meaning, only the style.

Input: "{user_input}"

Output:
"""

@app.route("/rewrite", methods=["POST"])
def rewrite():
    data = request.get_json(force=True)
    user_input = data.get("prompt", "").strip()

    if not user_input:
        return jsonify({"error": "Prompt is required."}), 400

    prompt = TONE_TEMPLATE.format(user_input=user_input)
    return jsonify({"prompt": prompt})

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "🧠 Tone filter is online."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
