from flask_restx import Namespace, Resource
from project.container import user_service
from project.setup.api.models import user
from flask import request
from project.tools.decorators import auth_required
import jwt
from project.config import config

JWT_SECRET = config.SECRET_KEY
JWT_ALGORITHM = config.JWT_ALGORITHM

api = Namespace('user')


@api.route('/')
class UserView(Resource):

    # @api.response(404, 'Not Found')

    @api.marshal_list_with(user)
    @auth_required
    def get(self):

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]

        user_info = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        email = user_info["email"]
        exist_user = user_service.get_by_email(email)
        """
        Get user info.
        """
        return user_service.get_one(exist_user.id)

    @api.marshal_with(user, code=201)
    @auth_required
    def patch(self):

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]

        user_info = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        email = user_info["email"]
        exist_user = user_service.get_by_email(email)

        updated_info = request.json

        return user_service.update_partial(exist_user, updated_info), 201






