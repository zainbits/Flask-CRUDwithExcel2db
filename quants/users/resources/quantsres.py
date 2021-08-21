from flask_restplus import Resource
from flask import request, make_response

from quants import db
from quants.users.models import UserModel
from quants.users.schema import UserSchema

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError


class Quants(Resource):

    def get(self):
        user_schema = UserSchema()
        users_schema = UserSchema(many=True)
        if request.method == 'GET':
            arg = request.args.get('id')
            if arg:
                data = UserModel.query.filter_by(id=arg).first()
                res = user_schema.dump(data)
                return res

            data = UserModel.query.all()
            res = users_schema.dump(data)
            return res

    def post(self):
        post_args = request.get_json(force=True)
        try:

            schema = UserSchema()
            datain = schema.load(post_args)
            print(datain)
            user = UserModel(**post_args)
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return make_response({"error": "user already exists"}, 403)
        return make_response({'msg': 'user inserted successfully', 'user id': user.id, 'username': user.name}, 201)

    def put(self, quant_id):
        post_args = request.get_json(force=True)
        UserModel.query.filter_by(id=quant_id).update(post_args)
        db.session.commit()
        data = UserModel.query.filter_by(id=quant_id).first()
        return UserSchema().dump(data)

    def delete(self, quant_id):
        try:
            data = UserModel.query.filter_by(id=quant_id).first()
            db.session.delete(data)
            db.session.commit()
        except UnmappedInstanceError:
            return {'msg': 'User does not exist'}
        return {'msg': 'deleted successfully'}


# User ORM for upload excel