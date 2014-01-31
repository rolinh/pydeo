from bottle import static_file

from app.controllers.application_controller import ApplicationController


class AssetsController(ApplicationController):
    """Class for handling static assets."""

    def favicon():
        return static_file('favicon.png', root='app/assets/img')

    def img(filename):
        return static_file(filename, root='app/assets/img')

    def js(filename):
        return static_file(filename, root='app/assets/js')

    def js_lib(filename):
        return static_file(filename, root='app/assets/js/lib')

    def swf(filename):
        return static_file(filename, root='app/assets/swf')

    def css(filename):
        return static_file(filename, root='app/assets/css')

    def css_lib(filename):
        return static_file(filename, root='app/assets/css/lib')

    def css_lib_font(filename):
        return static_file(filename, root='app/assets/css/lib/font')

    def css_fonts(filename):
        return static_file(filename, root='app/assets/css/fonts')
