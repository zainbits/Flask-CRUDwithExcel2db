from quants import ma
from marshmallow import fields


class UserSchema(ma.Schema):
    
    id = fields.String()
    name = fields.String()
    title = fields.String()
    groupname = fields.String()
    reporting_manager = fields.String()
    project = fields.String()