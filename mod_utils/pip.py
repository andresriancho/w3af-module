from w3af.core.controllers.dependency_check.platforms.current_platform import PIP_PACKAGES


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

    return [pkg_url.replace('git+git://', 'https://') for pkg_url in git_packages]