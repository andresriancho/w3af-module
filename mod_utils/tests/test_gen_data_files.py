import unittest

from mod_utils.gen_data_files import gen_data_files
from mod_utils.get_data_dst import get_data_dst


class TestGenDataFiles(unittest.TestCase):
    def test_gen_data_files_with_utils(self):
        result = gen_data_files('mod_utils')
        
        directories = [d for (d, _) in result]
        
        self.assertIn('%s/mod_utils/tests' % get_data_dst(), directories)
        
        for directory, file_list in result:
            if directory == '%s/mod_utils/tests' % get_data_dst():

                # data files should not contain python files
                self.assertNotIn('mod_utils/tests/test_pip.py', file_list)

                # Make sure that non py files are there
                self.assertIn('mod_utils/tests/data_test.bin', file_list)
                break
        else:
            self.assertTrue(False, 'Nothing matched')