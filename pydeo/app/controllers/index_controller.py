from bottle import mako_template as template

from pydeo.app.controllers.application_controller import ApplicationController


class IndexController(ApplicationController):
    """Class for handling index page."""

    def index(self):
        """Render index page."""
        return template('home/index.tpl')
