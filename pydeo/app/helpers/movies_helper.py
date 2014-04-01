from datetime import datetime
from logging import (
    warning,
    info
)
from mimetypes import guess_type
from os import (
    path,
    stat
)
from requests import ConnectionError

from guessit import guess_movie_info
import imdbpie

from pydeo.app.helpers.application_helper import (
    to_list,
    list_videos
)
from pydeo.app.models.movie import Movie
from pydeo.config.settings import movies_dir


def update_movies_db(db, dir='files/' + movies_dir + '/'):
    """
    Find all movie files in the movie folder and add them to the database.
    """

    movies_in_db = [m.file_path for m in db.query(Movie).all()]

    for f in list_videos(dir):
        if f in movies_in_db:
            continue

        info("Currently scanning: " + f)
        filename, ext = path.splitext(f)
        f_info = stat(f)
        guess = guess_movie_info(f)

        movie = Movie()
        try:
            movie.title = guess['title']
        except:
            movie.title = filename

        movie.file_path = f
        movie.file_name = f
        movie.file_extension = ext[1:]
        movie.file_modification_date = datetime.fromtimestamp(f_info.st_mtime)
        movie.file_size = f_info.st_size
        movie.mime_type = guess_type(f)[0]

        db.add(movie)
    db.commit()


def fetch_movies_information(db):
    """
    Fetch informations about movies such as the movie cover, list of actors and
    so on.
    """

    imdb = imdbpie.Imdb()
    for movie in db.query(Movie).all():
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
    db.commit()


def are_movie_titles_close(title_a, title_b):
    """
    Compare titles. If all words from title_a are also in title_b, True is
    returned. Otherwise, False is returned.
    """
    title_a_words = title_a.lower().split(' ')
    title_b_words = title_b.lower().split(' ')
    for w in title_a_words:
        if w not in title_b_words:
            return False
    return True
