from bottle import mako_template as template

from app.controllers.application_controller import ApplicationController


class MoviesController(ApplicationController):
    """Class for handling movies page."""

    def index(self):
        """Render /movies page."""

        return template('movies/index.tpl')
