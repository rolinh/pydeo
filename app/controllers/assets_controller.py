from bottle import static_file

from app.controllers.application_controller import ApplicationController


class AssetsController(ApplicationController):
    """Class for handling static assets."""

    def favicon():
        return static_file('favicon.png', root='app/assets/img')

    def images(filename):
        return static_file(filename, root='app/assets/img')

    def javascripts(filename):
        return static_file(filename, root='app/assets/js')

    def javascripts_libs(filename):
        return static_file(filename, root='app/assets/js/lib')

    def stylesheets(filename):
        return static_file(filename, root='app/assets/css')
