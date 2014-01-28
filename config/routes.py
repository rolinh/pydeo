from bottle import route

from app.controllers.assets_controller import AssetsController
from app.controllers.errors_controller import ErrorsController
from app.controllers.files_controller import FilesController
from app.controllers.index_controller import IndexController
from app.controllers.movies_controller import MoviesController
from app.controllers.music_controller import MusicController
from app.controllers.series_controller import SeriesController

from app.controllers.api.movies_api import MoviesAPIController


def setup_routing(app):
    # static files
    app.route('/img/<filename>', 'GET', AssetsController.images)
    app.route('/js/<filename>', 'GET', AssetsController.javascripts)
    app.route('/js/lib/<filename>', 'GET', AssetsController.javascripts_libs)
    app.route('/css/<filename>', 'GET', AssetsController.stylesheets)
    app.route('/css/font/<filename>', 'GET', AssetsController.fonts)
    app.route('/swf/<filename>', 'GET', AssetsController.flash)
    app.route('/favicon.ico', 'GET', AssetsController.favicon)
    app.route('/favicon.png', 'GET', AssetsController.favicon)
    app.route('/files/movies/<filename>', 'GET', FilesController.movies)

    # errors
    app.route('/error/404', 'GET', ErrorsController().error_404)
    app.route('/error/500', 'GET', ErrorsController().error_500)

    # home
    app.route('/', 'GET', IndexController().index)

    # music
    app.route('/music', 'GET', MusicController().index)

    # movies
    app.route('/movies', 'GET', MoviesController().index)
    app.route('/movies/id/<id>', 'GET', MoviesController().movie)

    # series
    app.route('/series', 'GET', SeriesController().index)

    # REST API routes
    # movies
    app.route('/api/movies', 'GET', MoviesAPIController().movies)
    app.route('/api/movies/reload', 'GET', MoviesAPIController().movies_reload)
    app.route('/api/movies/title', 'GET', MoviesAPIController().movies_title)
    app.route('/api/movies/id/<id>', 'GET', MoviesAPIController().movies_id)
