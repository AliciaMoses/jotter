from PyQt6.QtWidgets import QApplication

class ClipboardHandler:
    def __init__(self, editor):
        self.editor = editor
        self.clipboard = QApplication.clipboard()
    
    def cut(self):
        self.editor.cut()

    def copy(self):
        self.editor.copy()

    def paste(self):
        self.editor.paste()

    def undo(self):
        self.editor.undo()

    def redo(self):
        self.editor.redo()