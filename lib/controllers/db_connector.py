from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbConnector():
    session = None
    engine = None

    @staticmethod
    def init(db_url='sqlite:///:memory:'):
        DbConnector.engine = create_engine(db_url, echo=True)
        Session = sessionmaker(bind=DbConnector.engine)
        DbConnector.session = Session()
