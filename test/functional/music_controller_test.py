import unittest
from webtest import TestApp

import test_helper

class MusicControllerTests(unittest.TestCase):

    def test_music(self):
        app = TestApp(test_helper.get_app())
        assert app.get('/music').status == '200 OK'

