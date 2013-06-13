Introduction
============

Tools to install w3af as a Python module.

The setup.py file is only useful if you're trying to create some type of
wrapper around w3af and use it as a module. The file is not included into the
main w3af distribution because regular users don't need it.

Usage
=====

To use this file just download it, copy to the w3af root directory and run
`python setup.py install` , after some seconds you should be able to move
to any directory and from a python interpreter run `import w3af`.

Dependencies
============

It is important to note that this script does NOT install any pip or operating
system packages required by w3af. You still need to go through the regular
installation process to get a working w3af install.


