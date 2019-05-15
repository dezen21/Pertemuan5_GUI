import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Latihan2(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 100)
        self.move(300, 300)

        self.setWindowTitle('Tugas Menyisipkan Icon')
        self.label = QLabel()

        self.label.setText('<b>Bahasa Pemprogramman Favorit Anda</b>')

        icon1 = QIcon('bahasa/python.png')
        self.button1 = QPushButton('\tPython')
        self.button1.setIcon(icon1)

        icon2 = QIcon('bahasa/java.png')
        self.button2 = QPushButton('\tJava')
        self.button2.setIcon(icon2)

        icon3 = QIcon('bahsa/php.png')
        self.button3 = QPushButton('\tPHP')
        self.button3.setIcon(icon3)

        icon4 = QIcon('bahasa/c-plus-plus.png')
        self.button4 = QPushButton('\tC/C++')
        self.button4.setIcon(icon4)

        btnGrid = QGridLayout()
        btnGrid.addWidget(self.button1, 0, 0)
        btnGrid.addWidget(self.button2, 0, 1)
        btnGrid.addWidget(self.button3, 1, 0)
        btnGrid.addWidget(self.button4, 1, 1)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(btnGrid)
        self.setLayout(layout)


if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = Latihan2()
    form.show()
    a.exec_()
