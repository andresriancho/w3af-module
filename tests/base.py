import os
import sys
import shlex
import shutil
import subprocess


def get_module_dir():
    # Get the location for the w3af module
    FILE_CMD = "%s -c 'import w3af; print w3af.__file__'" % sys.executable
    module_file = subprocess.check_output(shlex.split(FILE_CMD), cwd='tests')
    module_file = module_file.strip()

    # Append it with the location for the version.txt file
    module_dir = module_file.replace('__init__.pyc', '')
    return module_dir


class BaseInstallMixin(object):

    # To be defined in child classes
    INSTALL_CMD = None
    UNINSTALL_CMDS = ["find venv/ -name 'w3af*' | xargs rm -rf",
                      "rm -rf ~/.w3af/",
                      "rm -rf build/ dist/ w3af.egg-info/"]
    NULL = open(os.devnull, 'w')

    @classmethod
    def setUpClass(cls):
        subprocess.check_call(shlex.split(cls.INSTALL_CMD),
                              stdout=cls.NULL, stderr=subprocess.STDOUT)

    @classmethod
    def tearDownClass(cls):
        """
        A rather aggressive uninstall strategy
        """
        for uninstall_cmd in cls.UNINSTALL_CMDS:
            subprocess.check_output(uninstall_cmd, shell=True)

    def test_version_txt(self):
        # Append it with the location for the version.txt file
        module_dir = get_module_dir()
        version_txt = os.path.join(module_dir, 'core/data/constants/version.txt')

        # Check that the file was installed
        msg = 'File "%s" does NOT exist' % version_txt
        self.assertTrue(os.path.exists(version_txt), msg)

    def test_get_version_call(self):
        VERSION_CMD = "%s -c 'from w3af.core.controllers.misc.get_w3af_version"\
                      " import get_w3af_version; print get_w3af_version()'"
        try:
            subprocess.check_call(shlex.split(VERSION_CMD % sys.executable),
                                  stdout=self.NULL, stderr=subprocess.STDOUT,
                                  cwd='tests')
        except subprocess.CalledProcessError, cpe:
            self.assertEqual(False, True, cpe.output)

    def test_import_module(self):
        IMPORT_CMD = "%s -c 'import w3af'" % sys.executable
        subprocess.check_call(shlex.split(IMPORT_CMD),
                              stdout=self.NULL, stderr=subprocess.STDOUT,
                              cwd='tests')

    def test_import_core(self):
        IMPORT_CMD = "%s -c 'from w3af.core.controllers.w3afCore import w3afCore;"\
                     "c = w3afCore()'" % sys.executable
        subprocess.check_call(shlex.split(IMPORT_CMD),
                              stdout=self.NULL, stderr=subprocess.STDOUT,
                              cwd='tests')