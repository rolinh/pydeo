from bottle import mako_template as template

from app.controllers.application_controller import ApplicationController

class SeriesController(ApplicationController):

    def index(self):
        """Render /series page."""
        return template('series/index.tpl')
