from flask import Flask, render_template, request, jsonify
from analyzer import analyze_requirement

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    requirement = data.get("requirement", "").strip()

    if not requirement:
        return jsonify({
            "error": "Please enter a software requirement."
        }), 400

    result = analyze_requirement(requirement)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
