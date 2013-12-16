import os

from distutils.command.install import install
from distutils.dist import Distribution


def get_data_dst():
    """
    Since "pip install ." and "python setup.py install" have different effects
    due to the `--single-version-externally-managed` flag which is added by
    pip, I need to do this magic to always install the data files in the
    expected location.
    """
    i = install(Distribution())
    i.initialize_options()
    i.finalize_options()
    return i.install_purelib + os.path.sep