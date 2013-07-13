from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from datetime import datetime

class Movie():
    """Model of a movie."""

    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    imdb_id = Column(String)
    title = Column(String)
    type = Column(String)
    year = Column(Integer)
    tagline = Column(String)
    plot_outline = Column(String)
    runtime = Column(String)
    poster_url = Column(String)
    cover_url = Column(String)
    release_date = Column(String)
    certification = Column(String)
    trailer_img_url = Column(String)
    directors = Column(String)
    creators = Column(String)
    cast_summary = Column(String)
    credits = Column(String)
    writers = Column(String)
    trailers = Column(String)
    view_count = Column(Integer)
    user_updated = Column(Boolean)
    file_name = Column(String)
    file_extension = Column(String)
    file_modification_date = Column(DateTime)
    file_size = Column(BigInteger)

    def __init__(self):
        self.imdb_id = None
        self.title = None
        self.type = None
        self.year = None
        self.tagline = None
        self.plot_outline = None
        self.runtime = None
        self.poster_url = None
        self.cover_url = None
        self.release_date = None
        self.certification = None
        self.trailer_img_url = None
        self.directors = None
        self.creators = None
        self.cast_summary = None
        self.credits = None
        self.writers = None
        self.trailers = None

        self.view_count = 0
        self.user_updated = False
        self.file_name = None
        self.file_extension = None
        self.file_modification_date = datetime(1970, 1, 1)
        self.file_size = 0


