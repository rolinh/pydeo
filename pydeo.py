#!/usr/bin/env python
# coding: utf-8

__version__ = '0.1.0'

import bottle

from config import environment
from config import routes
from config import settings

class Pydeo:

    def __init__(self, host='0.0.0.0', port=8080, reloader=False, debug=False):
        self.host = host
        self.port = port
        self.reloader = reloader
        self.debug = debug

        self.app = bottle.Bottle()

        routes.setup_routing(self.app)
        bottle.TEMPLATE_PATH.append("./app/views/")
        bottle.TEMPLATE_PATH.remove("./")
        bottle.TEMPLATE_PATH.remove("./views/")

        bottle.debug(self.debug)

if __name__ == "__main__":
    a = Pydeo(host=settings.host,
              port=settings.port,
              reloader=environment.reloader,
              debug=environment.debug)
    bottle.run(a.app, reloader=a.reloader, host=a.host, port=a.port)
