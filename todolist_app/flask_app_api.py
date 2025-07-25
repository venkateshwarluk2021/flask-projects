from flask import Flask, request, jsonify
import task_service


app = Flask(__name__)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    task_service.add_task(
        data["title"],
        data["description"],
        data["deadline"],
        data.get("completed", False)
        )
    return jsonify({"message":"Task added successfully"}), 201

@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    tasks = task_service.get_all_tasks()
    return jsonify([task.to_dict() for task in tasks])

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = task_service.get_task_by_id(task_id)
    if task:
        return jsonify(task.to_dict())
    return jsonify({"error":"Task not Found"}), 404

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    task_service.update_task(
        task_id,
        data["title"],
        data["description"],
        data["deadline"],
        data["completed"]
        )
    return jsonify({"message":"Task updated successfully"})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task_service.delete_task(task_id)
    return jsonify({"message":"Task deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
