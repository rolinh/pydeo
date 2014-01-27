from bottle import mako_template as template

from app.controllers.application_controller import ApplicationController


class MoviesController(ApplicationController):
    """Class for handling movies page."""

    def index(self):
        """Render /movies page."""

        return template('movies/index.tpl')

    def movie(self, id):
        """Render /movie/id/<id> page for a detailed view of a movie."""

        return template('movies/movie.tpl', id=id)
