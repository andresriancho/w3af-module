#!/usr/bin/env python

import os
from setuptools import setup, find_packages

from w3af.core.controllers.dependency_check.platforms.current_platform import PIP_PACKAGES


def get_version():
    '''
    :return: A string with the version, for example, '1.5'.
    '''
    version_file = os.path.join('w3af', 'core', 'data',
                                'constants', 'version.txt')
    version = file(version_file).read().strip()
    return version

def gen_data_files(*dirs):
    results = []

    for src_dir in dirs:
        for root, dirs, files in os.walk(src_dir):
            results.append((root, map(lambda f:root + "/" + f, files)))
            
    return results

def get_pip_requirements():
    '''
    :return: A list with the names of the pip packages used in w3af (both
             the console and GUI versions).
    '''
    return [p.package_name for p in PIP_PACKAGES\
            if 'git://' not in p.package_name]

def get_pip_git_requirements():
    '''
    :return: The requirements that should be installed from git
    '''
    git_packages =  [p.package_name for p in PIP_PACKAGES \
                     if 'git://' in p.package_name]

    return [pkg_url.replace('git+git://', 'http://') for pkg_url in git_packages]

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
      zip_safe=False,
      
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
