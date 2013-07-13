from bottle import template

from app.controllers.application_controller import ApplicationController

class SeriesController(ApplicationController):

    def series(self):
        """Render /series page."""
        return template('video/series.tpl')
