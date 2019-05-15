import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Latihan4(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 150)
        self.move(300, 300)
        self.setWindowTitle('Tugas QRadioButton')

        self.label1 = QLabel()
        self.label1.setText('Bilangan pertama')
        self.bilPetama = QLineEdit()
        self.bilPetama.setValidator(QIntValidator())


        self.label2 = QLabel()
        self.label2.setText('Bilangan kedua    ')
        self.bilKedua = QLineEdit()
        self.bilKedua.setValidator(QIntValidator())

        mGlyout = QGridLayout()
        mGlyout.addWidget(self.label1,0,0)
        mGlyout.addWidget(self.bilPetama,0,1)
        mGlyout.addWidget(self.label2,1,0)
        mGlyout.addWidget(self.bilKedua,1,1)


        self.cekTambah = QRadioButton()
        self.cekTambah.setText('&Tambah')
        self.cekTambah.setChecked(True)
        self.cekKurang = QRadioButton()
        self.cekKurang.setText('&Kurang')
        self.cekKali = QRadioButton()
        self.cekKali.setText('&Kali')
        self.cekBagi = QRadioButton()
        self.cekBagi.setText('&Bagi')

        hbox = QHBoxLayout()
        hbox.addWidget(self.cekTambah)
        hbox.addWidget(self.cekKurang)
        hbox.addWidget(self.cekKali)
        hbox.addWidget(self.cekBagi)

        self.resultLabel = QLabel('<b>Hasil: </b>')
        self.checkButton = QPushButton('Hitung')

        layout = QVBoxLayout()
        layout.addLayout(mGlyout)
        layout.addLayout(hbox)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.checkButton)
        layout.addStretch()

        self.setLayout(layout)
        self.checkButton.clicked.connect(self.checkButtonClick)

    def checkButtonClick(self):
        one = float(self.bilPetama.text())
        two = float(self.bilKedua.text())
        if self.cekTambah.isChecked():
            res = one+two
            self.resultLabel.setText('<b>Hasil Pertambahan : </b>'+str(res))
        elif self.cekKurang.isChecked():
            res = one - two
            self.resultLabel.setText('<b>Hasil Pengurangan : </b>'+str(res))
        elif self.cekKali.isChecked():
            res = one * two
            self.resultLabel.setText('<b>Hasil Perkalian : </b>'+str(res))
        else:
            res = one / two
            self.resultLabel.setText('<b>Hasil Pembagian : </b>'+str(res))


if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = Latihan4()
    form.show()
    a.exec_()
