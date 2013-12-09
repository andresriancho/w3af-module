import unittest

from mod_utils.gen_data_files import gen_data_files


class TestGenDataFiles(unittest.TestCase):
    def test_gen_data_files_with_utils(self):
        result = gen_data_files('mod_utils')
        
        directories = [d for (d, _) in result]
        
        self.assertIn('mod_utils', directories)
        self.assertIn('mod_utils/tests', directories)
        
        for directory, file_list in result:
            if directory == 'utils/tests':
                
                self.assertIn('utils/tests/test_pip.py', file_list)
                self.assertIn('utils/tests/test_gen_data_files.py', file_list)
                
                # Make sure that all files are there, not only py
                self.assertIn('utils/tests/data_test.bin', file_list)