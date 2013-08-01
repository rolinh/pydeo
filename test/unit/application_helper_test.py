import unittest

import test_helper

from app.helpers import application_helper as ah


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
