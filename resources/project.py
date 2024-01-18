from flask import Response, request
from flask_restful import Resource

from sqlalchemy.sql import func

from databases.models import Project, ProjectSchema
from databases.db import db


class ProjectsApi(Resource):
    def __init__(self):
        self.project_shema = ProjectSchema(many=True)
        self.project_shemaOne = ProjectSchema()

    def get(self):
        projects = Project.query.all()
        result = self.project_shema.dump(projects)
        return result, 200

    def options(self):
        return {}, 200

    def post(self):
        body = request.get_json()
        error = self.project_shemaOne.validate(body)
        if error:
            return error, 422

        project = Project(**self.project_shemaOne.load(body))
        db["session"].add(project)
        db["session"].commit()

        return self.project_shemaOne.dump(project), 200


class ProjectAPI(Resource):
    def __init__(self):
        self.project_shemaOne = ProjectSchema()

    def put(self, id):
        body = request.get_json()
        error = ProjectSchema().validate(body)
        if error:
            return error, 422

        project = Project.query.where(Project.id == id).update(
            dict(**ProjectSchema().load(body), updatedAt=func.now())
        )

        db["session"].commit()

        project = Project.query.filter(Project.id == id).first()
        return self.project_shemaOne.dump(project)

    def delete(self, id):
        project = Project.query.filter(Project.id == id).first()
        db["session"].delete(project)
        db["session"].commit()
        return {"id": id}, 200

    def get(self, id):
        project = Project.query.filter(Project.id == id).first()
        return self.project_shemaOne.dump(project)
