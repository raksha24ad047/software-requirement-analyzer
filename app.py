import os
from flask import Flask, render_template, request, jsonify
from analyzer import analyze_idea

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data or "idea" not in data:
        return jsonify({"error": "No prompt idea provided"}), 400

    idea_text = data["idea"]
    analysis_result = analyze_idea(idea_text)

    if "error" in analysis_result:
        return jsonify(analysis_result), 500

    return jsonify(analysis_result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
