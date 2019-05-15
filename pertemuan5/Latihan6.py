import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Latihan6(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Latihan QComboBox')

        self.comboMakanan = QComboBox()
        self.comboMakanan.addItem("--Pilih Makanan--")
        self.comboMakanan.addItem('Mendoan')
        self.comboMakanan.addItem('Cireng')
        self.comboMakanan.addItem('Gethuk')
        self.comboMakanan.addItem('Tahu Bulat')
        self.comboMakanan.addItem('Ketan Susu')

        self.comboMinuman = QComboBox()
        self.comboMinuman.addItem("--Pilih Minuman--")
        self.comboMinuman.addItem("Es Cincau")
        self.comboMinuman.addItem("Milkshake")
        self.comboMinuman.addItem("Chatime")
        self.comboMinuman.addItem("Thaitea")
        self.comboMinuman.addItem("Kopi Hitam")

        self.getTextButton = QPushButton('Pilihan Anda')

        layout = QVBoxLayout()
        layout.addWidget(self.comboMakanan)
        layout.addWidget(self.comboMinuman)
        layout.addWidget(self.getTextButton)

        layout.addStretch()
        self.setLayout(layout)

        self.getTextButton.clicked.connect(self.getTextButtonClick)

    def getTextButtonClick(self):
        QMessageBox.information(self, 'Informasi','Anda memilih: '+ self.comboMakanan.currentText() + " & " + self.comboMinuman.currentText())

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = Latihan6()
    form.show()

    a.exec_()
