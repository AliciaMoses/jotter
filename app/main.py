from PyQt6.QtWidgets import QApplication
from main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    sys.exit(app.exec())