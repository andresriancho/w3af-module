import unittest

from utils.get_version import get_version


class TestGetVersion(unittest.TestCase):
    def test_get_version(self):
        version = get_version()
        
        version = float(version)
        self.assertGreater(version, 1.4)
        
        