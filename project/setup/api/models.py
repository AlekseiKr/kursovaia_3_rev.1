from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Квентин Тарантино'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, example='Сияние'),
    'description': fields.String(example='Джек Торренс с женой и сыном ...'),
    'trailer': fields.String(example='https://www.youtube.com/watch?v=NMSUEhDWXH0'),
    'year': fields.Integer(example=1980),
    'rating': fields.String(example=8.4),
    'genre_id': fields.Integer(example=6),
    'director_id': fields.Integer(example=14),
})

user: Model = api.model('Пользователь',{
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, example='ivanov@mail.ru'),
    'password': fields.String(required=True, example='password'),
    'name': fields.String(required=True, example='Ivan'),
    'surname': fields.String(required=True, example='Ivanov'),
    'favourite_genre': fields.Integer(example=3),
})