import unittest

import test_helper
assert test_helper  # silence pyflakes

from pydeo.app.helpers import application_helper as ah


class ApplicationHelperTests(unittest.TestCase):

    def test_bytes2human(self):
        assert ah.bytes2human(-1) == '-1B'
        assert ah.bytes2human(0) == '0B'
        assert ah.bytes2human(1) == '1B'
        assert ah.bytes2human(10**3) == '1000B'
        assert ah.bytes2human(10**4) == '9K'
        assert ah.bytes2human(10**6) == '976K'
        assert ah.bytes2human(10**9) == '953M'
        assert ah.bytes2human(10**12) == '931G'
        assert ah.bytes2human(10**15) == '909T'

    def test_is_video(self):
        dir = 'data/movies/'

        assert not ah.is_video('foo')
        assert not ah.is_video('/tmp')
        assert not ah.is_video(dir + 'foo.txt')
        assert ah.is_video(dir + 'The Dark Knight.mkv')
        assert ah.is_video(dir + 'movie_that_does_not_exist.avi')
