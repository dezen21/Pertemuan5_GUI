import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Latihan3(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 200)
        self.move(300, 300)
        self.setWindowTitle('Penggunaan QTextEdit')

        self.label1 = QLabel()
        self.label1.setText('Dari')
        self.dari = QLineEdit('Aku')

        self.label2 = QLabel()
        self.label2.setText('Untuk')
        self.untuk = QLineEdit('Jodohku')

        self.label3 = QLabel(" ")

        horizontalLine = QFrame();
        horizontalLine.setFrameShape(QFrame.HLine)
        horizontalLine.setFrameShadow(QFrame.Sunken)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.dari)
        vbox1.addWidget(self.label2)
        vbox1.addWidget(self.untuk)
        vbox1.addWidget(horizontalLine)
        vbox1.addWidget(self.label3)


        self.messageEdit = QTextEdit()

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.messageEdit)

        vbox3 = QVBoxLayout()
        vbox3.addLayout(vbox1)
        vbox3.addLayout(vbox2)

        self.sendButton = QPushButton('&Kirim SMS')
        self.cancelButton = QPushButton('&Batal')

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.sendButton)
        hbox.addWidget(self.cancelButton)

        layout = QVBoxLayout()
        layout.addLayout(vbox3)

        layout.addWidget(horizontalLine)
        layout.addLayout(hbox)
        self.setLayout(layout)


if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = Latihan3()
    form.show()
    a.exec_()
