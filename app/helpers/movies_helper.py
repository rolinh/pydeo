from datetime import datetime
import logging
from mimetypes import guess_type
from os import listdir
from os import path
from os import stat
from requests import ConnectionError

from app.helpers.application_helper import to_list
from app.models.movie import Movie
from config.settings import movies_dir
from lib.controllers import db_connector as db
import imdbpie


def update_movies_db(dir='files/' + movies_dir + '/'):
    """
    Find all movie files in the movie folder and add them to the database.
    """

    sess = db.DbConnector.session
    movies_in_db = [m.file_name for m in sess.query(Movie).all()]

    imdb = imdbpie.Imdb()
    for f in listdir(dir):
        if not is_movie(dir + f):
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
                movie.genres = ', '.join(to_list(m.genres))
                movie.rating = m.rating
                movie.votes = m.votes
                movie.year = m.year
                movie.tagline = m.tagline
                movie.plot_outline = m.plot_outline
                movie.runtime = m.runtime
                movie.poster_url = m.poster_url
                movie.cover_url = m.cover_url
                movie.release_date = m.release_date
                movie.certification = m.certification
                movie.trailer_img_url = m.trailer_img_url
                movie.directors = ', '.join(p.name for p
                                            in to_list(m.directors_summary))
                movie.creators = ', '.join(p.name for p in to_list(m.creators))
                movie.cast = ', '.join(p.name for p in to_list(m.cast_summary))
                movie.credits = ', '.join(p.name for p in to_list(m.credits))
                movie.writers = ', '.join(p.name for p
                                          in to_list(m.writers_summary))
                movie.trailers = ', '.join(['%s#%s' % (k, v) for (k, v)
                                            in to_list(m.trailers.items())])
            else:
                movie.title = filename
        except ConnectionError:
            logging.warning('Unable to fetch movie information due to network'
                            ' connection problems: \"%s\"', title)

        movie.file_name = f
        movie.file_extension = ext[1:]
        movie.file_modification_date = datetime.fromtimestamp(f_info.st_mtime)
        movie.file_size = f_info.st_size

        sess.add(movie)
    sess.commit()


def is_movie(file):
    """
    Try to determine if the given file is a movie or not.
    Return true if it is one, false otherwise.
    """
    if not path.isfile(file):
        return False
    try:
        filetype = guess_type(file)[0]
        print(filetype)
        if filetype[:5] == 'video':
            return True
        else:
            return False
    except:
        logging.warning('Unable to detect file type: \"%s\"', file)
        return False
