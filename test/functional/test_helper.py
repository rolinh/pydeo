import sys

sys.path = ['../..'] + sys.path

import pydeo


def get_app():
    return pydeo.Pydeo(template_path='../../app/views/').app
