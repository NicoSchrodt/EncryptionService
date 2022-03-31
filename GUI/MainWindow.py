import os.path
import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi

from Service.Encryption.VigenereEncrypter import VigenereEncrypter
from Service.Text.VigenereText import VigenereText


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

    def init_ui(self, ui_name):
        base_path = os.path.abspath(".")
        full_path = os.path.join(base_path, ui_name)
        loadUi(full_path, self)

    def encrypt(self):
        if self.comboBox_chiffre.currentText() == "Vigenère-Chiffre":
            try:
                text = VigenereText()
                text.fill_character_list(self.clear_TE.toPlainText())
                encrypter = VigenereEncrypter(text)
                encrypter.encrypt(self.lineEdit_key.text())
                self.cipher_TE.setPlainText(text.get_cipher_string())
            except Exception as e:
                print("Encryption Error: " + str(e))

    def decrypt(self):
        if self.comboBox_chiffre.currentText() == "Vigenère-Chiffre":
            try:
                text = VigenereText()
                text.fill_cipher_list(self.cipher_TE.toPlainText())
                encrypter = VigenereEncrypter(text)
                encrypter.decrypt(self.lineEdit_key.text())
                self.clear_TE.setPlainText(text.get_plain_string())
            except Exception as e:
                print("Decryption Error: " + str(e))
