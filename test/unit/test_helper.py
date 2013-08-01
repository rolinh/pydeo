import sys

sys.path = ['../..'] + sys.path

from lib.controllers import db_connector as db
from lib.models import base_initializer as b


def init():
    db.DbConnector.init()
    b.BaseInitializer.get_base()
    b.BaseInitializer.Base.metadata.create_all(db.DbConnector.engine)
