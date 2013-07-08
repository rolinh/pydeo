from bottle import template

from app.controllers.application_controller import ApplicationController

class ErrorsController(ApplicationController):

    def error_404(self):
        return template('errors/404.tpl')

    def error_500(self):
        return template('errors/500.tpl')

