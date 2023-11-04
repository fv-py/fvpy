import os
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from fvpy.backend import ReadFile

__all__ = ["OpenFileSignal"]


class OpenFileSignal:
    """Signal for opening a file. This will usually be connected to a menu action (Open menu).

    Parameters
    ----------
    path : str, optional
        The path of the file to be opened. Default is None.
    instance : instance of `~PyQt5.QtWidgets.QWidget`, optional
        The instance of the widget that calls the signal. Default is None.
    """

    HOME_PATH = os.path.expanduser("~")

    def __init__(self, path=None, instance=None):
        self.message = None
        self._path = path or self.HOME_PATH
        self.instance = instance

    def __call__(self):
        """Open a file.

        If the file is readable, open a message box.
        """
        # TODO: Fix the bug that the file dialog is shifted to the right
        #  when reopening it true the message box retry slot.
        file_path, _filter = QFileDialog.getOpenFileName(
            self.instance, "Open File", self.path
        )
        if not file_path:
            return
        self.filename = os.path.basename(file_path)
        read_file = ReadFile(file_path)
        self.path = file_path
        if read_file.check_readable() is None:
            self.open_error()

    def open_error(self):
        self.message = QMessageBox()
        self.message.setWindowTitle("Open Error")
        self.message.setText("The file you are trying to open is not supported.")
        self.message.setIcon(QMessageBox.Warning)
        self.message.setStandardButtons(QMessageBox.Cancel | QMessageBox.Retry)
        self.message.setDefaultButton(QMessageBox.Retry)
        self.message.buttonClicked.connect(self.message_box_button_slot)
        self.message.exec_()

    def message_box_button_slot(self, button):
        if button.text() == "Retry":
            self.message.close()
            return self.__call__()
        else:
            pass

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        if os.path.isfile(path):
            self._path = os.path.dirname(path)
        else:
            self._path = path
