import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Latihan1(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(500, 600)
        self.move(300, 300)
        self.setWindowTitle('Tugas Praktikum Menyisipkan Gambar')

        self.label1 = QLabel()
        self.label1.setText('<b><font size=11 color = purple> Logo FTII: </font></b>')

        self.label2 = QLabel()
        self.label2.setText('<img src="ittp/ftii.png">')

        self.label3 = QLabel()
        self.label3.setText('<b><font size=11 color = red> Logo FTTE: </font></b>')

        self.label4 = QLabel()
        self.label4.setText('<img src="ittp/ftte.png">')

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)
        self.setLayout(layout)


if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = Latihan1()
    form.show()

    a.exec_()
