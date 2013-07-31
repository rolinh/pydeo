import json

from app.models import movie
from app.helpers import application_helper as ah
from app.helpers import movies_helper as mh
from lib.controllers import db_connector as db

class MoviesAPIController():

    def movies(self):
        """Return all movies."""
        sess = db.DbConnector.session
        movies = sess.query(movie.Movie).all()
        return json.dumps(movies, cls=ah.AlchemyEncoder)

    def movies_title(self):
        """Return movies title."""
        sess = db.DbConnector.session
        movies = [m.title for m in sess.query(movie.Movie).all()]
        return json.dumps(movies, cls=ah.AlchemyEncoder)

    def movies_reload(self):
        """Reload movie database actually fetching info from IMDB for movies
        that where not in database previously."""
        mh.update_movies_db()
        return "OK"
