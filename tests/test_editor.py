
from editor import Editor 
import unittest
from PyQt6.QtWidgets import QApplication


app = QApplication([])


class TestEditor(unittest.TestCase):

    def setUp(self):
        self.editor = Editor()

    def test_editor_initial_state(self):
      
        self.assertEqual(self.editor.toPlainText(), "")



if __name__ == '__main__':
    unittest.main()
