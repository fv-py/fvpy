from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QAction, QMenu, QMenuBar
from fvpy.utils import create_menu_action

__all__ = ["MenuBar", "FileMenu", "ViewMenu", "FvPyMenu"]


class MenuBar(QMenuBar):
    """Menu bar for the main window."""

    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)

        self.main_window = main_window

        self.fvpy_menu = FvPyMenu(main_window=self.main_window)
        self.addMenu(self.fvpy_menu)

        self.file_menu = FileMenu(main_window=self.main_window)
        self.addMenu(self.file_menu)

        self.edit_menu = self.addMenu("Edit")

        self.view_menu = ViewMenu(main_window=self.main_window)
        self.addMenu(self.view_menu)

        self.help_menu = self.addMenu("Help")


class FvPyMenu(QMenu):
    """FvPy menu for the main window."""

    def __init__(self, parent=None, main_window=None):
        super().__init__("FvPy", parent)

        self.main_window = main_window

        self.about_action = QAction("About FvPy", self)
        self.addAction(self.about_action)

        self.addSeparator()

        self.setting_action = QAction("Settings", self)
        self.addAction(self.setting_action)


class FileMenu(QMenu):
    """File menu for the main window."""

    def __init__(self, parent=None, main_window=None):
        super().__init__("File", parent)

        self.main_window = main_window

        self.new_action = create_menu_action(self, "New", shortcut=QKeySequence.New)
        self.addAction(self.new_action)

        open_signal = self.main_window.open_file_signal
        self.open_action = create_menu_action(
            self,
            "Open",
            shortcut=QKeySequence.Open,
            slot=open_signal,
            signal="triggered",
        )
        self.addAction(self.open_action)

        self.save_action = create_menu_action(self, "Save", shortcut=QKeySequence.Save)
        self.addAction(self.save_action)

        self.save_as_action = create_menu_action(
            self, "Save As", shortcut=QKeySequence.SaveAs
        )
        self.addAction(self.save_as_action)

        self.exit_action = create_menu_action(self, "Exit", shortcut=QKeySequence.Quit)
        self.addAction(self.exit_action)


class ViewMenu(QMenu):
    """View menu for the main window."""

    def __init__(self, parent=None, main_window=None):
        super().__init__("View", parent)
        self.main_window = main_window

        self.addMenu(self.appearance_menu())

        self.addSeparator()

        self.full_screen_action = create_menu_action(
            self, "Full Screen", shortcut=QKeySequence.FullScreen
        )
        self.addAction(self.full_screen_action)

        self.minimize_action = create_menu_action(self, "Minimize")
        self.addAction(self.minimize_action)

        self.maximize_action = create_menu_action(self, "Maximize")
        self.addAction(self.maximize_action)

        self.restore_action = create_menu_action(
            self, "Restore", shortcut=QKeySequence("Ctrl+Shift+R")
        )
        self.addAction(self.restore_action)

    def appearance_menu(self):
        menu = QMenu("Appearance", self)

        light_mode_action = create_menu_action(self, "Light Mode")
        light_mode_action.triggered.connect(self.light_mode_slot)
        menu.addAction(light_mode_action)

        dark_mode_action = create_menu_action(self, "Dark Mode")
        dark_mode_action.triggered.connect(self.dark_mode_slot)
        menu.addAction(dark_mode_action)

        return menu

    def light_mode_slot(self):
        if self.main_window:
            self.main_window.centralWidget.setText("Light Mode")

    def dark_mode_slot(self):
        if self.main_window:
            self.main_window.centralWidget.setText("Dark Mode")
