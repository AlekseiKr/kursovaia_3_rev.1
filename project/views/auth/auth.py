from flask_restx import Namespace, Resource
from flask import request
from project.container import auth_service
from project.container import user_service

api = Namespace('auth')

@api.route('/register/')
class AuthsView(Resource):
 
    def post(self):
        user_data = request.json
        user = user_service.create(user_data)

        return "", 201, {"location":f"/users/{user.id}"}


@api.route('/login/')
class Login(Resource):

    def post(self):

        data = request.json
        email = data.get("email", None)
        password = data.get("password", None)

        if None in [email, password]:
            return "Данные не корректны", 400

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 201

    def put(self):
        req_json = request.json
        token = req_json.get("refresh_token")
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201

