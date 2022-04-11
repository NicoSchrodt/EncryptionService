from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

from Service.ResourcePath import resource_path
from Service.Text.EligibleCharacters import EligibleCharacters


class CharsetWindow(QMainWindow):
    def __init__(self, MainWindow):
        super(CharsetWindow, self).__init__()
        self.init_ui("GUI\\CharsetWindow.ui")
        self.MainWindow = MainWindow

        self.charset = None
        self.get_charset()
        self.refresh_characters()

        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.MSWindowsFixedSizeDialogHint)

        # Buttons
        self.InsertSet_Button.clicked.connect(self.insert_set)
        self.InsertCharacter_Button.clicked.connect(self.insert_char)

    def init_ui(self, ui_name):
        full_path = resource_path(ui_name)
        loadUi(full_path, self)

    def get_charset(self):
        if isinstance(self.MainWindow.charset, EligibleCharacters):
            self.charset = self.MainWindow.charset
        else:
            self.charset = EligibleCharacters()
            self.charset.insert_predefined_into_character_list(["std"])

    def insert_set(self):
        if self.CharacterSet_Box.currentText() == "Upper Case":
            self.charset.insert_predefined_into_character_list(["std"])
        elif self.CharacterSet_Box.currentText() == "Lower Case":
            self.charset.insert_predefined_into_character_list(["std_low"])
        elif self.CharacterSet_Box.currentText() == "Special Characters":
            self.charset.insert_predefined_into_character_list(["sc"])
        elif self.CharacterSet_Box.currentText() == "Numbers":
            self.charset.insert_predefined_into_character_list(["nmb"])
        self.refresh_characters()

    def insert_char(self):
        if len(self.insertCharacter_line.text()) == 1:
            self.charset.add_to_character_list(self.insertCharacter_line.text())
        else:
            self.charset.add_to_character_list(self.insertCharacter_line.text()[0])
        self.refresh_characters()

    def refresh_characters(self):
        temp = ""
        for i in self.charset.get_character_list():
            temp = temp + i
        self.currentCharacters.setPlainText(temp)

    def copy_to_MainWindow(self):
        self.MainWindow.charset = self.charset
