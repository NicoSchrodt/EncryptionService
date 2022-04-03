from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

from Service.ResourcePath import resource_path


class CharsetWindow(QMainWindow):
    def __init__(self, MainWindow):
        super(CharsetWindow, self).__init__()
        self.init_ui("GUI\\CharsetWindow.ui")

        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.MSWindowsFixedSizeDialogHint)

    def init_ui(self, ui_name):
        full_path = resource_path(ui_name)
        loadUi(full_path, self)
