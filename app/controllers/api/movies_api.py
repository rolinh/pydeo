import json

from sqlalchemy.orm.exc import NoResultFound

from app.models.movie import Movie
from app.helpers import application_helper as ah
from app.helpers import movies_helper as mh


class MoviesAPIController():
    """Class to handle RESTful API for movies."""

    def movies(self, db):
        """Return all movies."""
        movies = db.query(Movie).all()
        return json.dumps(movies, cls=ah.AlchemyEncoder)

    def movies_title(self, db):
        """Return movies title."""
        movies = [m.title for m in db.query(Movie).all()]
        return json.dumps(movies, cls=ah.AlchemyEncoder)

    def movies_id(self, db, id):
        """Return a movie corresponding to the given id."""
        try:
            movie = db.query(Movie).filter_by(id=id).one()
        except NoResultFound:
            movie = {}
        return json.dumps(movie, cls=ah.AlchemyEncoder)

    def movies_reload(self, db):
        """Reload movie database actually fetching info from IMDB for movies
        that where not in database previously."""
        mh.update_movies_db(db)
        return "OK"
