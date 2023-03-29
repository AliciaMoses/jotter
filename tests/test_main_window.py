import unittest
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow

app = QApplication([])

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.main_window = MainWindow()

    def test_main_window_initial_state(self):
        self.assertEqual(self.main_window.geometry().x(), 100)
        self.assertEqual(self.main_window.geometry().y(), 100)
        self.assertEqual(self.main_window.geometry().width(), 600)
        self.assertEqual(self.main_window.geometry().height(), 400)

if __name__ == '__main__':
    unittest.main()