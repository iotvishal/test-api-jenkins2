from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {"id": 1, "title": "Learn Jenkins", "completed": False},
    {"id": 2, "title": "Build Docker pipeline", "completed": True}
]


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted"})
    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
