from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import Users, Tasks
from forms import ItemForm
from settings import app, db
import random
import os


# Initialize the JWTManager
jwt = JWTManager(app)

# In-memory user store for simplicity
# users = {
#     "user1": "password1",
#     "user2": "password2"
# }

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = ItemForm()

    id = random.randint(1000, 1999)
    if request.method == "POST":
        user_info = Users(
            id = id,
            password = request.json.get("password"),
            email = request.json.get("email")
        )

        db.session.add(user_info)
        db.session.commit()

        message = "Welcome, your user ID is {}. Kindly keep it somewhere save as this is required for login".format(id)
        access_token = create_access_token(identity=id)
        return jsonify(access_token=access_token,msg=message), 201


@app.route('/login', methods=['POST'])
def login():
    id = request.json.get('user_id', None)
    password = request.json.get('password', None)

    if not id or not password:
        return jsonify({"msg": "Missing username or password"}), 400
    
    user = Users.query.get(id)

    if user.password != password:
        return jsonify({"msg": "Wrong username or password"}), 401

    access_token = create_access_token(identity=id)
    return jsonify(access_token=access_token), 200


@app.route('/home', methods=['GET'])
@jwt_required()
def login_success():
    current_user = get_jwt_identity()
    message = "Welcome, create new tasks"
    
    return jsonify(msg=message), 200
    

@app.route('/new', methods=['GET','POST'])
@jwt_required()
def create_task():
    task_id = random.randint(1000, 1999)
    task_title = request.json.get("task_title", None)
    task = request.json.get("task", None)
    due_date = request.json.get("due_date", None)
    
    current_user = get_jwt_identity()
    task_info = Tasks(
            user_id = current_user,
            id = task_id,
            title = task_title,
            task = task,
            due = due_date
        )

    db.session.add(task_info)
    db.session.commit()

    message = "Task added succesfully"
    return jsonify(msg=message), 201


@app.route('/tasks', methods=['GET'])
@jwt_required()
def view_tasks():
    tasks = Tasks.query.all()
    for items in tasks:
        info = {"id":items.id, "task":items.title}

        return jsonify(msg=info), 200


@app.route('/tasks/<id>', methods=['GET'])
@jwt_required()
def view_task(id):
    task = Tasks.query.get(id)

    return jsonify(msg=task.title), 200


@app.route('/tasks/<id>/update', methods=['PUT'])
@jwt_required()
def update_task(id):
    current_task = Tasks.query.get(id)

    task = request.json.get("task", None)
    due_date = request.json.get("due_date", None)
    
    task_info = Tasks(
            user_id = current_task.user_id,
            title = current_task.title,
            task = task,
            due = due_date
        )

    db.session.add(task_info)
    message = "Task {} updated successfully".format(id)
    return jsonify(msg=message), 200


@app.route('/tasks/<id>/delete', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    current_task = Tasks.query.get(id)

    db.session.delete(current_task)
    message = "Task {} deleted successfully".format(id)
    return jsonify(msg=message), 200


if __name__ == '__main__':
    app.run(debug=True)
