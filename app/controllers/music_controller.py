from bottle import mako_template as template

from app.controllers.application_controller import ApplicationController

class MusicController(ApplicationController):

    def music(self):
        """Render /music page."""
        return template('music/index.tpl')
