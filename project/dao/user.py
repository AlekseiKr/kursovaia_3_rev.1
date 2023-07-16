from project.models import User

class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(User).get(id)

    def get_by_email(self,email):
        return self.session.query(User).filter(User.email == email).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_data):
        user = User(**user_data)

        self.session.add(user)
        self.session.commit()

        return user

    def delete(self, id):
        user = self.get_one(id)

        self.session.delete(user)
        self.session.commit()

    def update(self, user_data):
        self.session.add(user_data)
        self.session.commit()

        return user_data

    def update_partial(self, user):
        self.session.add(user)
        self.session.commit()

        return user

