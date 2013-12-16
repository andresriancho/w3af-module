import os

from mod_utils.get_data_dst import get_data_dst

EXCLUDE_EXTENSIONS = ('.py', '.pyc')
PROFILE_ROOT_SRC = 'w3af-repo/profiles/'
DATA_ROOT_DST = get_data_dst()
PROFILE_ROOT_DST = os.path.join(DATA_ROOT_DST, 'w3af/profiles/')


def gen_data_files(_dir):
    result = []
    result.extend(gen_profile_files())
    result.extend(gen_generic_data_files(_dir))
    print result
    return result


def gen_profile_files():
    path_join = lambda f: PROFILE_ROOT_SRC + "/" + f

    profile_data = [(PROFILE_ROOT_DST,
                     map(path_join, os.listdir(PROFILE_ROOT_SRC)))]
    return profile_data


def gen_generic_data_files(_dir):
    results = []

    path_join = lambda f: root + "/" + f

    def file_filter(fname):
        for exclude_ext in EXCLUDE_EXTENSIONS:
            if fname.endswith(exclude_ext):
                return False

        return True

    for root, dirs, files in os.walk(_dir):
        filtered_files = filter(file_filter, files)
        if filtered_files:
            results.append((DATA_ROOT_DST + '/' + root,
                            map(path_join, filtered_files)))

    return results