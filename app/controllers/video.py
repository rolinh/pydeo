from bottle import template

from app.controllers.application_controller import ApplicationController

class VideoController(ApplicationController):

    def movies(self):
        return template('video/movies.tpl')

    def series(self):
        return template('video/series.tpl')
