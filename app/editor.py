from PyQt6.QtWidgets import QPlainTextEdit

class Editor(QPlainTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_editor()

    def set_editor(self):
        pass 


    