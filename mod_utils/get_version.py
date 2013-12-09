import os


def get_version():
    '''
    :return: A string with the version, for example, '1.5'.
    '''
    version_file = os.path.join('w3af', 'core', 'data',
                                'constants', 'version.txt')
    version = file(version_file).read().strip()
    return version
