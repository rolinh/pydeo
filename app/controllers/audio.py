from bottle import template

from app.controllers.application_controller import ApplicationController

class AudioController(ApplicationController):

    def music(self):
        return template('audio/music.tpl')
