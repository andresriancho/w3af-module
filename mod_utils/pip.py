from w3af.core.controllers.dependency_check.platforms.current_platform import PIP_PACKAGES


def get_pip_requirements():
    '''
    :return: A list with the names of the pip packages used in w3af (both
             the console and GUI versions).
    '''
    return ['%s==%s' % (p.package_name, p.package_version) for p in PIP_PACKAGES]


def get_pip_git_requirements():
    '''
    :return: The requirements that should be installed from git
    '''
    result = []
    git_packages = [p for p in PIP_PACKAGES if p.is_git]

    for package in git_packages:
        for to_replace in ('git+git://', 'git+https://'):
            package.git_src = package.git_src.replace(to_replace, 'https://')

    for package in git_packages:
        egg_link = '%s-%s' % (package.tgz_src, package.package_version)
        result.append(egg_link)

    return result