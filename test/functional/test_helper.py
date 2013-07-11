import sys

sys.path = ['../..'] + sys.path

import pydeo

def get_app():
    return pydeo.Pydeo('localhost',
                       8080,
                       False,
                       True,
                       '../../app/views/').app

