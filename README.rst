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

    git clone --recursive git@github.com:andresriancho/w3af-module.git
    python setup.py install

Please note that this repository uses submodules to include the main w3af
repository, so the ``--recursive`` flag in the ``git clone`` command is required.

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


