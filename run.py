#!/usr/bin/env python
# coding: utf-8

import bottle
from logging import info
import sys

from pydeo import Pydeo
from pydeo.app.helpers import files_dir_helper
from pydeo.config import (
    environment,
    settings
)


def main():
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

if __name__ == "__main__":
    main()
