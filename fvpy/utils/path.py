import os

THIS_FILE_PATH = os.path.abspath(__file__)


def file_dir_path(file_path):
    """Return the path of the directory of a file."""
    return os.path.dirname(file_path)


def package_dir_path():
    """Return the path of the base directory of the package."""
    return os.path.dirname(os.path.dirname(THIS_FILE_PATH))


def base_dir_path():
    """Return the path of the base directory of the package."""
    return os.path.dirname(package_dir_path())
