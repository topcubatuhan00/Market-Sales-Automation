
import sys, sqlite3, datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from backend import backendServices

class salesHistoryPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('X Market')
        self.setGeometry(450, 250, 960, 540)

        self.setWindowIcon(QIcon('./frontend/icons/market.png'))
        self.setStyleSheet('background-color: #293241')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))

class addProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('X Market')
        self.setGeometry(450, 250, 960, 540)

        self.setWindowIcon(QIcon('./frontend/icons/market.png'))
        self.setStyleSheet('background-color: #293241')

        self.initUI()

    def warningMessage(self,messageContent):

        self.message = QMessageBox()
        self.message.setIcon(QMessageBox.Warning)
        self.message.setWindowIcon(QIcon('./frontend/icons/warning.png'))
        self.message.setText(messageContent)
        self.message.setWindowTitle("Warning!")
                
        self.message.exec_()

    def congMessage(self,messageContent):
        self.messageCong = QMessageBox()
        self.messageCong.setIcon(QMessageBox.Information)
        self.messageCong.setWindowIcon(QIcon('./frontend/icons/confirm.png'))
        self.messageCong.setText(messageContent)
        self.messageCong.setWindowTitle("Congratulations")

        self.messageCong.exec_()

    def initUI(self):
        
        self.labelBarcode = QtWidgets.QLabel(self)
        self.labelBarcode.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBarcode.setText("Barcode Number =>")
        self.labelBarcode.resize(250,75)
        self.labelBarcode.move(200,45)

        self.textBarcode = QtWidgets.QLineEdit(self)
        self.textBarcode.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.textBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.textBarcode.resize(250,75)
        self.textBarcode.move(510,45)

        self.labelProductName = QtWidgets.QLabel(self)
        self.labelProductName.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelProductName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductName.setText("Product Name =>")
        self.labelProductName.resize(250,75)
        self.labelProductName.move(200,170)

        self.textProductName = QtWidgets.QLineEdit(self)
        self.textProductName.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.textProductName.setAlignment(QtCore.Qt.AlignCenter)
        self.textProductName.resize(250,75)
        self.textProductName.move(510,170)

        self.labelAmount = QtWidgets.QLabel(self)
        self.labelAmount.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAmount.setText("Product Amount =>")
        self.labelAmount.resize(250,75)
        self.labelAmount.move(200,295)

        self.textAmount = QtWidgets.QLineEdit(self)
        self.textAmount.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.textAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.textAmount.resize(250,75)
        self.textAmount.move(510,295)

        self.buttonBackHome = QPushButton("Home", self)
        self.buttonBackHome.setStyleSheet('background-color:#e76f51; color:#e9edc9; font-size:24px; border: 1px solid #293241; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px')
        self.buttonBackHome.resize(125,75)
        self.buttonBackHome.move(325,420)
        self.buttonBackHome.clicked.connect(self.backHome)

        self.buttonSave = QPushButton("Save", self)
        self.buttonSave.setStyleSheet('background-color:#2a9d8f; color:#e9edc9; font-size:24px;border: 1px solid #293241; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px')
        self.buttonSave.resize(125,75)
        self.buttonSave.move(510,420)
        self.buttonSave.clicked.connect(self.save)
        
    def backHome(self):
        self.mainForm = MainForm()
        self.mainForm.show()
        self.hide()

    def save(self):
        if len(str(self.textBarcode.text())) != 0:
            if backendServices.checkBarcode(int(self.textBarcode.text())):
                self.warningMessage("This barcode number is already in use.")
            else:
                try:
                    self.barcodeNumber = int(self.textBarcode.text())
                    self.productName = self.textProductName.text()
                    self.productAmount = int(self.textAmount.text())

                    if len(self.labelBarcode.text()) == 0 | len(self.labelProductName.text()) == 0 | len(self.labelAmount.text()) == 0:
                        self.warningMessage("Fill in the information completely.")
                    else:
                        backendServices.addProduct(self.barcodeNumber,self.productName,self.productAmount)
                        self.congMessage("Product added successfully")
                        
                except ValueError:
                    self.warningMessage("Fill in the all blanks.")
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

    def warningMessage(self,messageContent):

        self.message = QMessageBox()
        self.message.setIcon(QMessageBox.Warning)
        self.message.setWindowIcon(QIcon('./frontend/icons/warning.png'))
        self.message.setText(messageContent)
        self.message.setWindowTitle("Warning!")
                
        self.message.exec_()

    def congMessage(self,messageContent):
        self.messageCong = QMessageBox()
        self.messageCong.setIcon(QMessageBox.Information)
        self.messageCong.setWindowIcon(QIcon('./frontend/icons/confirm.png'))
        self.messageCong.setText(messageContent)
        self.messageCong.setWindowTitle("Congratulations")

        self.messageCong.exec_()

    def initUI(self):

        self.labelBarcode = QtWidgets.QLabel(self)
        self.labelBarcode.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBarcode.setText("Barcode Number =>")
        self.labelBarcode.resize(250,50)
        self.labelBarcode.move(200,50)

        self.textBarcode = QtWidgets.QLineEdit(self)
        self.textBarcode.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.textBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.textBarcode.resize(250,50)
        self.textBarcode.move(510,50)

        self.buttonConfirmation = QPushButton("✔", self)
        self.buttonConfirmation.setStyleSheet('background-color:#d0d1ff; color:#2a9d8f; font-size:24px; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px')
        self.buttonConfirmation.resize(50,50)
        self.buttonConfirmation.move(455,127)
        self.buttonConfirmation.clicked.connect(self.clickConfirmButton)    
        

        self.labelProductName = QtWidgets.QLabel(self)
        self.labelProductName.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelProductName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductName.setText("Product Name :")
        self.labelProductName.resize(250,50)
        self.labelProductName.move(200,204)

        self.labelProductNameArea = QtWidgets.QLabel(self)
        self.labelProductNameArea.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelProductNameArea.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductNameArea.resize(250,50)
        self.labelProductNameArea.move(510,204)

        self.labelProductAmount = QtWidgets.QLabel(self)
        self.labelProductAmount.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelProductAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductAmount.setText("Product Amount :")
        self.labelProductAmount.resize(250,50)
        self.labelProductAmount.move(200,281)

        self.labelProductAmountArea = QtWidgets.QLabel(self)
        self.labelProductAmountArea.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelProductAmountArea.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductAmountArea.resize(250,50)
        self.labelProductAmountArea.move(510,281)

        self.labelQuantity = QtWidgets.QLabel(self)
        self.labelQuantity.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelQuantity.setAlignment(QtCore.Qt.AlignCenter)
        self.labelQuantity.setText("Quantity =>")
        self.labelQuantity.resize(250,50)
        self.labelQuantity.move(200,358)

        self.textQuantity = QtWidgets.QLineEdit(self)
        self.textQuantity.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047; border-radius:50px;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.textQuantity.setAlignment(QtCore.Qt.AlignCenter)
        self.textQuantity.resize(250,50)
        self.textQuantity.move(510,358)

        self.buttonAdd = QPushButton("Add", self)
        self.buttonAdd.setStyleSheet('background-color:#a8dadc; color:#023047; font-size:24px; border: 1px solid #006d77; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px')
        self.buttonAdd.resize(100,40)
        self.buttonAdd.move(430,435)
        if str(self.labelProductAmountArea.text()) != 0: 
            self.buttonAdd.clicked.connect(self.addBasket)
        
        self.labelAmount = QtWidgets.QLabel(self)
        self.labelAmount.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAmount.setText("Total :")
        self.labelAmount.resize(100,40)
        self.labelAmount.move(0,500)

        self.labelAmountArea = QtWidgets.QLabel(self)
        self.labelAmountArea.setStyleSheet("background-color:#d0d1ff; font-size:20px; color:#023047;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelAmountArea.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAmountArea.setText("0")
        self.labelAmountArea.resize(100,40)
        self.labelAmountArea.move(110,500)

        self.buttonNext = QPushButton("Next", self)
        self.buttonNext.setStyleSheet('background-color:#a8dadc; color:#023047; font-size:24px; border: 1px solid #006d77; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px')
        self.buttonNext.resize(100,40)
        self.buttonNext.move(859,499)
        self.buttonNext.clicked.connect(self.nextClick)

        self.buttonBackHome = QPushButton("Home", self)
        self.buttonBackHome.setStyleSheet('background-color:#e76f51; color:#e9edc9; font-size:24px; border: 1px solid #293241; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px')
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
                self.warningMessage("Please enter the information correctly and completely.")
    def addBasket(self):
        try:
            self.quantity = int(self.textQuantity.text())
            self.basketTotal = int(self.labelAmountArea.text())
            
            self.text = str(self.basketTotal + (self.quantity * self.productAmount))
            self.labelAmountArea.setText(self.text)
            
        except ValueError:
            self.warningMessage("Please enter the information correctly and completely.")
        except AttributeError:
            self.warningMessage("Please enter the information correctly and completely.")

        self.textBarcode.setText(" ")
        self.labelProductNameArea.setText(" ")
        self.labelProductAmountArea.setText(" ")
        self.textQuantity.setText(" ")

    def nextClick(self):
        self.currentAmount = int(self.labelAmountArea.text())

        if self.currentAmount != 0:
            backendServices.saveAmount(str(datetime.datetime.now().date()),self.currentAmount,str(datetime.datetime.now().strftime("%H:%M")))
            self.congMessage("Transaction completed successfully")

            self.labelAmountArea.setText("0")
        else:
            self.warningMessage("Please sell first.")

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
        self.labelDailyEarnings.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelDailyEarnings.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDailyEarnings.setText(f"Daily Earnings : {self.dailyEarnings}")
        self.labelDailyEarnings.resize(200,75)
        self.labelDailyEarnings.move(0,465)

        
        self.btnSaleHistory = QPushButton("Sale History", self)
        self.btnSaleHistory.setStyleSheet("background-color:#a8dadc; font-size:20px; color:#023047;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.btnSaleHistory.resize(200,75)
        self.btnSaleHistory.move(760,465)
        self.btnSaleHistory.clicked.connect(self.saleHis)

    def addProductWindow(self):
        self.addProductWindow = addProductWindow()
        self.addProductWindow.show()
        self.hide()

    def saleHis(self):
        self.saleWind = salesHistoryPage()
        self.saleWind.show()
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