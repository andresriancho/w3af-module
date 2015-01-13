import unittest
import subprocess

from tests.base import BaseInstallMixin


REMOTE_ERROR_MSG = '''In some rare cases when w3af changes the dependencies, or
the dependency_check function changes it's implementation the remote installation
test will fail. This is because of the outdated w3af-module contents which are
in "pip install git+https://github.com/andresriancho/w3af-module.git", which
might be different from the ones available locally "pip install ."

To fix this issue you'll have to manually update the w3af-repo directory in the
w3af-module repository.

    git checkout w3af-develop
    git pull -v

    git checkout develop
    git rm -r -q w3af-repo
    git read-tree --prefix=w3af-repo/ -u w3af-develop

    git merge --squash -s subtree --no-commit w3af-develop
    git commit w3af-repo/ -m 'Merging latest w3af(develop) into w3af-module(develop)'; true
    git push --set-upstream origin develop
'''


class TestPIPInstallRemote(BaseInstallMixin, unittest.TestCase):

    branch = subprocess.check_output('git rev-parse --abbrev-ref HEAD', shell=True).strip()
    INSTALL_CMD = 'pip install git+https://github.com/andresriancho/w3af-module.git@%s' % branch

    ERROR_MSG = REMOTE_ERROR_MSG


class TestPIPInstallLocal(BaseInstallMixin, unittest.TestCase):

    INSTALL_CMD = 'pip install .'


