from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QToolBar
from PyQt6.QtGui import QAction
from editor import Editor
from file_handler import FileHandler
from clipboard_handler import ClipboardHandler


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        self.setGeometry(100, 100, 600, 400)
        self.setWindowOpacity(0.9)
        layout = QVBoxLayout()
        self.editor = Editor()
        self.file_handler = FileHandler(self.editor, self)
        self.clipboard_handler = ClipboardHandler(self.editor)
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
        edit_menu = self.menuBar().addMenu("&Edit")

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

        cut_action = QAction("Cut", self)
        cut_action.setStatusTip("Cut selected text")
        cut_action.triggered.connect(self.clipboard_handler.cut)
        edit_menu.addAction(cut_action)

        copy_action = QAction("Copy", self)
        copy_action.setStatusTip("Copy selected text")
        copy_action.triggered.connect(self.clipboard_handler.copy)
        edit_menu.addAction(copy_action)

        paste_action = QAction("Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
        paste_action.triggered.connect(self.clipboard_handler.paste)
        edit_menu.addAction(paste_action)

        
