import os.path

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi

from Service.Encryption.CaesarEncrypter import CaesarEncrypter
from Service.Encryption.VigenereEncrypter import VigenereEncrypter
from Service.Text.CaesarText import CaesarText
from Service.Text.VigenereText import VigenereText

from Service.ResourcePath import resource_path


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.init_ui("GUI\\MainWindow.ui")

        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.MSWindowsFixedSizeDialogHint)

        # Exit Button
        exit_button = self.button_Exit
        exit_button.clicked.connect(self.close)

        # Encrypt Button
        encrypt_button = self.button_encrypt
        encrypt_button.clicked.connect(self.encrypt)

        # Decrypt Button
        decrypt_button = self.button_decrypt
        decrypt_button.clicked.connect(self.decrypt)

        self.encryption_dict = {
            "Vigenère": 0,
            "Caesar": 1,
            "Encrypt": 2,
            "Decrypt": 3
        }

    def init_ui(self, ui_name):
        full_path = resource_path(ui_name)
        loadUi(full_path, self)

    def en_de_crypt(self, dict_value, dict_value_2):
        if self.encryption_dict["Vigenère"] == dict_value:
            text = VigenereText()
            encrypter = VigenereEncrypter(text)
        elif self.encryption_dict["Caesar"] == dict_value:
            text = CaesarText()
            encrypter = CaesarEncrypter(text)
        if self.encryption_dict["Encrypt"] == dict_value_2:
            text.fill_character_list(self.clear_TE.toPlainText())
            encrypter.encrypt(self.lineEdit_key.text())
            self.cipher_TE.setPlainText(text.get_cipher_string())
        elif self.encryption_dict["Decrypt"] == dict_value_2:
            text.fill_cipher_list(self.cipher_TE.toPlainText())
            encrypter.decrypt(self.lineEdit_key.text())
            self.clear_TE.setPlainText(text.get_plain_string())

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
