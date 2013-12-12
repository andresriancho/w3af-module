import sys
import unittest

from tests.base import BaseInstallMixin


class TestSetupInstall(BaseInstallMixin, unittest.TestCase):

    UNINSTALL_CMD = 'pip uninstall -y w3af'
    INSTALL_CMD = '%s setup.py install' % sys.executable
