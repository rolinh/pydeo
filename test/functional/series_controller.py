import unittest
from webtest import TestApp

import test_helper

class SeriesControllerTests(unittest.TestCase):

    def test_series(self):
        app = TestApp(test_helper.get_app())
        assert app.get('/series').status == '200 OK'

