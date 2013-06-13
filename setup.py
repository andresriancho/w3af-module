#!/usr/bin/env python

from setuptools import setup, find_packages
from os.path import join


def get_version():
    '''
    :return: A string with the version, for example, '1.5'.
    '''
    version_file = join('w3af', 'core', 'data', 'constants', 'version.txt')
    version = file(version_file).read().strip()
    return version


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
      
      packages=find_packages(),
      include_package_data=True,
      
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
