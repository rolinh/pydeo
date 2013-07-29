from sqlalchemy.ext.declarative import declarative_base

class BaseInitializer:
    Base = None

    def get_base():
        if BaseInitializer.Base == None:
            BaseInitializer.Base = declarative_base()

        return BaseInitializer.Base
