import unittest

from mod_utils.pip import get_pip_git_requirements, get_pip_requirements


class TestPip(unittest.TestCase):
    def test_get_pip_git_requirements(self):
        pips = get_pip_git_requirements()
        
        self.assertIn('http://github.com/ramen/phply.git#egg=phply', pips)
    
    def test_get_pip_requirements(self):
        pips = get_pip_requirements()
        
        self.assertIn('clamd', pips)
        self.assertIn('esmre', pips)
        self.assertIn('chardet', pips)
        self.assertIn('futures', pips)
    