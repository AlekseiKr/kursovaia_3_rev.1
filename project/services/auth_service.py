import calendar
import datetime

import jwt

from flask import abort
from project.config import config
from project.services.users_services import UsersService

JWT_SECRET = config.SECRET_KEY
JWT_ALGORITHM = config.JWT_ALGORITHM

TOKEN_EXPIRE_MINUTES = config.TOKEN_EXPIRE_MINUTES
TOKEN_EXPIRE_DAYS = config.TOKEN_EXPIRE_DAYS

class AuthService:

    def __init__(self, user_service: UsersService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            raise abort(404)

        if not is_refresh:

            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            "email": user.email
        }

        # 30 min access_token живет
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRE_MINUTES)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)
        # 130 days refresh_token живет
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=TOKEN_EXPIRE_DAYS)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {"access_token": access_token,
                "refresh_token": refresh_token
                }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=JWT_ALGORITHM)
        username = data.get("username")

        return self.generate_tokens(username, None, is_refresh=True)