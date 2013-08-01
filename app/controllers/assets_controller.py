from bottle import static_file

from app.controllers.application_controller import ApplicationController


class AssetsController(ApplicationController):

    def favicon():
        return static_file('favicon.png', root='app/assets/img')

    def images(filename):
        return static_file(filename, root='app/assets/img')

    def javascripts(filename):
        return static_file(filename, root='app/assets/js')

    def stylesheets(filename):
        return static_file(filename, root='app/assets/css')
