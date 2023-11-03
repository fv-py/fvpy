from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QMainWindow
from fvpy.menu import MenuBar

__all__ = ["MainWindow"]


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("FvPy")
        self.resize(800, 600)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self.menu_bar = MenuBar(main_window=self)
        self.setMenuBar(self.menu_bar)
