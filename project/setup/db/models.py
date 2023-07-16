from sqlalchemy import Column, Integer, String

from project.setup.db import db


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
