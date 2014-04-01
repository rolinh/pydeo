__version__ = '0.1.0'

import bottle
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine

from pydeo.app.models import Base
from pydeo.config import (
    routes,
    settings
)


class Pydeo:

    def __init__(self,
                 server='auto',
                 host='0.0.0.0',
                 port=8080,
                 db_url='sqlite:///:memory:',
                 db_echo=False,
                 reloader=False,
                 debug=False,
                 template_path='./pydeo/app/views/'):
        self.server_type = server
        self.host = host
        self.port = port
        self.reloader = reloader
        self.debug = debug
        self.dir_list = ['files/' + s for s in [settings.music_dir,
                                                settings.movies_dir,
                                                settings.series_dir]]

        self.app = bottle.Bottle()

        routes.setup_routing(self.app)
        if template_path not in bottle.TEMPLATE_PATH:
            bottle.TEMPLATE_PATH.append(template_path)
        if './' in bottle.TEMPLATE_PATH:
            bottle.TEMPLATE_PATH.remove('./')
        if './views' in bottle.TEMPLATE_PATH:
            bottle.TEMPLATE_PATH.remove('./views')

        bottle.debug(self.debug)

        engine = create_engine(db_url, echo=db_echo)

        sqlalchemy_plugin = sqlalchemy.Plugin(
            engine,
            Base.metadata,
            keyword='db',
            create=True,
            commit=True,
            use_kwargs=False
        )
        self.app.install(sqlalchemy_plugin)
