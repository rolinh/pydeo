from bottle import mako_template as template

from pydeo.app.controllers.application_controller import ApplicationController


class MusicController(ApplicationController):
    """Class for handling music page."""

    def index(self):
        """Render /music page."""
        return template('music/index.tpl')
