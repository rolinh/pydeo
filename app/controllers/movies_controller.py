from bottle import template

from app.controllers.application_controller import ApplicationController

class MoviesController(ApplicationController):

    def movies(self):
        """Render /movies page."""
        return template('video/movies.tpl')

