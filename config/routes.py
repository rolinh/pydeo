from bottle import route

from app.controllers.audio import AudioController
from app.controllers.assets import AssetsController
from app.controllers.errors import ErrorsController
from app.controllers.index import IndexController
from app.controllers.video import VideoController

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
    app.route('/music', 'GET', AudioController().music)

    # video
    app.route('/movies', 'GET', VideoController().movies)
    app.route('/series', 'GET', VideoController().series)
