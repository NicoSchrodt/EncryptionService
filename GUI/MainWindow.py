import os.path
import sys

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.init_ui("GUI\\MainWindow.ui")

        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.MSWindowsFixedSizeDialogHint)

        # Exit Button
        exit_button = self.button_Exit
        exit_button.clicked.connect(self.close)

    def init_ui(self, ui_name):
        base_path = os.path.abspath(".")
        full_path = os.path.join(base_path, ui_name)
        loadUi(full_path, self)
