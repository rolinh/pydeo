import unittest
from webtest import TestApp

import test_helper


class SettingsControllerTests(unittest.TestCase):

    def test_settings(self):
        app = TestApp(test_helper.get_app())
        assert app.get('/settings').status == '200 OK'
