#!/usr/bin/env python
# coding: utf-8

__version__ = '0.1.0'

import sys
import bottle
from bottle.ext import sqlalchemy
from logging import info
from sqlalchemy import create_engine

from app.helpers import files_dir_helper
from app.models.base import Base
from config import environment
from config import routes
from config import settings


class Pydeo:

    def __init__(self,
                 server='auto',
                 host='0.0.0.0',
                 port=8080,
                 db_url='sqlite:///:memory:',
                 db_echo=False,
                 reloader=False,
                 debug=False,
                 template_path='./app/views/'):
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
        if not template_path in bottle.TEMPLATE_PATH:
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


if __name__ == "__main__":
    info('Pydeo started')
    db_url = settings.db_url
    server = settings.server
    if not db_url:
        db_url = environment.db_url
    if not server:
        server = environment.server

    info('\nApplication settings:\n'
         'server = %s\n'
         'host = %s\n'
         'port = %s\n'
         'db_url = %s\n'
         'db_echo = %s\n'
         'reloader = %s\n'
         'debug = %s\n',
         server,
         settings.host,
         settings.port,
         db_url,
         environment.db_echo,
         environment.reloader,
         environment.debug)
    a = Pydeo(
        server=server,
        host=settings.host,
        port=settings.port,
        db_url=db_url,
        db_echo=environment.db_echo,
        reloader=environment.reloader,
        debug=environment.debug
    )
    chk_dir = files_dir_helper.check_dir_presence(a.dir_list)
    if chk_dir != 'OK':
        sys.stderr.write(('At least one of the media folders set in settings '
                          'does not seem to exist: {}\n').format(chk_dir))
        sys.exit(1)

    bottle.run(
        a.app,
        server=a.server_type,
        reloader=a.reloader,
        host=a.host,
        port=a.port
    )
