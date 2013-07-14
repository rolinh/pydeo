from bottle import template

from app.controllers.application_controller import ApplicationController

class ErrorsController(ApplicationController):

    def error_404(self):
        """Render 404 error page."""
        return template('errors/404.tpl')

    def error_500(self):
        """Render 500 error page."""
        return template('errors/500.tpl')

