import unittest

from mod_utils.pip import get_pip_git_requirements, get_pip_requirements


class TestPip(unittest.TestCase):
    def test_get_pip_git_requirements(self):
        pips = get_pip_git_requirements()
        
        self.assertIn('https://github.com/ramen/phply.git#egg=phply', pips)
    
    def test_get_pip_requirements(self):
        pips = get_pip_requirements()

        # All pip requirements are specific
        for pip_req in pips:
            self.assertIn('==', pip_req)

        # And at least these are there
        for expected in ('clamd', 'esmre', 'chardet', 'futures'):
            for pip_req in pips:
                if pip_req.startswith(expected):
                    break
            else:
                self.assertTrue(False, '%s not found' % expected)
