from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from datetime import datetime

from lib.models import base_initializer as b

class Movie(b.BaseInitializer.get_base()):
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
        self.imdb_id = ''
        self.title = ''
        self.type = ''
        self.year = 0
        self.tagline = ''
        self.plot_outline = ''
        self.runtime = ''
        self.poster_url = ''
        self.cover_url = ''
        self.release_date = ''
        self.certification = ''
        self.trailer_img_url = ''
        self.directors = ''
        self.creators = ''
        self.cast_summary = ''
        self.credits = ''
        self.writers = ''
        self.trailers = ''

        self.view_count = 0
        self.user_updated = False
        self.file_name = ''
        self.file_extension = ''
        self.file_modification_date = datetime(1970, 1, 1)
        self.file_size = 0

    def __repr__(self):
        return ('<Movie:'
                'imdb_id=%s,'
                'title=%s,'
                'type=%s,'
                'year=%s,'
                'tagline=%s,'
                'plot_outline=%s,'
                'runtime=%s,'
                'poster_url=%s,'
                'cover_url=%s,'
                'release_date=%s,'
                'certification=%s,'
                'trailer_img_url=%s,'
                'directors=%s,'
                'creators=%s,'
                'cast_summary=%s,'
                'credits=%s,'
                'writers=%s,'
                'trailers=%s,'
                'view_count=%s,'
                'user_updated=%s,'
                'file_name=%s,'
                'file_extension=%s,'
                'file_modification_date=%s,'
                'file_size=%s>') % (self.imdb_id,
                                    self.title,
                                    self.type,
                                    self.year,
                                    self.tagline,
                                    self.plot_outline,
                                    self.runtime,
                                    self.poster_url,
                                    self.cover_url,
                                    self.release_date,
                                    self.certification,
                                    self.trailer_img_url,
                                    self.directors,
                                    self.creators,
                                    self.cast_summary,
                                    self.credits,
                                    self.writers,
                                    self.trailers,
                                    self.view_count,
                                    self.user_updated,
                                    self.file_name,
                                    self.file_extension,
                                    self.file_modification_date,
                                    self.file_size)

    def __str__(self):
        return ('Movie attributes:\n'
                'imdb_id: %s\n'
                'title: %s\n'
                'type: %s\n'
                'year: %s\n'
                'tagline: %s\n'
                'plot_outline: %s\n'
                'runtime: %s\n'
                'poster_url: %s\n'
                'cover_url: %s\n'
                'release_date: %s\n'
                'certification: %s\n'
                'trailer_img_url: %s\n'
                'directors: %s\n'
                'creators: %s\n'
                'cast_summary: %s\n'
                'credits: %s\n'
                'writers: %s\n'
                'trailers: %s\n'
                'view_count: %s\n'
                'user_updated: %s\n'
                'file_name: %s\n'
                'file_extension: %s\n'
                'file_modification_date: %s\n'
                'file_size: %s') % (self.imdb_id,
                                    self.title,
                                    self.type,
                                    self.year,
                                    self.tagline,
                                    self.plot_outline,
                                    self.runtime,
                                    self.poster_url,
                                    self.cover_url,
                                    self.release_date,
                                    self.certification,
                                    self.trailer_img_url,
                                    self.directors,
                                    self.creators,
                                    self.cast_summary,
                                    self.credits,
                                    self.writers,
                                    self.trailers,
                                    self.view_count,
                                    self.user_updated,
                                    self.file_name,
                                    self.file_extension,
                                    self.file_modification_date,
                                    self.file_size)

