from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []
next_id = 1


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos), 200


@app.route("/todos", methods=["POST"])
def create_todo():
    global next_id
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    todo = {"id": next_id, "title": data["title"], "done": False}
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201


if __name__ == "__main__":
    app.run(debug=True)
