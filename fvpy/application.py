import yaml
from PyQt5.QtWidgets import QApplication
from fvpy.utils import package_dir_path
from fvpy.window import MainWindow


def run(args):

    app = Application(args)
    app.exec_()


class Application(QApplication):
    def __init__(self, args):

        super().__init__(args)

        self.new_window = MainWindow()
        self.new_window.show()

        self.license_window = None
        self.check_first()

    def check_first(self):
        """check if it is the first time the program is run.

        If it is the first time, show the license window.
        """
        path = package_dir_path() + "/_config.yaml"
        config = yaml.load(open(path, "r"), Loader=yaml.FullLoader)
        if config["first"]:
            from fvpy.window.license import LicenseWindow

            self.new_window.setEnabled(False)
            self.license_window = LicenseWindow(main_window=self.new_window)
            self.license_window.exec_()
            self.new_window.setEnabled(True)
            # config["first"] = False
            # yaml.dump(config, open(path, "w"))
