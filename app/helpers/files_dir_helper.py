import os


def check_dir_presence(dir_list):
    """
    Checks if given folders in `dir_list` exist. Returns OK if they all do or
    the first folder that does not exist otherwise.
    """

    for dir_path in dir_list:
        if not os.path.isdir(dir_path):
            return dir_path

    return 'OK'
