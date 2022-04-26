from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

from GUI.CharsetWindow import CharsetWindow
from GUI.KasiskiTestWindow import KasiskiTestWindow

from Service.Encryption.CaesarEncrypter import CaesarEncrypter
from Service.Encryption.VigenereEncrypter import VigenereEncrypter
from Service.Text.CaesarText import CaesarText
from Service.Text.EligibleCharacters import EligibleCharacters
from Service.Text.VigenereText import VigenereText

from Service.ResourcePath import resource_path


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.init_ui("GUI\\MainWindow.ui")

        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.encrypter = None
        self.text = None
        self.charset = None

        self.dialog = None

        # Exit Button
        exit_button = self.button_Exit
        exit_button.clicked.connect(self.close)

        # Encrypt Button
        encrypt_button = self.button_encrypt
        encrypt_button.clicked.connect(self.encrypt)

        # Decrypt Button
        decrypt_button = self.button_decrypt
        decrypt_button.clicked.connect(self.decrypt)

        # Menubar File
        exitApplication = self.actionExit
        exitApplication.triggered.connect(self.close)

        # Menubar Settings
        ChangeCharset = self.actionChangeCharset
        ChangeCharset.triggered.connect(self.open_CharsetWindow)

        # Menubar Analysis
        self.actionKeyLength.triggered.connect(self.open_KasiskiTestWindow)

        self.encryption_dict = {
            "Vigenère": 0,
            "Caesar": 1,
            "Encrypt": 2,
            "Decrypt": 3
        }

    def closeEvent(self, event):
        if self.dialog:
            self.dialog.close()

    def init_ui(self, ui_name):
        full_path = resource_path(ui_name)
        loadUi(full_path, self)

    def open_CharsetWindow(self):
        if self.dialog is not None:
            self.dialog.close()
        self.dialog = CharsetWindow(self)
        self.dialog.show()

    def open_KasiskiTestWindow(self):
        if self.dialog is not None:
            self.dialog.close()
        self.dialog = KasiskiTestWindow(self)
        self.dialog.show()

    def set_Text(self, dict_value):
        if self.encryption_dict["Vigenère"] == dict_value:
            self.text = VigenereText()
        elif self.encryption_dict["Caesar"] == dict_value:
            self.text = CaesarText()
        else:
            raise ValueError

    def set_Encrypter(self, dict_value):
        if self.encryption_dict["Vigenère"] == dict_value:
            self.encrypter = VigenereEncrypter(self.text)
        elif self.encryption_dict["Caesar"] == dict_value:
            self.encrypter = CaesarEncrypter(self.text)
        else:
            raise ValueError

    def set_Charset_local(self, charset):
        if isinstance(charset, EligibleCharacters):
            self.charset = charset
        else:
            raise TypeError

    def insert_Charset_in_text(self):
        self.text.set_eligible_characters(self.charset)

    def do_encrypt(self):
        self.text.fill_character_list(self.clear_TE.toPlainText())
        self.encrypter.encrypt(self.lineEdit_key.text())
        self.cipher_TE.setPlainText(self.text.get_cipher_string())

    def do_decrypt(self):
        self.text.fill_cipher_list(self.cipher_TE.toPlainText())
        self.encrypter.decrypt(self.lineEdit_key.text())
        self.clear_TE.setPlainText(self.text.get_plain_string())

    def en_de_crypt(self, dict_value, dict_value_2):
        self.set_Text(dict_value)
        if self.charset is not None:
            self.insert_Charset_in_text()
        self.set_Encrypter(dict_value)

        if self.encryption_dict["Encrypt"] == dict_value_2:
            self.do_encrypt()
        elif self.encryption_dict["Decrypt"] == dict_value_2:
            self.do_decrypt()

    def encrypt(self):
        try:
            if self.comboBox_chiffre.currentText() == "Vigenère-Chiffre":
                self.en_de_crypt(self.encryption_dict["Vigenère"], self.encryption_dict["Encrypt"])
            elif self.comboBox_chiffre.currentText() == "Caesar-Chiffre":
                self.en_de_crypt(self.encryption_dict["Caesar"], self.encryption_dict["Encrypt"])
        except Exception as e:
            print("Encryption Error: " + str(e))

    def decrypt(self):
        try:
            if self.comboBox_chiffre.currentText() == "Vigenère-Chiffre":
                self.en_de_crypt(self.encryption_dict["Vigenère"], self.encryption_dict["Decrypt"])
            elif self.comboBox_chiffre.currentText() == "Caesar-Chiffre":
                self.en_de_crypt(self.encryption_dict["Caesar"], self.encryption_dict["Decrypt"])
        except Exception as e:
            print("Decryption Error: " + str(e))
