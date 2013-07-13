import unittest

import test_helper

from app.helpers import files_dir

class FilesDirHelperTests(unittest.TestCase):

    def test_check_dir_presence(self):
        assert files_dir.check_dir_presence(['/tmp', '/usr', '/usr/bin']) == 'OK'
        assert files_dir.check_dir_presence(['/foo', '/bar']) != 'OK'
        assert files_dir.check_dir_presence(['/usr/bin', '/bar']) != 'OK'

