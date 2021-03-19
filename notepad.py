import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QHBoxLayout,QPushButton,QVBoxLayout,QLabel,QFileDialog,QAction,qApp,QMainWindow

class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.temizle = QPushButton("Temizle")
        self.ac = QPushButton("Aç")
        self.dosya_olustur = QPushButton("Yeni")

        h_box = QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.dosya_olustur)

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("Note Pad")
        self.temizle.clicked.connect(self.sil)
        self.ac.clicked.connect(self.dosya_ac)
        self.dosya_olustur.clicked.connect(self.yeni_dosya)

    def sil(self):
        self.yazi_alani.clear()
    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("Desktop"))
        with open(dosya_ismi[0],"r") as file:
            self.yazi_alani.setText(file.read())
    def yeni_dosya(self):
        dosya_ismi = QFileDialog.getSaveFileName(self, "Dosya Kaydet",os.getenv("Desktop"))
        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazi_alani.toPlainText())

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = Notepad()
        self.setCentralWidget(self.pencere)
        self.menuleri_olustur()
        self.setWindowTitle("Note Pad")
        self.show()
    def menuleri_olustur(self):
        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")
        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")
        temizle = QAction("Temizle",self)
        temizle.setShortcut("Ctrl+D")
        cikis = QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response)

    def response(self,action):
        if action.text() == "Dosya Aç":
            self.pencere.dosya_ac()
        elif action.text() == "Dosya Kaydet":
            self.pencere.yeni_dosya()
        elif action.text() == "Temizle":
            self.pencere.sil()
        elif action.text() == "Çıkış":
            qApp.quit()




app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec())
