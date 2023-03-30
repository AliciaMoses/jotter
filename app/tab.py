from PyQt6.QtWidgets import QWidget, QVBoxLayout
from editor import Editor

class Tab(QWidget):
    def __init__(self, *args, **kwargs):
        super(Tab, self).__init__(*args, **kwargs)
        
        layout = QVBoxLayout()
        self.editor = Editor()
        layout.addWidget(self.editor)
        self.setLayout(layout)