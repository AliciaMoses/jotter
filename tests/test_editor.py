
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



if __name__ == '__main__':
    unittest.main()
