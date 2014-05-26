Introduction
============

Tools to install w3af as a Python module.

The setup.py file is only useful if you're trying to create some type of
wrapper around w3af and use it as a module. The file is not included into the
main w3af distribution because regular users don't need it.

Usage
=====

To install w3af as a module you'll have to follow these steps:

::

    git clone git@github.com:andresriancho/w3af-module.git
    sudo python setup.py install

After some seconds you should be able to move to any directory and from a
python interpreter run ``import w3af``.

::

    andres@box:~$ python
    Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
    [GCC 4.6.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import w3af
    >>>


Dependencies
============

It is important to note that this script does NOT install any pip or operating
system packages required by w3af. You still need to go through the regular
installation process to get a working w3af install.


The w3af directory
==================

Advanced users will notice that the ``w3af-repo`` directory is a copy of the
``w3af`` repository that lives in ``git@github.com:andresriancho/w3af.git``. This is
the source which will be used to build the module and was merged into this repository
using `git subtree <https://help.github.com/articles/working-with-subtree-merge>`_.

To update the code that lives in this directory you'll have to run:

::

    cd w3af-repo/
    git pull -s subtree w3af develop # or master if you want the stable release
    git push


Testing the setup.py
====================

Testing the `setup.py` file is easy:

::

    virtualenv venv
    . venv/bin/activate
    rm -rf build/ dist/ w3af.egg-info/
    python setup.py install --dry-run --record record.txt
    # inspect the record.txt file
    
