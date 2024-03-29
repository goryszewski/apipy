from flask import Response, request
from flask_restful import Resource

from sqlalchemy.sql import func

from databases.models import Task, TaskSchema
from databases.db import db


class TasksApi(Resource):
    def __init__(self):
        self.task_shema = TaskSchema(many=True)
        self.task_shemaOne = TaskSchema()

    def get(self):
        tasks = Task.query.all()
        result = self.task_shema.dump(tasks)
        return result, 200

    def options(self):
        return {}, 200

    def post(self):
        body = request.get_json()
        error = self.task_shemaOne.validate(body)
        if error:
            return error, 422

        task = Task(**self.task_shemaOne.load(body))
        db["session"].add(task)
        db["session"].commit()

        return self.task_shemaOne.dump(task), 200


class TaskAPI(Resource):
    def __init__(self):
        self.task_shemaOne = TaskSchema()

    def put(self, id):
        body = request.get_json()
        error = TaskSchema().validate(body)
        if error:
            return error, 422

        task = Task.query.where(Task.id == id).update(
            dict(**TaskSchema().load(body), updatedAt=func.now())
        )

        db["session"].commit()

        task = Task.query.filter(Task.id == id).first()
        return self.task_shemaOne.dump(task)

    def delete(self, id):
        task = Task.query.filter(Task.id == id).first()
        db["session"].delete(task)
        db["session"].commit()
        return {"id": id}, 200

    def get(self, id):
        task = Task.query.filter(Task.id == id).first()
        return self.task_shemaOne.dump(task)
