import unittest

from mod_utils.gen_data_files import gen_data_files


class TestGenDataFiles(unittest.TestCase):
    def test_gen_data_files_with_utils(self):
        result = gen_data_files('mod_utils')
        
        directories = [d for (d, _) in result]
        
        self.assertIn('mod_utils/tests', directories)
        
        for directory, file_list in result:
            if directory == 'mod_utils/tests':

                # data files should not contain python files
                self.assertNotIn('mod_utils/tests/test_pip.py', file_list)

                # Make sure that non py files are there
                self.assertIn('mod_utils/tests/data_test.bin', file_list)