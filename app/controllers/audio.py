from bottle import template

from app.controllers.application_controller import ApplicationController

class AudioController(ApplicationController):

    def index(self):
        return template('audio/index.tpl')

    def music(self):
        return template('audio/music.tpl')
