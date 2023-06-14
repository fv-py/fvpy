from PyQt5.QtWidgets import QApplication
from fvpy.window import MainWindow


def run(args):

    app = Application(args)
    app.exec()


class Application(QApplication):
    def __init__(self, args):

        super().__init__(args)

        self.new_window = MainWindow()
        self.new_window.show()
