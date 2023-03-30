import unittest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QAction
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
    
    def test_set_opacity(self):
        test_opacity = 0.5
        self.main_window.setWindowOpacity(test_opacity)
        self.assertAlmostEqual(self.main_window.windowOpacity(), test_opacity, places=2)

    def test_open_file_action_connection(self):
        open_file_action = QAction()
        open_file_action.triggered.connect(self.main_window.file_handler.file_open)
        self.assertEqual(open_file_action.receivers(open_file_action.triggered), 1)

    def test_save_file_action_connection(self):
        save_file_action = QAction()
        save_file_action.triggered.connect(self.main_window.file_handler.file_save)
        self.assertEqual(save_file_action.receivers(save_file_action.triggered), 1)

    def test_saveas_file_action_connection(self):
        saveas_file_action = QAction()
        saveas_file_action.triggered.connect(self.main_window.file_handler.file_saveas)
        self.assertEqual(saveas_file_action.receivers(saveas_file_action.triggered), 1)

    def test_print_action_connection(self):
        print_action = QAction()
        print_action.triggered.connect(self.main_window.file_handler.file_print)
        self.assertEqual(print_action.receivers(print_action.triggered), 1)

    def test_undo_action_connection(self):
        undo_action = QAction()
        undo_action.triggered.connect(self.main_window.editor.undo)
        self.assertEqual(undo_action.receivers(undo_action.triggered), 1)

    def test_redo_action_connection(self):
        redo_action = QAction()
        redo_action.triggered.connect(self.main_window.editor.redo)
        self.assertEqual(redo_action.receivers(redo_action.triggered), 1)



if __name__ == '__main__':
    unittest.main()