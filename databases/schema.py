from marshmallow import Schema, fields, validate


class TaskSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3, max=255))
    describe = fields.Str(required=True)
    autor = fields.Str(required=True)
