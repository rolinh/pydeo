import unittest
from webtest import TestApp

import test_helper


class MoviesAPIControllerTests(unittest.TestCase):

    def test_movies(self):
        app = TestApp(test_helper.get_app())
        assert app.get('/api/movies').status == '200 OK'

    def test_movies_title(self):
        app = TestApp(test_helper.get_app())
        assert app.get('/api/movies/title').status == '200 OK'

    def test_movies_id(self):
        app = TestApp(test_helper.get_app())
        assert app.get('/api/movies/id/1').status == '200 OK'
        assert app.get('/api/movies/id/42').status == '200 OK'

    # TODO find a way to test it
    # def test_movies_reload(self):
    #     app = TestApp(test_helper.get_app())
    #     assert app.get('/api/movies/reload').status == '200 OK'
