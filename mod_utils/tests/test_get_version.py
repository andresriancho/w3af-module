import unittest

from mod_utils.get_version import get_version


class TestGetVersion(unittest.TestCase):
    def test_get_version(self):
        version = get_version()
        
        self.assertTrue(version.startswith('1.6') or version.startswith('1.7')
                        or version.startswith('1.8') or version.startswith('1.9'))


