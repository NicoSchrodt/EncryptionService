import sys
from UnitTests.tests import TestClass
from PyQt6.QtWidgets import QApplication

from Service.Text.Vigeneretext import VigenereText
from Service.Encryption.VigenereEncrypter import VigenereEncrypter
from GUI.MainWindow import MainWindow


# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':
    text2 = VigenereText()
    text2.fill_character_list("Tes&t")
    text2_enc = VigenereEncrypter(text2)
    text2_enc.encrypt("EinSchluessel")
    print(f'Cipher: {text2.cipher_character_list}')

    app = QApplication(sys.argv)
    main_menu = MainWindow()
    main_menu.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
