#!/usr/bin/env python
# coding: utf-8

__version__ = '0.1.0'

from bottle import Bottle
from bottle import TEMPLATE_PATH
from bottle import debug
from bottle import run

from app.controllers import *
from config import environment
from config import routes
from config import settings

app = Bottle()
TEMPLATE_PATH.append("./app/views/")
TEMPLATE_PATH.remove("./")
TEMPLATE_PATH.remove("./views/")

debug(environment.debug)

if __name__ == "__main__":
    routes.setup_routing(app)
    run(app, reloader=environment.reloader, host=settings.host, port=settings.port)
