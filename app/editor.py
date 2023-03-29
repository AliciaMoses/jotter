from PyQt6.QtWidgets import QPlainTextEdit

class Editor(QPlainTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_editor()
        

    def set_editor(self):
        self.set_font() 

    def set_font(self):
        doc = self.document()
        font = doc.defaultFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        doc.setDefaultFont(font)


    