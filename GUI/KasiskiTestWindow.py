from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

from Service.ResourcePath import resource_path

from Service.Analysis.Kasiski.GoBetween import guessKey


class KasiskiTestWindow(QMainWindow):
    def __init__(self, MainWindow):
        super(KasiskiTestWindow, self).__init__()
        self.init_ui("GUI\\KasiskiTestWindow.ui")
        self.MainWindow = MainWindow

        self.load_cipher_text()

        # Buttons
        self.DetermineKeyLength_Button.clicked.connect(self.determine_key_length)
        self.CacheResults_Button.clicked.connect(self.cache_results)

    def init_ui(self, ui_name):
        full_path = resource_path(ui_name)
        loadUi(full_path, self)

    def load_cipher_text(self):
        self.CipherTest_TE.setPlainText(self.MainWindow.cipher_TE.toPlainText())

    def determine_key_length(self):
        self.KeyLengths_TE.setPlainText(str(guessKey(self.CipherTest_TE.toPlainText())))

    def cache_results(self):
        pass
