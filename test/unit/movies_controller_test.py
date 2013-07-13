import unittest

import test_helper
from app.controllers import movies

class MoviesControllerTests(unittest.TestCase):

    def test_update_movies_db(self):
        dir = 'data/movies/'
        l = movies.MoviesController().update_movies_db(dir)
        assert l[0].view_count == 0
        assert l[1].view_count == 0
        assert l[0].file_name == 'Sintel.mkv'
        assert l[1].file_name == 'big_buck_bunny_1080p_h264.mov'
        assert l[0].file_extension == 'mkv'
        assert l[1].file_extension == 'mov'
        assert l[0].file_size == 4300800
        assert l[1].file_size == 1379328

    test_update_movies_db.slow = 1
