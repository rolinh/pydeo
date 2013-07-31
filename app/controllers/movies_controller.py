from bottle import mako_template as template

from app.controllers.application_controller import ApplicationController
from app.models import movie
from lib.controllers import db_connector as db

class MoviesController(ApplicationController):

    def movies(self):
        """Render /movies page."""

        sess = db.DbConnector.session
        movies_title = sess.query(movie.Movie.title).order_by(movie.Movie.title).all()

        return template('movies/index.tpl', movies_title=movies_title)

