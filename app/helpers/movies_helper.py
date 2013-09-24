from datetime import datetime
import logging
from os import listdir
from os import path
from os import stat
from requests import ConnectionError

from app.models.movie import Movie
from config.settings import movies_dir
from lib.controllers import db_connector as db
from vendor.imdbpie.imdbpie import imdbpie


def update_movies_db(dir='files/' + movies_dir + '/'):
    """
    Find all movie files in the movie folder and add them to the database.
    """

    sess = db.DbConnector.session
    movies_in_db = [m.file_name for m in sess.query(Movie).all()]

    imdb = imdbpie.Imdb()
    for f in listdir(dir):
        if not path.isfile(dir + f):
            continue
        if f in movies_in_db:
            continue

        filename, ext = path.splitext(f)
        f_info = stat(dir + f)
        # TODO implement this function to generate a clean title from filename
        # title = application_helper.gen_clean_name(filename)
        title = filename

        movie = Movie()
        try:
            m = imdb.find_by_title(title)
            if m:
                m = imdb.find_movie_by_id(m[0]['imdb_id'])
                movie.imdb_id = m.imdb_id
                movie.title = m.title
                movie.type = m.type
                movie.year = m.year
                movie.tagline = m.tagline
                movie.plot_outline = m.plot_outline
                movie.runtime = m.runtime
                movie.poster_url = m.poster_url
                movie.cover_url = m.cover_url
                movie.release_date = m.release_date
                movie.certification = m.certification
                movie.trailer_img_url = m.trailer_img_url
                movie.directors = ', '.join(p.name for p in m.directors_summary)
                movie.creators = ', '.join(p.name for p in m.creators)
                movie.cast_summary = ', '.join(p.name for p in m.cast_summary)
                movie.credits = ', '.join(p.name for p in m.credits)
                movie.writers = ', '.join(p.name for p in m.writers_summary)
                movie.trailers = ', '.join(['%s#%s' % (k, v) for (k, v)
                                            in m.trailers.items()])
            else:
                movie.title = filename
        except ConnectionError:
            # TODO log to a file
            logging.warning('Unable to fetch movie information due to network'
                            ' connection problems: \"%s\"', title)

        movie.file_name = f
        movie.file_extension = ext[1:]
        movie.file_modification_date = datetime.fromtimestamp(f_info.st_mtime)
        movie.file_size = f_info.st_size

        sess.add(movie)
    sess.commit()
