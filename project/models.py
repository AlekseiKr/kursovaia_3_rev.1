from sqlalchemy import Column, String, Integer, Float, ForeignKey, VARCHAR

from project.setup.db import models, db


class Genre(models.Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

class Director(models.Base):
    __tablename__ = 'directors'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(300))
    description = Column(String(300))
    trailer = Column(String(300))
    year = Column(Integer)
    rating = VARCHAR((100))
    genre_id = Column(Integer, ForeignKey(Genre.id))
    director_id = Column(Integer, ForeignKey(Director.id))

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    favourite_genre = Column(Integer, ForeignKey(Genre.id))




