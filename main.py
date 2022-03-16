import sys

from PyQt6.QtWidgets import QApplication

from GUI.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = MainWindow()
    main_menu.show()
    sys.exit(app.exec())

