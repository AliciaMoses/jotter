
from editor import Editor 
import unittest
from PyQt6.QtWidgets import QApplication


app = QApplication([])

class TestEditor(unittest.TestCase):

    def setUp(self):
        self.editor = Editor()

    def test_editor_initial_state(self):
      
        self.assertEqual(self.editor.toPlainText(), "")
    
    def test_editor_add_text(self):
        test_text = "This is a test text."
        self.editor.setPlainText(test_text)
        self.assertEqual(self.editor.toPlainText(), test_text)
    
    def test_editor_font_family(self):
        doc = self.editor.document()
        font = doc.defaultFont()
        font_family = font.family()
        self.assertEqual(font_family, "Courier New")

    def test_editor_font_size(self):
        doc = self.editor.document()
        font = doc.defaultFont()
        font_size = font.pointSize()
        self.assertEqual(font_size, 11)


if __name__ == '__main__':
    unittest.main()
