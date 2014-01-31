from bottle import mako_template as template

from pydeo.app.controllers.application_controller import ApplicationController


class SeriesController(ApplicationController):
    """Class for handling series page."""

    def index(self):
        """Render /series page."""
        return template('series/index.tpl')
