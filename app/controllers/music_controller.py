from bottle import template

from app.controllers.application_controller import ApplicationController

class MusicController(ApplicationController):

    def music(self):
        """Render /music page."""
        return template('audio/music.tpl')
