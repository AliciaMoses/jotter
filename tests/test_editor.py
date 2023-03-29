
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

    def test_line_numbers_visible(self):
        line_number_area = self.editor.line_number_area
        self.assertIsNotNone(line_number_area)

    def test_line_number_area_width(self):
        self.editor.setPlainText("1\n2\n3\n4\n5\n6\n7\n8\n9\n10")
        self.assertEqual(self.editor.line_number_area_width(), 3 + self.editor.fontMetrics().horizontalAdvance('9') * 2)

    def test_line_numbers_update_on_new_line(self):
        self.editor.setPlainText("1\n2\n3")
        initial_width = self.editor.line_number_area_width()
        self.editor.setPlainText("1\n2\n3\n4\n5\n6\n7\n8\n9\n10")
        updated_width = self.editor.line_number_area_width()
        self.assertNotEqual(initial_width, updated_width)


if __name__ == '__main__':
    unittest.main()
