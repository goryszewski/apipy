from .db import db


class Task(db.Document):
    name = db.StringField(required=True, unique=True)
    describe = db.StringField(required=True)
    autor = db.StringField(required=True)


class Project(db.Document):
    name = db.StringField(required=True, unique=True)


class Images(db.Document):
    name = db.StringField(required=True, unique=True)
    version = db.StringField(required=True)
    autor = db.StringField(required=True)
