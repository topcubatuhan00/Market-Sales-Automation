
import sys, sqlite3, datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PyQt5.QtGui import QIcon

from backend import backendServices

class addProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('X Market')
        self.setGeometry(450, 250, 960, 540)

        self.setWindowIcon(QIcon('./frontend/icons/market.png'))
        self.setStyleSheet('background-color: #293241')

        self.initUI()

    def initUI(self):
        
        self.labelBarcode = QtWidgets.QLabel(self)
        self.labelBarcode.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBarcode.setText("Barcode Number =>")
        self.labelBarcode.resize(250,75)
        self.labelBarcode.move(200,45)

        self.textBarcode = QtWidgets.QLineEdit(self)
        self.textBarcode.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047; border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.textBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.textBarcode.resize(250,75)
        self.textBarcode.move(510,45)

        self.labelProductName = QtWidgets.QLabel(self)
        self.labelProductName.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelProductName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductName.setText("Product Name =>")
        self.labelProductName.resize(250,75)
        self.labelProductName.move(200,170)

        self.textProductName = QtWidgets.QLineEdit(self)
        self.textProductName.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047; border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.textProductName.setAlignment(QtCore.Qt.AlignCenter)
        self.textProductName.resize(250,75)
        self.textProductName.move(510,170)

        self.labelAmount = QtWidgets.QLabel(self)
        self.labelAmount.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAmount.setText("Product Amount =>")
        self.labelAmount.resize(250,75)
        self.labelAmount.move(200,295)

        self.textAmount = QtWidgets.QLineEdit(self)
        self.textAmount.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047; border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.textAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.textAmount.resize(250,75)
        self.textAmount.move(510,295)

        self.buttonBackHome = QPushButton("Home", self)
        self.buttonBackHome.setStyleSheet('background-color:#e76f51; color:#e9edc9; font-size:24px; border: 1px solid #293241; border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px')
        self.buttonBackHome.resize(125,75)
        self.buttonBackHome.move(325,420)
        self.buttonBackHome.clicked.connect(self.backHome)

        self.buttonSave = QPushButton("Save", self)
        self.buttonSave.setStyleSheet('background-color:#2a9d8f; color:#e9edc9; font-size:24px;border: 1px solid #293241; border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px')
        self.buttonSave.resize(125,75)
        self.buttonSave.move(510,420)
        self.buttonSave.clicked.connect(self.save)
        
    def backHome(self):
        self.mainForm = MainForm()
        self.mainForm.show()
        self.hide()

    def save(self):
        if backendServices.checkBarcode(int(self.textBarcode.text())):
            self.msg2 = QMessageBox()
            self.msg2.setIcon(QMessageBox.Warning)
            self.msg2.setWindowIcon(QIcon('./frontend/icons/warning.png'))
            self.msg2.setText("This barcode number is already in use.")
            self.msg2.setWindowTitle("Warning!")
                
            self.msg2.exec_()

        else:
            try:
                self.barcodeNumber = int(self.textBarcode.text())
                self.productName = self.textProductName.text()
                self.productAmount = int(self.textAmount.text())

                if len(self.labelBarcode.text()) == 0 | len(self.labelProductName.text()) == 0 | len(self.labelAmount.text()) == 0:
                    self.msg1 = QMessageBox()
                    self.msg1.setIcon(QMessageBox.Warning)
                    self.msg1.setWindowIcon(QIcon('./frontend/icons/warning.png'))
                    self.msg1.setText("Fill in the information completely.")
                    self.msg1.setWindowTitle("Warning!")
                    self.msg1.exec_()
                else:
                    backendServices.addProduct(self.barcodeNumber,self.productName,self.productAmount)
                    self.msg3 = QMessageBox()
                    self.msg3.setIcon(QMessageBox.Information)
                    self.msg3.setWindowIcon(QIcon('./frontend/icons/confirm.png'))
                    self.msg3.setText("Product added successfully")
                    self.msg3.setWindowTitle("Congratulations")

                    self.msg3.exec_()

            except ValueError:
                self.msg4 = QMessageBox()
                self.msg4.setIcon(QMessageBox.Warning)
                self.msg4.setWindowIcon(QIcon('./frontend/icons/warning.png'))
                self.msg4.setText("Fill in the all blanks.")
                self.msg4.setWindowTitle("Warning!")
                self.msg4.exec_()
        self.textProductName.setText("")
        self.textBarcode.setText("")
        self.textAmount.setText("")

class saleWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('X Market')
        self.setGeometry(450, 250, 960, 540)

        self.setWindowIcon(QIcon('./frontend/icons/market.png'))
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

        self.labelProductNameArea = QtWidgets.QLabel(self)
        self.labelProductNameArea.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelProductNameArea.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductNameArea.resize(250,50)
        self.labelProductNameArea.move(510,204)

        self.labelProductAmount = QtWidgets.QLabel(self)
        self.labelProductAmount.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelProductAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductAmount.setText("Product Amount :")
        self.labelProductAmount.resize(250,50)
        self.labelProductAmount.move(200,281)

        self.labelProductAmountArea = QtWidgets.QLabel(self)
        self.labelProductAmountArea.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelProductAmountArea.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductAmountArea.resize(250,50)
        self.labelProductAmountArea.move(510,281)

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

        self.buttonAdd = QPushButton("Add", self)
        self.buttonAdd.setStyleSheet('background-color:#a8dadc; color:#023047; font-size:24px; border: 1px solid #006d77; border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px')
        self.buttonAdd.resize(100,40)
        self.buttonAdd.move(430,435)
        if str(self.labelProductAmountArea.text()) != 0: 
            self.buttonAdd.clicked.connect(self.addBasket)
        
        self.labelAmount = QtWidgets.QLabel(self)
        self.labelAmount.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAmount.setText("Total :")
        self.labelAmount.resize(100,40)
        self.labelAmount.move(0,500)

        self.labelAmountArea = QtWidgets.QLabel(self)
        self.labelAmountArea.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelAmountArea.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAmountArea.setText("0")
        self.labelAmountArea.resize(100,40)
        self.labelAmountArea.move(110,500)

        self.buttonNext = QPushButton("Next", self)
        self.buttonNext.setStyleSheet('background-color:#a8dadc; color:#023047; font-size:24px; border: 1px solid #006d77; border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px')
        self.buttonNext.resize(100,40)
        self.buttonNext.move(859,499)
        self.buttonNext.clicked.connect(self.nextClick)

        self.buttonBackHome = QPushButton("Home", self)
        self.buttonBackHome.setStyleSheet('background-color:#e76f51; color:#e9edc9; font-size:24px; border: 1px solid #293241; border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px')
        self.buttonBackHome.resize(130,40)
        self.buttonBackHome.move(415,500)
        self.buttonBackHome.clicked.connect(self.backHome)

    def backHome(self):
        self.mainForm = MainForm()
        self.mainForm.show()
        self.hide()

    def clickConfirmButton(self):
        self.labelProductNameArea.setText(" ")
        self.labelProductAmountArea.setText(" ")
        if len(str(self.textBarcode.text())) != 0:
            try:
                self.productBarcodeName = self.textBarcode.text()
                data = backendServices.getProductWithBarcodeNumber(self.productBarcodeName)
                
                for row in data:
                    self.productName = row[1]
                    self.productAmount = row[2]
                    self.labelProductNameArea.setText(self.productName)
                    self.labelProductAmountArea.setText(str(self.productAmount))
            except sqlite3.OperationalError:
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.setWindowIcon(QIcon('./frontend/icons/warning.png'))
                self.msg.setText("Please enter the information correctly and completely.")
                self.msg.setWindowTitle("Warning!")

                self.msg.exec_()

    def addBasket(self):
        try:
            self.quantity = int(self.textQuantity.text())
            self.basketTotal = int(self.labelAmountArea.text())
            
            self.text = self.basketTotal + (self.quantity * self.productAmount)
            self.labelAmountArea.setText(self.text)
            
        except ValueError:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setWindowIcon(QIcon('./frontend/icons/warning.png'))
            self.msg.setText("Please enter the information correctly and completely.")
            self.msg.setWindowTitle("Warning!")
            self.msg.exec_()
        except AttributeError:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setWindowIcon(QIcon('./frontend/icons/warning.png'))
            self.msg.setText("Please enter the information correctly and completely.")
            self.msg.setWindowTitle("Warning!")
            self.msg.exec_()

        self.textBarcode.setText(" ")
        self.labelProductNameArea.setText(" ")
        self.labelProductAmountArea.setText(" ")
        self.textQuantity.setText(" ")

    def nextClick(self):
        self.currentAmount = int(self.labelAmountArea.text())

        if self.currentAmount != 0:
            backendServices.saveAmount(str(datetime.datetime.now().date()),self.currentAmount)
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowIcon(QIcon('./frontend/icons/confirm.png'))
            self.msg.setText("Transaction completed successfully")
            self.msg.setWindowTitle("Congratulations")

            self.msg.exec_()

            self.labelAmountArea.setText("0")
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setWindowIcon(QIcon('./frontend/icons/warning.png'))
            self.msg.setText("Please sell first.")
            self.msg.setWindowTitle("Warning!")

            self.msg.exec_()

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('X Market')
        self.setGeometry(450, 250, 960, 540)

        self.setWindowIcon(QIcon('./frontend/icons/market.png'))
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
        self.btnAddProd.resize(300,150)
        self.btnAddProd.move(510,195)
        self.btnAddProd.clicked.connect(self.addProductWindow)

        self.date = datetime.datetime.now().date()
        self.dailyEarnings = backendServices.dailyEarnings(self.date)

        self.labelDailyEarnings = QtWidgets.QLabel(self)
        self.labelDailyEarnings.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047;border-top-left-radius :20px; border-top-right-radius : 20px; border-bottom-left-radius : 20px; border-bottom-right-radius : 20px")
        self.labelDailyEarnings.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDailyEarnings.setText(f"Daily Earnings : {self.dailyEarnings}")
        self.labelDailyEarnings.resize(260,75)
        self.labelDailyEarnings.move(350,465)

    def addProductWindow(self):
        self.addProductWindow = addProductWindow()
        self.addProductWindow.show()
        self.hide()


    def saleWindow(self):
        self.saleWindow = saleWindow()
        self.saleWindow.show()
        self.hide()


def run():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

run()