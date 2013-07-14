import unittest

import test_helper
from app.helpers import movies_helper

class MoviesHelperTests(unittest.TestCase):

    def test_update_movies_db(self):
        dir = 'data/movies/'
        l = movies_helper.update_movies_db(dir)
        assert l[0].title == 'movie_that_does_not_exist'
        assert l[0].view_count == 0
        assert l[0].user_updated == False
        assert l[0].file_name == 'movie_that_does_not_exist.mov'
        assert l[0].file_extension == 'mov'
        assert l[0].file_size == 1379328

        # there is no necessity to test all movie attributes, just some of them
        # is enough
        assert l[1].imdb_id == 'tt0468569'
        assert l[1].title == 'The Dark Knight'
        assert l[1].type == 'feature'
        assert l[1].year == 2008
        assert l[1].tagline == 'Why So Serious?'
        assert l[1].view_count == 0
        assert l[1].file_name == 'The Dark Knight.mkv'
        assert l[1].file_extension == 'mkv'
        assert l[1].file_size == 4300800

    test_update_movies_db.slow = 1
