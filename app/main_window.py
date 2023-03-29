from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QToolBar
from PyQt6.QtGui import QAction
from editor import Editor
from file_handler import FileHandler



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        self.setGeometry(100, 100, 600, 400)
        self.setWindowOpacity(0.9)
        layout = QVBoxLayout()
        self.editor = Editor()
        self.file_handler = FileHandler(self.editor, self)
        self.path = None
        layout.addWidget(self.editor)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self._create_menus_and_toolbars()
        self.show()

    def _create_menus_and_toolbars(self):
        file_toolbar = QToolBar("File")
        self.addToolBar(file_toolbar)
        file_menu = self.menuBar().addMenu("&File")

        open_file_action = QAction("Open file", self)
        open_file_action.setStatusTip("Open file")
        open_file_action.triggered.connect(self.file_handler.file_open)
        file_menu.addAction(open_file_action)
        file_toolbar.addAction(open_file_action)

        save_file_action = QAction("Save", self)
        save_file_action.setStatusTip("Save current page")
        save_file_action.triggered.connect(self.file_handler.file_save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)

        saveas_file_action = QAction("Save As", self)
        saveas_file_action.setStatusTip("Save current page to specified file")
        saveas_file_action.triggered.connect(self.file_handler.file_saveas)
        file_menu.addAction(saveas_file_action)
        file_toolbar.addAction(saveas_file_action)

        print_action = QAction("Print", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.file_handler.file_print)
        file_menu.addAction(print_action)
        file_toolbar.addAction(print_action)

        
