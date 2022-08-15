import bcrypt
from flask import request
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required
from app.users.model import User
from app.users.schema import UserSchema, UserLoginSchema
from app.utils.filters import filters


class UserList(MethodView):     # /users
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=UserSchema, many=True)
        users = User.query.all()
        return schema.dump(users), 200


    def post(self):
        data = request.json

        possible_user = User.query.filter_by(username=data['username']).first()
        if possible_user:
            return {'error': 'username already chosen'}

        schema = UserSchema()
        user = schema.load(data)
        user.save()
        return schema.dump(user), 201


class UserId(MethodView):       # /users/<id>
    decorators = [jwt_required()]
    def get(self, id):
        schema = filters.getSchema(qs=request.args, schema_cls=UserSchema)
        user = User.query.get_or_404(id)
        return schema.dump(user), 200


    def put(self, id):
        try:
            user = User.query.get_or_404(id)
        except:
            return {'error': 'user not found'}, 404
        
        data = request.json
        schema = UserSchema(exclude=['password'])
        user = schema.load(data, instance=user)
        user.update()
        return schema.dump(user), 200


    def patch(self, id):
        try:
            user = User.query.get_or_404(id)
        except:
            return {'error': 'user not found'}, 404
        
        data = request.json
        schema = UserSchema(exclude=['password'])
        user = schema.load(data, instance=user, partial=True)
        user.update()
        return schema.dump(user), 200
    

    def delete(self, id):
        try:
            user = User.query.get_or_404(id)
        except:
            return {'error': 'user not found'}, 404
        
        User.delete(user)
        return {}, 204


class UserLogin(MethodView):
    def post(self):
        schema = UserLoginSchema()
        data = schema.load(request.json)

        username = data['username']
        passw = data['password']

        user = User.query.filter_by(username=username).first()

        if not user or not bcrypt.hashpw(passw.encode(), bcrypt.gensalt()):
            return {'error': 'invalid username or password'}, 404

        
        token = create_access_token(identity=user.id)
        return {
            'user': UserSchema().dump(user),
            'token': token
        }, 200

