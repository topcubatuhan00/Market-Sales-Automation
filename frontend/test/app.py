import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon


def on_clickSale():
    print("Clicked")
    

def on_clickbtnAddProd():
    pass

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('X Market')
    win.setGeometry(450, 250, 960, 540)

    win.setWindowIcon(QIcon('market.png'))
    win.setStyleSheet('background-color: #4a4e69')


    btnSale = QPushButton('💲 Satış Yap 💲', win)
    btnSale.setStyleSheet('background-color:#f2e9e4; color:#22223b; font-weight:bold; font-size:24px')
    btnSale.setToolTip('This is an example button')
    btnSale.resize(300,150)
    btnSale.move(150,195)
    btnSale.clicked.connect(on_clickSale)

    btnAddProd = QPushButton('📁 Ürün Kaydet 📁', win)
    btnAddProd.setStyleSheet('background-color:#f2e9e4; color:#22223b; font-weight:bold; font-size:24px')
    btnAddProd.setToolTip('This is an example button')
    btnAddProd.resize(300,150)
    btnAddProd.move(510,195)
    btnAddProd.clicked.connect(on_clickbtnAddProd)

    
    win.show()
    sys.exit(app.exec_())

window()