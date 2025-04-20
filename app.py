from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load JSON data
def load_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

men_dict = load_json("men.json")
women_dict = load_json("women.json")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.json.get("query", "").strip().lower()
    if not query:
        return jsonify({"men": "Not found", "women": "Not found"})

    # Return all entries if query is "all"
    if query == "all":
        result1 = "\n".join([f"{k}: {v}" for k, v in men_dict.items()])
        result2 = "\n".join([f"{k}: {v}" for k, v in women_dict.items()])
        return jsonify({"men": result1, "women": result2})

    # Filter dictionary data for normal search
    matches1 = {k: v for k, v in men_dict.items() if query in k.lower()}
    matches2 = {k: v for k, v in women_dict.items() if query in k.lower()}

    result1 = "\n".join([f"{k}: {v}" for k, v in matches1.items()]) if matches1 else "Not found"
    result2 = "\n".join([f"{k}: {v}" for k, v in matches2.items()]) if matches2 else "Not found"

    return jsonify({"men": result1, "women": result2})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
