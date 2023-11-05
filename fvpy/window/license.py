import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QCheckBox,
    QDialog,
    QHBoxLayout,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QTextEdit,
    QVBoxLayout,
)
from fvpy.utils import base_dir_path


class LicenseWindow(QDialog):

    LICENSE_CLOSE = pyqtSignal(bool)

    def __init__(self, main_window, parent=None):
        super().__init__(parent)

        self.can_close = False
        self.message = None

        self.main_window = main_window
        self.setWindowTitle("License")
        self.resize(800, 600)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.verticalScrollBar().valueChanged.connect(
            self.scrollbar_value_changed_slot
        )
        license_path = base_dir_path() + "/LICENSE.rst"
        self.text_edit.setText(open(license_path, "r").read())

        self.check_button = QCheckBox(
            "I have read and agree to the terms of the license."
        )
        self.check_button.setChecked(False)
        self.enable_check_button = False
        self.check_button.setEnabled(self.enable_check_button)
        self.check_button.stateChanged.connect(self.check_button_slot)

        self.continue_button = QPushButton("Continue")
        self.continue_button.setDefault(True)
        self.continue_button.setEnabled(False)
        self.continue_button.clicked.connect(self.continue_slot)
        self.continue_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        self.close_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.text_edit)
        self.v_layout.addWidget(self.check_button)
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.close_button)
        self.h_layout.addWidget(self.continue_button)
        self.h_layout.setAlignment(Qt.AlignRight)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def closeEvent(self, event):
        if not self.can_close:
            event.ignore()
            return self.close_error()
        self.LICENSE_CLOSE.emit(True)
        event.accept()

    def scrollbar_value_changed_slot(self, value):
        if value == self.text_edit.verticalScrollBar().maximum():
            self.check_button.setEnabled(True)
            self.enable_check_button = True
        elif self.enable_check_button:
            self.check_button.setEnabled(True)
        else:
            self.check_button.setEnabled(False)

    def check_button_slot(self, state):
        self.check_button.setCheckState(state)
        self.update_continue_button()

    def update_continue_button(self):
        if self.check_button.isChecked():
            self.continue_button.setEnabled(True)
        else:
            self.continue_button.setEnabled(False)

    def continue_slot(self):
        self.can_close = True
        self.close()

    def close_error(self):

        self.message = QMessageBox()
        self.message.setWindowTitle("Close Error")
        self.message.setText("You must agree to the terms of the license to continue.")
        self.message.setIcon(QMessageBox.Warning)
        self.message.addButton("OK", QMessageBox.AcceptRole)
        self.message.addButton("Quit", QMessageBox.RejectRole)
        self.message.buttonClicked.connect(self.message_box_button_slot)
        self.message.exec_()

    def message_box_button_slot(self, button):
        if button.text() == "Quit":
            self.continue_slot()
            self.main_window.close()
            sys.exit()
        elif button.text() == "OK":
            self.message.close()
