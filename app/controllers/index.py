from bottle import template

from app.controllers.application_controller import ApplicationController

class IndexController(ApplicationController):

    def index(self):
        return template('home/index.tpl')
