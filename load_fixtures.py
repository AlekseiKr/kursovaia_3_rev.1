from typing import Any, Dict, List, Type
from project.models import Movie
from project.setup.db import db, models


def load_data(data: List[Dict[str, Any]], model: Type[models.Base]) -> None:
    for item in data:
        db.session.add(model(**item))

def load_movies_data(movies: List[Dict[str, Any]], model: Type[Movie]):
    for movie in movies:
        db.session.add(model(**movie))



