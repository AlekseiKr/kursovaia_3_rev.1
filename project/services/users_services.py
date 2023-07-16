import hmac

from project.dao.user import UserDAO
import base64
import hashlib
from project.config import BaseConfig

PWD_HASH_SALT = BaseConfig.PWD_HASH_SALT
PWD_HASH_ITERATIONS = BaseConfig.PWD_HASH_ITERATIONS

class UsersService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, id):
        return self.dao.get_one(id)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_data):
        user_data["password"] = self.generate_password(user_data["password"])
        return self.dao.create(user_data)

    def update(self, user_data):
        id = user_data.get("pk")

        user = self.get_one(id)

        user.email = user_data.get("email")
        user.password = user_data.get("password")
        user["password"] = self.generate_password(user["password"])
        user.name = user_data.get("name")
        user.surname = user_data.get("surname")
        user.favourite_genre = user_data.get("favourite_genre")

        self.dao.update(user)

    def update_partial(self, exist_user, updated_inf):

        for key in updated_inf.keys():

            if key == "email":
                exist_user.email = updated_inf["email"]

            if key == "name":
                exist_user.name = updated_inf["name"]

            if key == "surname":
                exist_user.surname = updated_inf["surname"]

            if key == "favourite_genre":
                exist_user.favourite_genre = updated_inf["favourite_genre"]

        self.dao.update_partial(exist_user)


    def delete(self, id):
        self.dao.delete(id)

    def generate_password(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password) -> bool:
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            other_password.encode("utf-8"),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digest)
