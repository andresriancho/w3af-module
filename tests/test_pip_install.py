import unittest

from tests.base import BaseInstallMixin


class TestPIPInstall(BaseInstallMixin, unittest.TestCase):

    UNINSTALL_CMD = 'pip uninstall -y w3af'
    INSTALL_CMD = 'pip install git+https://github.com/andresriancho/w3af-module.git'
