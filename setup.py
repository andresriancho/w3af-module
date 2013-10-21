#!/usr/bin/env python

from setuptools import setup, find_packages

from utils.get_version import get_version
from utils.gen_data_files import gen_data_files
from utils.pip import get_pip_git_requirements, get_pip_requirements


setup(
      name='w3af',

      version=get_version(),
      license = 'GNU General Public License v2 (GPLv2)',
      platforms='Linux',
      
      description=('w3af is an open source web application security scanner.'),
      long_description=file('README.rst').read(),
      
      author='Andres Riancho',
      author_email='andres.riancho@gmail.com',
      url='https://github.com/andresriancho/w3af/',
      
      packages=find_packages(where='.', exclude=['tests', 'test_']),

      # This will install all the files which live in the w3af directory inside
      # site-packages. It's not pretty, but it works.       
      data_files = gen_data_files('w3af'),
      
      # This allows w3af plugins to read the data_files which we deploy with
      # data_files.
      zip_safe = False,
      
      # Run the module tests using nose
      test_suite = 'nose.collector',
      
      # Require at least the easiest PIP requirements from w3af
      install_requires = get_pip_requirements(),
      dependency_links = get_pip_git_requirements(),
      
      # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers = [
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
