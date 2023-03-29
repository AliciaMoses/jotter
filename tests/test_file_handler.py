import unittest 
from unittest.mock import MagicMock, patch
from PyQt6.QtWidgets import QApplication
from file_handler import FileHandler
from editor import Editor

app = QApplication([])

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.editor = Editor()
        self.file_handler = FileHandler(self.editor, None)

    @patch("file_handler.QFileDialog.getSaveFileName")
    @patch("builtins.open", new_callable=MagicMock)
    def test_file_saveas(self, mock_open, mock_getSaveFileName):
        mock_getSaveFileName.return_value = ('test.txt', 'Text documents (*.txt);All files (*.*)')
        self.editor.setPlainText("This is a test.")
        self.file_handler.file_saveas()
        mock_open.assert_called_once_with('test.txt', 'w')

    @patch("file_handler.QFileDialog.getOpenFileName")
    @patch("builtins.open", new_callable=MagicMock)
    def test_file_open(self, mock_open, mock_getOpenFileName):
        mock_getOpenFileName.return_value = ('test.txt', 'Text documents (*.txt);All files (*.*)')
        mock_open.return_value.__enter__.return_value.read.return_value = "This is a test."
        self.file_handler.file_open()
        self.assertEqual(self.editor.toPlainText(), "This is a test.")
        mock_open.assert_called_once_with('test.txt', 'rU')

if __name__ == '__main__':
    unittest.main()