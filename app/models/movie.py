from vendor.imdbpie.imdbpie import imdbpie
from datetime import datetime


class Movie(imdbpie.Movie):
    """Model of a movie."""

    def __init__(self, *args, **kwargs):
        super(imdbpie.Movie, self).__init__(*args, **kwargs)
        self.view_count = 0
        self.file_name = 'unknown'
        self.file_extension = 'unknown'
        self.file_modification_date = datetime(1970, 1, 1)
        self.file_size = 0


