from bottle import mako_template as template

from app.controllers.application_controller import ApplicationController


class IndexController(ApplicationController):

    def index(self):
        """Render index page."""
        return template('home/index.tpl')
