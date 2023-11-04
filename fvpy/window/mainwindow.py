from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QMainWindow
from fvpy.menu import MenuBar
from fvpy.signals import OpenFileSignal

__all__ = ["MainWindow"]


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("FvPy")
        self.resize(800, 600)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self.open_file_signal = OpenFileSignal(instance=self)

        self.menu_bar = MenuBar(main_window=self)
        self.setMenuBar(self.menu_bar)
        # If on macOS, the following line is needed to show the fvpy menu of the menu bar.
        # Otherwise, the fvpy menu is hidden under the macOS application menu named python.
        # self.menu_bar.setNativeMenuBar(False)
