import os
from PyQt5.QtWidgets import QFileDialog

__all__ = ["OpenFileSignal"]


class OpenFileSignal:
    """Signal for opening a file."""

    HOME_PATH = os.path.expanduser("~")

    def __init__(self, path=None, instance=None):
        self._path = path or self.HOME_PATH
        self.instance = instance

    def __call__(self):
        return QFileDialog.getOpenFileName(self.instance, "Open File", self.path)

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        if os.path.isfile(path):
            self._path = os.path.dirname(path)
        else:
            self._path = path
