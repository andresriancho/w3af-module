import os
import sys

from distutils.command.install import install
from distutils.dist import Distribution
from pkg_resources import get_build_platform
from pkg_resources import Distribution as PkgResDistribution
from sysconfig import get_python_version

from mod_utils.get_version import get_version


def get_data_dst():
    """
    Since "pip install ." and "python setup.py install" have different effects
    due to the `--single-version-externally-managed` flag which is added by
    pip, I need to do this magic to always install the data files in the
    expected location.
    """
    # Compute filename of the output egg
    basename = PkgResDistribution(
        None, None, 'w3af', get_version(),
        get_python_version(),
        False and get_build_platform()
    ).egg_name()
    egg_name = basename + '.egg'

    i = install(Distribution())
    i.initialize_options()
    i.finalize_options()

    if called_from_pip():
        return i.install_purelib + os.path.sep
    else:
        return i.install_purelib + os.path.sep #+ egg_name + os.path.sep


def called_from_pip():
    if '--single-version-externally-managed' in sys.argv:
        return True

    return False