from bottle import route

from app.controllers.assets_controller import AssetsController
from app.controllers.errors_controller import ErrorsController
from app.controllers.index_controller import IndexController
from app.controllers.movies_controller import MoviesController
from app.controllers.music_controller import MusicController
from app.controllers.series_controller import SeriesController

def setup_routing(app):
    # static files
    app.route('/img/<filename>', 'GET', AssetsController.images)
    app.route('/js/<filename>', 'GET', AssetsController.javascripts)
    app.route('/css/<filename>', 'GET', AssetsController.stylesheets)
    app.route('/favicon.ico', 'GET', AssetsController.favicon)
    app.route('/favicon.png', 'GET', AssetsController.favicon)

    # errors
    app.route('/error/404', 'GET', ErrorsController().error_404)
    app.route('/error/500', 'GET', ErrorsController().error_500)

    # home
    app.route('/', 'GET', IndexController().index)

    # audio
    app.route('/music', 'GET', MusicController().music)

    # video
    app.route('/movies', 'GET', MoviesController().movies)
    app.route('/series', 'GET', SeriesController().series)
