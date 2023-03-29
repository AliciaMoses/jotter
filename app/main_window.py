from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from editor import Editor

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

    
        self.editor = Editor()
        self.path = None

        layout.addWidget(self.editor)

        container = QWidget()

        container.setLayout(layout)

        self.setCentralWidget(container)

        self.show()

