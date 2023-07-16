from project.dao.movie import MoviesDAO
from project.models import Movie
from project.exceptions import ItemNotFound
from typing import Optional

class MoviesService:

    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao

    def get_item(self, id) -> Movie:
        if movie:= self.dao.get_by_id(id):
            return movie
        raise ItemNotFound(f'Movie with id={id} not exist.')

    def get_all(self, page: Optional[int] = None):
        return self.dao.get_all(page=page)

    def create(self, movie_data):
        return self.dao.create(movie_data)

    def update(self, movie_data):
        id = movie_data.get("id")

        movie = self.get_item(id)

        movie.title = movie_data.get("title")
        movie.description = movie_data.get("description")
        movie.trailer = movie_data.get("trailer")
        movie.year = movie_data.get("year")
        movie.rating = movie_data.get("rating")
        movie.genre_id = movie_data.get("genre_id")
        movie.director_id = movie_data.get("director_id")

        self.dao.update(movie)

    def delete(self, id):
        self.dao.delete(id)
