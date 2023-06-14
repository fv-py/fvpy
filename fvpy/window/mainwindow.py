from PyQt5.QtWidgets import QMainWindow

__all__ = ["MainWindow"]


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
