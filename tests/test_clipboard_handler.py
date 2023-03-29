import unittest
from PyQt6.QtWidgets import QApplication, QPlainTextEdit
from clipboard_handler import ClipboardHandler

app = QApplication([])

class TestClipboardHandler(unittest.TestCase):
    def setUp(self):
        self.editor = QPlainTextEdit()
        self.clipboard_handler = ClipboardHandler(self.editor)

    def test_cut(self):
        self.editor.setPlainText("This is test text!")
        self.editor.selectAll()
        self.clipboard_handler.cut()
        self.assertEqual(self.editor.toPlainText(), "")

    def test_copy(self):
        self.editor.setPlainText("This is test text!")
        self.editor.selectAll()
        self.clipboard_handler.copy()
        self.assertEqual(app.clipboard().text(), "This is test text!")

    def test_paste(self):
        app.clipboard().setText("This is test text!")
        self.clipboard_handler.paste()
        self.assertEqual(self.editor.toPlainText(), "This is test text!")

if __name__ == '__main__':
    unittest.main()
