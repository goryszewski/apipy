from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("task")

todos = {}


class Todo(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        args = parser.parse_args()
        task = {"task": args["task"]}
        todos[todo_id] = task
        return task, 201

    def delete(self, todo_id):
        if todo_id not in todos:
            abort(404, message="TODO {} doesn't exist".format(todo_id))

        del todos[todo_id]
        return "", 204


class TodoList(Resource):
    def get(self):
        return todos


api.add_resource(Todo, "/<string:todo_id>")
api.add_resource(TodoList, "/")
if __name__ == "__main__":
    app.run(debug=True)
