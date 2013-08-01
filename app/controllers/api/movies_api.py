import json

from sqlalchemy.orm.exc import NoResultFound

from app.models.movie import Movie
from app.helpers import application_helper as ah
from app.helpers import movies_helper as mh
from lib.controllers import db_connector as db

class MoviesAPIController():

    def movies(self):
        """Return all movies."""
        sess = db.DbConnector.session
        movies = sess.query(Movie).all()
        return json.dumps(movies, cls=ah.AlchemyEncoder)

    def movies_title(self):
        """Return movies title."""
        sess = db.DbConnector.session
        movies = [m.title for m in sess.query(Movie).all()]
        return json.dumps(movies, cls=ah.AlchemyEncoder)

    def movies_id(self, id):
        """Return a movie corresponding to the given id."""
        sess = db.DbConnector.session
        try:
            movie = sess.query(Movie).filter_by(id=id).one()
        except NoResultFound:
            movie = {}
        return json.dumps(movie, cls=ah.AlchemyEncoder)

    def movies_reload(self):
        """Reload movie database actually fetching info from IMDB for movies
        that where not in database previously."""
        mh.update_movies_db()
        return "OK"
