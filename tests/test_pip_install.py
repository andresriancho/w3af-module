import unittest

from tests.base import BaseInstallMixin


class TestPIPInstallRemote(BaseInstallMixin, unittest.TestCase):

    INSTALL_CMD = 'pip install git+https://github.com/andresriancho/w3af-module.git'


class TestPIPInstallLocal(BaseInstallMixin, unittest.TestCase):

    INSTALL_CMD = 'pip install .'
