import unittest

import test_helper
from app.helpers import movies_helper
from app.models import movie
from lib.controllers import db_connector as db


class MoviesHelperTests(unittest.TestCase):

    def test_update_movies_db(self):
        test_helper.init()
        sess = db.DbConnector.session
        dir = 'data/movies/'
        movies_helper.update_movies_db(dir)

        assert sess.query(movie.Movie).count() == 2

        l = sess.query(movie.Movie).order_by(movie.Movie.title).all()

        # some attributes, eg votes and rating, cannot be tested as they are
        # subject to change over time
        assert l[0].imdb_id == 'tt0468569'
        assert l[0].title == 'The Dark Knight'
        assert l[0].type == 'feature'
        assert l[0].genres == 'Action, Crime, Drama, Thriller'
        assert l[0].directors == 'Christopher Nolan'
        assert l[0].cast == ('Christian Bale, Heath Ledger, Aaron Eckhart,'
                             ' Michael Caine')
        assert l[0].writers == 'Jonathan Nolan, Christopher Nolan'
        assert l[0].year == 2008
        assert l[0].release_date == '2008-07-18'
        assert l[0].certification == 'PG-13'
        assert l[0].runtime == 152
        assert l[0].tagline == 'Why So Serious?'
        assert l[0].view_count == 0
        assert l[0].mime_type == 'video/x-matroska'
        assert l[0].file_path == dir + 'The Dark Knight.mkv'
        assert l[0].file_name == 'The Dark Knight.mkv'
        assert l[0].file_extension == 'mkv'
        assert l[0].file_size == 4434

        assert l[1].title == 'movie that does not exist'
        assert l[1].view_count == 0
        assert l[1].user_updated is False
        assert l[1].mime_type == 'video/x-msvideo'
        assert l[1].file_path == dir + 'movie_that_does_not_exist.avi'
        assert l[1].file_name == 'movie_that_does_not_exist.avi'
        assert l[1].file_extension == 'avi'
        assert l[1].file_size == 16818

    def test_is_movie(self):
        test_helper.init()
        dir = 'data/movies/'

        assert not movies_helper.is_movie('foo')
        assert not movies_helper.is_movie('/tmp')
        assert not movies_helper.is_movie(dir + 'foo.txt')
        assert movies_helper.is_movie(dir + 'The Dark Knight.mkv')
        assert movies_helper.is_movie(dir + 'movie_that_does_not_exist.avi')

    test_update_movies_db.slow = 1
