from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from databases.db import Base

from marshmallow import Schema, fields, validate


class TaskSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True, validate=validate.Length(min=3, max=255))
    describe = fields.Str(required=True)
    autor = fields.Str(required=True)
    projectId = fields.Int(required=True)
    createdAt = fields.DateTime(dump_only=True)
    updatedAt = fields.DateTime(dump_only=True)


class Task(Base):
    __tablename__ = "Task"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    describe = Column(String(50))
    autor = Column(String(50))
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=True)

    def __init__(self, name=None, describe=None, autor=None):
        self.name = name
        self.describe = describe
        self.autor = autor

    def __repr__(self):
        return f"<Task {self.name}>"


class ProjectSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True, validate=validate.Length(min=3, max=255))
    createdAt = fields.DateTime(dump_only=True)
    updatedAt = fields.DateTime(dump_only=True)


class Project(Base):
    __tablename__ = "Project"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=True)

    def __init__(self, name=None, describe=None, autor=None):
        self.name = name
        self.describe = describe
        self.autor = autor

    def __repr__(self):
        return f"<Project {self.name}>"
