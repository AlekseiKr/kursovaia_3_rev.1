from project.models import Movie
from typing import Generic, Optional, TypeVar
from werkzeug.exceptions import NotFound
from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import scoped_session


from flask import current_app

T = TypeVar('T', bound=Movie)

class MoviesDAO(Generic[T]):
    __model__ = Movie

    def __init__(self,db_session: scoped_session) -> None:
        self._db_session = db_session

    @property
    def _items_per_page(self) -> int:
        return current_app.config['ITEMS_PER_PAGE']

    def get_by_id(self, id: int) -> Optional[T]:

        return self._db_session.query(self.__model__).get(id)

    def get_by_title(self, title):

        return self._db_session.query(self.__model__).get(title)

    def get_all(self, page: Optional[int] = None):
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()

    def create(self, movie_data):

        movie = Movie(**movie_data)

        self._db_session.add(movie)
        self._db_session.commit()

        return movie

    def delete(self, id):

        movie = self.get_by_id(id)

        self._db_session.delete(movie)
        self._db_session.commit()

    def update(self, movie_data):

        self._db_session.add(movie_data)
        self._db_session.commit()

        return movie_data

    def update_partial(self, movie):

        self._db_session.add(movie)
        self._db_session.commit()

        return movie


