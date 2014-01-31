from datetime import datetime
from logging import warning
from mimetypes import guess_type
from os import listdir
from os import path
from os import stat
from requests import ConnectionError

from guessit import guess_movie_info
import imdbpie

from app.helpers.application_helper import to_list
from app.models.movie import Movie
from config.settings import movies_dir


def update_movies_db(db, dir='files/' + movies_dir + '/'):
    """
    Find all movie files in the movie folder and add them to the database.
    """

    movies_in_db = [m.file_name for m in db.query(Movie).all()]

    imdb = imdbpie.Imdb()
    for f in listdir(dir):
        file_path = dir + f
        if not is_movie(file_path):
            continue
        if f in movies_in_db:
            continue

        filename, ext = path.splitext(f)
        f_info = stat(dir + f)
        guess = guess_movie_info(file_path)

        movie = Movie()
        movie.title = guess['title'] if guess['title'] else filename
        try:
            m = imdb.find_by_title(movie.title)

            if m and (are_movie_titles_close(movie.title, m[0]['title']) or
                      are_movie_titles_close(m[0]['title'], movie.title)):
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
                                            in m.trailers.items()])
        except ConnectionError:
            warning('Unable to fetch movie information due to network'
                    ' connection problems: \"%s\"', movie.title)

        movie.file_path = file_path
        movie.file_name = f
        movie.file_extension = ext[1:]
        movie.file_modification_date = datetime.fromtimestamp(f_info.st_mtime)
        movie.file_size = f_info.st_size
        movie.mime_type = guess_type(file_path)[0]

        db.add(movie)


def is_movie(file):
    """
    Try to determine if the given file is a movie or not.
    Return true if it is one, false otherwise.
    """
    if not path.isfile(file):
        return False
    try:
        filetype = guess_type(file)[0]
        if filetype[:5] == 'video':
            return True
        else:
            return False
    except:
        warning('Unable to detect file type: \"%s\"', file)
        return False


def are_movie_titles_close(title_a, title_b):
    """
    Compare titles. If all words from title_a are also in title_b, True is
    returned. Otherwise, False is returned.
    """
    title_a_words = title_a.lower().split(' ')
    title_b_words = title_b.lower().split(' ')
    for w in title_a_words:
        if not w in title_b_words:
            return False
    return True
