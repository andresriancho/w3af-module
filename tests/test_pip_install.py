import unittest

from tests.base import BaseInstallMixin


class TestPIPInstall(BaseInstallMixin, unittest.TestCase):

    INSTALL_CMD = 'pip install git+https://github.com/andresriancho/w3af-module.git'
