from flask import Response, request
from databases.models import Task
from flask_restful import Resource


class TasksApi(Resource):
    def get(self):
        movies = Task.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        task = Task(**body).save()
        id = task.id

        return {'id': str(id)}, 200


class TaskAPI(Resource):
    def put(self, index):
        body = request.get_json()
        Task.objects(id=index).update(**body)
        return '', 200

    def delete(self, index):
        Task.objects.get(id=index).delete()
        return 'None', 200

    def get(self, index):
        tasks = Task.objects.get(id=index).to_json()
        return Response(tasks, mimetype='application/json', status=200)
