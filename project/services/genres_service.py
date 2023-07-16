from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Genre


class GenresService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, genre_id: int) -> Genre:
        if genre := self.dao.get_by_id(genre_id):
            return genre
        raise ItemNotFound(f'Genre with id={genre_id} not exists.')

    def get_all(self, page: Optional[int] = None):
        return self.dao.get_all(page=page)
