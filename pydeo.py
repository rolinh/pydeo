#!/usr/bin/env python
# coding: utf-8

__version__ = '0.1.0'

import sys
import bottle

from app.helpers import files_dir_helper
from config import environment
from config import routes
from config import settings
from lib.controllers import db_connector as db
from lib.models import  base_initializer as b

class Pydeo:

    def __init__(self,
                 host='0.0.0.0',
                 port=8080,
                 reloader=False,
                 debug=False,
                 template_path='./app/views/'):
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

        db.DbConnector.init()
        b.BaseInitializer.get_base()
        b.BaseInitializer.Base.metadata.create_all(db.DbConnector.engine)

if __name__ == "__main__":
    a = Pydeo(host=settings.host,
              port=settings.port,
              reloader=environment.reloader,
              debug=environment.debug)
    chk_dir = files_dir_helper.check_dir_presence(a.dir_list)
    if chk_dir != 'OK':
        sys.stderr.write(('At least one of the media folders set in settings '
                          'does not seem to exist: {}\n').format(chk_dir))
        sys.exit(1)

    bottle.run(a.app, reloader=a.reloader, host=a.host, port=a.port)
