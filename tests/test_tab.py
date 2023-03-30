import unittest
from PyQt6.QtWidgets import QApplication, QVBoxLayout
from tab import Tab
from editor import Editor

app = QApplication([])

class TestTab(unittest.TestCase):
    
    def setUp(self):
        self.tab = Tab()
    
    def test_editor_and_layout_in_tab(self):
        self.assertIsInstance(self.tab.layout(), QVBoxLayout)
        self.assertIsInstance(self.tab.layout().itemAt(0).widget(), Editor)


    def test_tab_initial_state(self):
        self.assertIsNotNone(self.tab.editor)

    def test_editor_content(self):
        self.tab.editor.setPlainText("Test content")
        self.assertEqual(self.tab.editor.toPlainText(), "Test content")

if __name__ == '__main__':
    unittest.main()