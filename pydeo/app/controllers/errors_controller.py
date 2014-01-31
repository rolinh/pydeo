from bottle import mako_template as template

from pydeo.app.controllers.application_controller import ApplicationController


class ErrorsController(ApplicationController):
    """Class for handling HTTP errors."""

    def error_404(self):
        """Render 404 error page."""
        return template('errors/404.tpl')

    def error_500(self):
        """Render 500 error page."""
        return template('errors/500.tpl')
