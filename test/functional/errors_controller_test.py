import unittest
from webtest import TestApp

import test_helper

class ErrorsControllerTests(unittest.TestCase):

    def test_error_404(self):
        app = TestApp(test_helper.get_app())
        assert app.get('/error/404').status == '200 OK'

    def test_error_500(self):
        app = TestApp(test_helper.get_app())
        assert app.get('/error/500').status == '200 OK'

