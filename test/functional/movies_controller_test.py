import unittest
from webtest import TestApp

import test_helper

class MoviesControllerTests(unittest.TestCase):

    def test_movies(self):
        app = TestApp(test_helper.get_app())
        assert app.get('/movies').status == '200 OK'

