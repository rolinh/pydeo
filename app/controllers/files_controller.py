from bottle import static_file

from app.controllers.application_controller import ApplicationController


class FilesController(ApplicationController):
    """Class for handling static files, such as media files."""

    def movies(filename):
        return static_file(filename, root='files/movies')
