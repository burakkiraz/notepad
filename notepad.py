import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QHBoxLayout,QPushButton,QVBoxLayout,QFileDialog,QAction,qApp,QMainWindow

class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.text_area = QTextEdit()
        self.clear = QPushButton("Clear All")
        self.open = QPushButton("Open File")
        self.new_file = QPushButton("New File")

        h_box = QHBoxLayout()
        h_box.addWidget(self.clear)
        h_box.addWidget(self.open)
        h_box.addWidget(self.new_file)

        v_box = QVBoxLayout()
        v_box.addWidget(self.text_area)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("NotePad")
        self.clear.clicked.connect(self.delete)
        self.open.clicked.connect(self.open_file)
        self.new_file.clicked.connect(self.new_fille)

    def delete(self):
        self.text_area.clear()
    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self,"Open File",os.getenv("Desktop"))
        with open(file_name[0],"r") as file:
            self.text_area.setText(file.read())
    def new_fille(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File",os.getenv("Desktop"))
        with open(file_name[0],"w") as file:
            file.write(self.text_area.toPlainText())

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.windoww = Notepad()
        self.setCentralWidget(self.windoww)
        self.create_menu()
        self.setWindowTitle("Note Pad")
        self.show()
    def create_menu(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        open_file = QAction("Open File",self)
        open_file.setShortcut("Ctrl+O")
        save_file = QAction("Save File",self)
        save_file.setShortcut("Ctrl+S")
        clear = QAction("Clear",self)
        clear.setShortcut("Ctrl+D")
        exit = QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")
        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(clear)
        file.addAction(exit)

        file.triggered.connect(self.response)

    def response(self,action):
        if action.text() == "Open File":
            self.windoww.open_file()
        elif action.text() == "Save File":
            self.windoww.yeni_file()
        elif action.text() == "Clear":
            self.windoww.delete()
        elif action.text() == "Exit":
            qApp.quit()




app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec())
