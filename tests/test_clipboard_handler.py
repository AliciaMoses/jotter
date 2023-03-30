import unittest
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QPlainTextEdit
from functools import partial
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

    def test_undo(self):
        self.editor.setPlainText("This is test text!")
        self.clipboard_handler.undo()
        QTimer.singleShot(100, partial(self._check_after_undo, self.editor.toPlainText()))

    def _check_after_undo(self, text):
        self.assertEqual(text, "")

    def test_redo(self):
        self.editor.setPlainText("This is test text!")
        self.clipboard_handler.undo()
        QTimer.singleShot(100, self._after_undo)

    def _after_undo(self):
        self.assertEqual(self.editor.toPlainText(), "")
        self.clipboard_handler.redo()
        QTimer.singleShot(100, partial(self._check_after_redo, self.editor.toPlainText()))

    def _check_after_redo(self, text):
        self.assertEqual(text, "This is test text!")

if __name__ == '__main__':
    unittest.main()
