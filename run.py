from project.config import config
from project.models import Genre, Director, Movie
from project.server import create_app, db
from load_fixtures import load_data, load_movies_data
from typing import Dict, List, Any
from project.utils_ok import read_json
from sqlalchemy.exc import IntegrityError
from contextlib import suppress

app = create_app(config)

def add_information(db, app):

    fixtures: Dict[str, List[Dict[str, Any]]] = read_json("fixtures.json")

    with app.app_context():

        db.create_all() #Создаем таблицы

        # TODO: [fixtures] Добавить модели Directors и Movies
        load_data(fixtures['genres'], Genre)
        load_data(fixtures['directors'], Director)
        load_movies_data(fixtures['movies'], Movie)

        with suppress(IntegrityError):
            db.session.commit()


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
    }

if __name__ == '__main__':

    add_information(db, app)
    app.run(host='127.0.0.1', port=25000)


