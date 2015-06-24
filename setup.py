#!/usr/bin/env python
import os

from setuptools import setup, find_packages
from mod_utils.get_version import get_version
from mod_utils.pip import get_pip_git_requirements, get_pip_requirements

SETUPTOOLS_VERSION = '11.3.1'
PROFILES_DIR = 'w3af-repo/profiles/'


setup(
    name='w3af',

    version=get_version(),
    license='GNU General Public License v2 (GPLv2)',
    platforms='Linux',

    description='w3af is an open source web application security scanner.',
    long_description=file('README.rst').read(),

    author='Andres Riancho',
    author_email='andres.riancho@gmail.com',
    url='https://github.com/andresriancho/w3af/',

    packages=find_packages(where='.', exclude=['tests*', 'mod_utils*']),

    # include everything in source control which lives inside one of the
    # packages identified by find_packages, depends on setuptools_git
    include_package_data=True,

    # include the data files, which don't live inside the directory

    data_files=[('profiles',
                [PROFILES_DIR + '/' + f for f in os.listdir(PROFILES_DIR)])],

    # This allows w3af plugins to read the data_files which we deploy with
    # data_files.
    zip_safe=False,

    # Run the module tests using nose
    test_suite='nose.collector',

    # Require at least the easiest PIP requirements from w3af
    setup_requires=['setuptools>=%s' % SETUPTOOLS_VERSION,
                    "setuptools_git>=1.0"],
    install_requires=get_pip_requirements(),
    dependency_links=get_pip_git_requirements(),

    # Install these scripts
    scripts=['w3af-repo/w3af_console',
             'w3af-repo/w3af_gui',
             'w3af-repo/w3af_api'],

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security'
    ],
)
