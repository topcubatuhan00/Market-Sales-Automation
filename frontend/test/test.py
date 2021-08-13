import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon

class saleWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('X Market')
        self.setGeometry(450, 250, 960, 540)

        self.setWindowIcon(QIcon('market.png'))
        self.setStyleSheet('background-color: #293241')

        self.initUI()

    def initUI(self):

        self.labelBarcode = QtWidgets.QLabel(self)
        self.labelBarcode.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBarcode.setText("Barcode Number =>")
        self.labelBarcode.resize(250,50)
        self.labelBarcode.move(200,50)

        self.textBarcode = QtWidgets.QLineEdit(self)
        self.textBarcode.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047; border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.textBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.textBarcode.resize(250,50)
        self.textBarcode.move(510,50)

        self.buttonConfirmation = QPushButton("✔", self)
        self.buttonConfirmation.setStyleSheet('background-color:#d0d1ff; color:#2a9d8f; font-size:24px; border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px')
        self.buttonConfirmation.resize(50,50)
        self.buttonConfirmation.move(455,127)
        self.buttonConfirmation.clicked.connect(self.clickConfirmButton)

        self.labelProductName = QtWidgets.QLabel(self)
        self.labelProductName.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelProductName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductName.setText("Product Name :")
        self.labelProductName.resize(250,50)
        self.labelProductName.move(200,204)

        self.labelProductName = QtWidgets.QLabel(self)
        self.labelProductName.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelProductName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductName.resize(250,50)
        self.labelProductName.move(510,204)

        self.labelProductAmount = QtWidgets.QLabel(self)
        self.labelProductAmount.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelProductAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductAmount.setText("Product Amount :")
        self.labelProductAmount.resize(250,50)
        self.labelProductAmount.move(200,281)

        self.labelProductAmount = QtWidgets.QLabel(self)
        self.labelProductAmount.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelProductAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductAmount.resize(250,50)
        self.labelProductAmount.move(510,281)

        self.labelQuantity = QtWidgets.QLabel(self)
        self.labelQuantity.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelQuantity.setAlignment(QtCore.Qt.AlignCenter)
        self.labelQuantity.setText("Quantity =>")
        self.labelQuantity.resize(250,50)
        self.labelQuantity.move(200,358)

        self.textQuantity = QtWidgets.QLineEdit(self)
        self.textQuantity.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047; border-radius:50px;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.textQuantity.setAlignment(QtCore.Qt.AlignCenter)
        self.textQuantity.resize(250,50)
        self.textQuantity.move(510,358)

        self.labelAmount = QtWidgets.QLabel(self)
        self.labelAmount.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAmount.setText("Total :")
        self.labelAmount.resize(100,40)
        self.labelAmount.move(0,500)

        self.labelAmount = QtWidgets.QLabel(self)
        self.labelAmount.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAmount.resize(100,40)
        self.labelAmount.move(110,500)

        self.buttonNext = QPushButton("Next", self)
        self.buttonNext.setStyleSheet('background-color:#a8dadc; color:#023047; font-size:24px; border: 1px solid #006d77; border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px')
        self.buttonNext.resize(100,40)
        self.buttonNext.move(859,499)

    def clickConfirmButton(self):
        self.productBarcodeName = self.textBarcode.text()
        print(self.productBarcodeName)

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('X Market')
        self.setGeometry(450, 250, 960, 540)

        self.setWindowIcon(QIcon('market.png'))
        self.setStyleSheet('background-color: #293241')

        self.initUI()

    def initUI(self):
        self.btnSale = QPushButton('💲 Satış Yap 💲', self)
        self.btnSale.setStyleSheet('background-color:#f2e9e4; color:#22223b; font-weight:bold; font-size:24px')
        self.btnSale.resize(300,150)
        self.btnSale.move(150,195)
        self.btnSale.clicked.connect(self.saleWindow)

        self.btnAddProd = QPushButton('📁 Ürün Kaydet 📁', self)
        self.btnAddProd.setStyleSheet('background-color:#f2e9e4; color:#22223b; font-weight:bold; font-size:24px')
        self.btnAddProd.setToolTip('This is an example button')
        self.btnAddProd.resize(300,150)
        self.btnAddProd.move(510,195)
        self.btnAddProd.clicked.connect(self.on_clickbtnAddProd)


    def on_clickbtnAddProd(self):
        print("Clicked Add Product Button.")


    def saleWindow(self):
        self.saleWindow = saleWindow()
        self.saleWindow.show()
        self.hide()


def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()