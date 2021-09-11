
import sys, sqlite3, datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from backend import backendServices,readBarcodeService

class salesHistoryPage(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('X Market')

        self.setWindowIcon(QIcon('./icons/market.png'))
        self.setStyleSheet('background-color: #DFE7FD')
        self.initUI()
        
        self.showMaximized()
    def initUI(self):

        self.buttonBack = QPushButton('↼',self)
        self.buttonBack.setStyleSheet("background:#DFE7FD;color:000000;border:none; font-size:36px")
        self.buttonBack.resize(55,50)
        self.buttonBack.move(0,0)
        self.buttonBack.clicked.connect(self.close)
        
        self.btnSale = QPushButton('Satış Yap', self)
        self.btnSale.setStyleSheet('background-color:#FDE2E4; border:1px solid #FAD2E1;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px; color:#6c757d; font-weight:bold; font-size:24px')
        self.btnSale.resize(350,100)
        self.btnSale.move(94,340)
        self.btnSale.clicked.connect(self.saleWindow)

        

        self.btnSaleHistory = QPushButton("Satış Geçmişi", self)
        self.btnSaleHistory.setStyleSheet("background-color:#FAD2E1; border:1px solid #FAD2E1;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px; color:#1D3557; font-weight:bold; font-size:24px; opacity:.5")
        self.btnSaleHistory.resize(350,100)
        self.btnSaleHistory.move(94,640)
        
        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.text1 = QtWidgets.QLabel(self)
        self.text1.setStyleSheet("font-size:20px; color:#1D3557;font-weight:bold; border-bottom: 1px solid #1D3557;")
        self.text1.setAlignment(QtCore.Qt.AlignCenter)
        self.text1.setText("Tarih")
        self.text1.resize(75,50)
        self.text1.move(820,50)
        self.text2 = QtWidgets.QLabel(self)
        self.text2.setStyleSheet("font-size:20px; font-weight:bold;color:#1D3557;border-bottom: 1px solid #1D3557;")
        self.text2.setAlignment(QtCore.Qt.AlignCenter)
        self.text2.setText("Saat")
        self.text2.resize(75,50)
        self.text2.move(955,50)
        self.text3 = QtWidgets.QLabel(self)
        self.text3.setStyleSheet("font-size:20px;font-weight:bold; color:#1D3557;border-bottom: 1px solid #1D3557;")
        self.text3.setAlignment(QtCore.Qt.AlignCenter)
        self.text3.setText("Ücret")
        self.text3.resize(75,50)
        self.text3.move(1075,50)


        self.show()
    def addProductWindow(self):
        self.addProductWindow = addProductWindow()
        self.addProductWindow.show()
        self.hide()
    def saleWindow(self):
        self.salePage = MainForm()
        self.salePage.show()
        self.hide()

    def createTable(self):

        self.data = backendServices.getHistory()


        self.tableWidget = QTableWidget()
        self.tableWidget.setStyleSheet("""
                font-size:24px; 
                color:#1D3557;
                margin-left: 750px;
                margin-top: 125px;
                border: none;
                font-weight:bold;
            """)
        header = self.tableWidget.horizontalHeader()
        
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setRowCount(backendServices.getDateQuantity())
        self.tableWidget.setColumnCount(3)
        x = 0
        y = 0
        for self.dat in self.data:
            self.tableWidget.setItem(x, y, QTableWidgetItem("   "+self.dat[0]+"    "))
            y+=1
            self.tableWidget.setItem(x, y, QTableWidgetItem("   "+self.dat[1]+"   "))
            y+=1
            self.tableWidget.setItem(x, y, QTableWidgetItem(f'    {str(self.dat[2])} $    '))
            y = 0
            x+=1

        self.btnAddProd = QPushButton('Ürün Kaydet', self)
        self.btnAddProd.setStyleSheet('background-color:#FDE2E4; border:1px solid #FAD2E1;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px; color:#6c757d; font-weight:bold; font-size:24px; opacity:.5')
        self.btnAddProd.resize(350,100)
        self.btnAddProd.move(94,490)
        self.btnAddProd.clicked.connect(self.addProductWindow)
class addProductWindow(QMainWindow):
    def __init__(self):
        super(addProductWindow, self).__init__()

        self.setWindowTitle('X Market')

        self.setWindowIcon(QIcon('./icons/market.png'))
        self.setStyleSheet('background-color: #DFE7FD')

        self.initUI()
        
        self.showMaximized()

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
        self.buttonBack = QPushButton('↼',self)
        self.buttonBack.setStyleSheet("background:#DFE7FD;color:000000;border:none; font-size:36px")
        self.buttonBack.resize(55,50)
        self.buttonBack.move(0,0)
        self.buttonBack.clicked.connect(self.close)

        self.btnSale = QPushButton('Satış Yap', self)
        self.btnSale.setStyleSheet('background-color:#FDE2E4; border:1px solid #FAD2E1;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px; color:#6c757d; font-weight:bold; font-size:24px')
        self.btnSale.resize(350,100)
        self.btnSale.move(94,340)
        self.btnSale.clicked.connect(self.salePage)

        self.btnAddProd = QPushButton('Ürün Kaydet', self)
        self.btnAddProd.setStyleSheet('background-color:#FAD2E1; border:1px solid #FAD2E1;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px; color:#1D3557; font-weight:bold; font-size:24px; opacity:.5')
        self.btnAddProd.resize(350,100)
        self.btnAddProd.move(94,490)

        self.btnSaleHistory = QPushButton("Satış Geçmişi", self)
        self.btnSaleHistory.setStyleSheet("background-color:#FDE2E4; border:1px solid #FAD2E1;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px; color:#6c757d; font-weight:bold; font-size:24px; opacity:.5")
        self.btnSaleHistory.resize(350,100)
        self.btnSaleHistory.move(94,640)
        self.btnSaleHistory.clicked.connect(self.saleHis)

        self.labelBg = QtWidgets.QLabel(self)
        self.labelBg.setStyleSheet("background-color:#CDDAFD;border-top-right-radius : 40px; border-bottom-left-radius : 40px; border-bottom-right-radius : 40px")
        self.labelBg.resize(1342,900)
        self.labelBg.move(554,82)

        self.labelBarcode = QtWidgets.QLabel(self)
        self.labelBarcode.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;color:#212529;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.labelBarcode.resize(350,75)
        self.labelBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBarcode.setText("Barkod Numarası")
        self.labelBarcode.move(830,309)

        self.labelBarcodeBg = QtWidgets.QLabel(self)
        self.labelBarcodeBg.setStyleSheet("background-color:#EAE4E9;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.labelBarcodeBg.resize(350,75)
        self.labelBarcodeBg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBarcodeBg.move(1270,309)

        self.textBarcode = QtWidgets.QLineEdit(self)
        self.textBarcode.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;color:#212529;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.textBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.textBarcode.resize(275,75)
        self.textBarcode.move(1270,309)

        self.buttonImage = QPushButton('📸',self)
        self.buttonImage.setStyleSheet("background:#EAE4E9;border:none; font-size:36px")
        self.buttonImage.resize(55,50)
        self.buttonImage.move(1558,321)
        self.buttonImage.clicked.connect(self.barcode)

        self.labelProductName = QtWidgets.QLabel(self)
        self.labelProductName.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;color:#212529;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.labelProductName.resize(350,75)
        self.labelProductName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductName.setText("Ürün Adı")
        self.labelProductName.move(830,434)

        self.textProductName = QtWidgets.QLineEdit(self)
        self.textProductName.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;color:#212529;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.textProductName.setAlignment(QtCore.Qt.AlignCenter)
        self.textProductName.resize(350,75)
        self.textProductName.move(1270,434)

        self.labelProductAmount = QtWidgets.QLabel(self)
        self.labelProductAmount.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;color:#212529;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.labelProductAmount.resize(350,75)
        self.labelProductAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductAmount.setText("Ürün Fiyatı")
        self.labelProductAmount.move(830,559)

        self.textProductAmount = QtWidgets.QLineEdit(self)
        self.textProductAmount.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;color:#212529;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.textProductAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.textProductAmount.resize(350,75)
        self.textProductAmount.move(1270,559)

        self.buttonSave = QPushButton('Kaydet',self)
        self.buttonSave.setStyleSheet("background:#99D98C;border:none; font-size:22px; border-bottom-right-radius:40px;")
        self.buttonSave.resize(150,50)
        self.buttonSave.move(1746,932)
        self.buttonSave.clicked.connect(self.save)

    def barcode(self):
        barcodes = readBarcodeService.generate()
        if len(barcodes) != 0:
            self.textBarcode.setText(barcodes[0])
    
    def salePage(self):
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
                    self.productAmount = int(self.textProductAmount.text())

                    if len(self.labelBarcode.text()) == 0 | len(self.labelProductName.text()) == 0 | len(self.labelAmount.text()) == 0:
                        self.warningMessage("Fill in the information completely.")
                    else:
                        backendServices.addProduct(self.barcodeNumber,self.productName,self.productAmount)
                        self.congMessage("Product added successfully")
                        
                except ValueError:
                    self.warningMessage("Fill in the all blanks.")
        else:
            self.warningMessage("Fill in the all blanks.")
        self.textProductName.setText("")
        self.textBarcode.setText("")
        self.textProductAmount.setText("")

    def saleHis(self):
        self.saleHiss = salesHistoryPage()
        self.saleHiss.show()
        self.hide()

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('X Market')

        self.setWindowIcon(QIcon('./icons/market.png'))
        self.setStyleSheet('background-color: #DFE7FD')

        self.initUI()
        
        self.showMaximized()

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
        self.buttonBack = QPushButton('↼',self)
        self.buttonBack.setStyleSheet("background:#DFE7FD;color:000000;border:none; font-size:36px")
        self.buttonBack.resize(55,50)
        self.buttonBack.move(0,0)
        self.buttonBack.clicked.connect(self.close)

        self.btnSale = QPushButton('Satış Yap', self)
        self.btnSale.setStyleSheet('background-color:#FAD2E1; border:1px solid #FAD2E1;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px; color:#1D3557; font-weight:bold; font-size:24px')
        self.btnSale.resize(350,100)
        self.btnSale.move(94,340)

        self.btnAddProd = QPushButton('Ürün Kaydet', self)
        self.btnAddProd.setStyleSheet('background-color:#FDE2E4; border:1px solid #FAD2E1;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px; color:#6c757d; font-weight:bold; font-size:24px; opacity:.5')
        self.btnAddProd.resize(350,100)
        self.btnAddProd.move(94,490)
        self.btnAddProd.clicked.connect(self.addProductWindow)

        self.btnSaleHistory = QPushButton("Satış Geçmişi", self)
        self.btnSaleHistory.setStyleSheet("background-color:#FDE2E4; border:1px solid #FAD2E1;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px; color:#6c757d; font-weight:bold; font-size:24px; opacity:.5")
        self.btnSaleHistory.resize(350,100)
        self.btnSaleHistory.move(94,640)
        self.btnSaleHistory.clicked.connect(self.saleHis)

        self.labelBg = QtWidgets.QLabel(self)
        self.labelBg.setStyleSheet("background-color:#CDDAFD;border-top-right-radius : 40px; border-bottom-left-radius : 40px; border-bottom-right-radius : 40px")
        self.labelBg.resize(1342,900)
        self.labelBg.move(554,82)

        self.labelBarcode = QtWidgets.QLabel(self)
        self.labelBarcode.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;color:#212529;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.labelBarcode.resize(350,75)
        self.labelBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBarcode.setText("Barkod Numarası")
        self.labelBarcode.move(830,137)

        self.labelBarcodeBg = QtWidgets.QLabel(self)
        self.labelBarcodeBg.setStyleSheet("background-color:#EAE4E9;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.labelBarcodeBg.resize(350,75)
        self.labelBarcodeBg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBarcodeBg.move(1270,137)

        self.textBarcode = QtWidgets.QLineEdit(self)
        self.textBarcode.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;color:#212529;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.textBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.textBarcode.resize(275,75)
        self.textBarcode.move(1270,137)

        self.buttonImage = QPushButton('📸',self)
        self.buttonImage.setStyleSheet("background:#EAE4E9;border:none; font-size:36px")
        self.buttonImage.resize(55,50)
        self.buttonImage.move(1558,149)
        self.buttonImage.clicked.connect(self.barcode)

        self.buttonConfirmBarcode1 = QPushButton('√',self)
        self.buttonConfirmBarcode1.setStyleSheet("background:#1D3557;color:#EAE4E9;border:none; font-size:28px;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.buttonConfirmBarcode1.resize(75,75)
        self.buttonConfirmBarcode1.move(1187,268)
        self.buttonConfirmBarcode1.clicked.connect(self.clickConfirmButton)

        # start content area
        
        self.labelProductName = QtWidgets.QLabel(self)
        self.labelProductName.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.labelProductName.resize(350,75)
        self.labelProductName.setText("Ürün Adı")
        self.labelProductName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductName.move(830,385)

        self.labelProductNameText = QtWidgets.QLabel(self)
        self.labelProductNameText.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.labelProductNameText.resize(350,75)
        self.labelProductNameText.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductNameText.move(1270,385)

        self.labelProductAmount = QtWidgets.QLabel(self)
        self.labelProductAmount.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.labelProductAmount.resize(350,75)
        self.labelProductAmount.setText("Ürün Adet/Kilo Fiyatı")
        self.labelProductAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductAmount.move(830,510)

        self.labelProductAmountText = QtWidgets.QLabel(self)
        self.labelProductAmountText.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.labelProductAmountText.resize(350,75)
        self.labelProductAmountText.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductAmountText.move(1270,510)

        self.labelProductQuantity = QtWidgets.QLabel(self)
        self.labelProductQuantity.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.labelProductQuantity.resize(350,75)
        self.labelProductQuantity.setText("Adet")
        self.labelProductQuantity.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProductQuantity.move(830,635)

        self.textProductQuantity = QtWidgets.QLineEdit(self)
        self.textProductQuantity.setStyleSheet("font-weight:bold; font-size:24px;background-color:#EAE4E9;color:#212529;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.textProductQuantity.setAlignment(QtCore.Qt.AlignCenter)
        self.textProductQuantity.resize(350,75)
        self.textProductQuantity.move(1270,635)
        
        # end of content area

        self.buttonConfirmBarcode2 = QPushButton('∴',self)
        self.buttonConfirmBarcode2.setStyleSheet("background:#1D3557;color:#EAE4E9;border:none; font-size:28px;border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px;border-top-left-radius:10px")
        self.buttonConfirmBarcode2.resize(75,75)
        self.buttonConfirmBarcode2.move(1187,769)
        self.buttonConfirmBarcode2.clicked.connect(self.addBasket)

        self.labelPrice = QtWidgets.QLabel(self)
        self.labelPrice.setStyleSheet("font-weight:bold; font-size:24px;background-color:#99D98C;border-bottom-left-radius : 40px; ")
        self.labelPrice.resize(150,50)
        self.labelPrice.setText("0")
        self.labelPrice.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPrice.move(554,932)

        self.buttonConfirmBarcode2 = QPushButton('💵 ÖDE',self)
        self.buttonConfirmBarcode2.setStyleSheet("font-weight:bold; font-size:24px;background-color:#99D98C;border-bottom-right-radius : 40px; ")
        self.buttonConfirmBarcode2.resize(150,50)
        self.buttonConfirmBarcode2.move(1746,932)
        self.buttonConfirmBarcode2.clicked.connect(self.nextClick)

    def barcode(self):
        barcodes = readBarcodeService.generate()
        if len(barcodes) != 0:
            self.textBarcode.setText(barcodes[0])
    
    def addProductWindow(self):
        self.addProductWindow = addProductWindow()
        self.addProductWindow.show()
        self.hide()
    
    def clickConfirmButton(self):
        self.labelProductNameText.setText(" ")
        self.labelProductAmountText.setText(" ")
        if len(str(self.textBarcode.text())) != 0:
            try:
                self.productBarcodeName = self.textBarcode.text()
                data = backendServices.getProductWithBarcodeNumber(self.productBarcodeName)
                
                for row in data:
                    self.productName = row[1]
                    self.productAmount = row[2]
                    self.labelProductNameText.setText(self.productName)
                    self.labelProductAmountText.setText(str(self.productAmount))
            except sqlite3.OperationalError:
                self.warningMessage("Please enter the information correctly and completely.")
        else:
            self.warningMessage("Please enter the information correctly and completely.")

    def addBasket(self):
        try:
            self.quantity = int(self.textProductQuantity.text())
            self.basketTotal = int(self.labelPrice.text())
            
            self.text = str(self.basketTotal + (self.quantity * int(self.labelProductAmountText.text())))
            self.labelPrice.setText(self.text)
            
        except ValueError:
            self.warningMessage("Please enter the information correctly and completely.")
        except AttributeError:
            self.warningMessage("Please enter the information correctly and completely.")

        self.textBarcode.setText(" ")
        self.labelProductNameText.setText(" ")
        self.labelProductAmountText.setText(" ")
        self.textProductQuantity.setText(" ")

    def nextClick(self):
        self.currentAmount = int(self.labelPrice.text())

        if self.currentAmount != 0:
            backendServices.saveAmount(str(datetime.datetime.now().date()),self.currentAmount,str(datetime.datetime.now().strftime("%H:%M")))
            self.congMessage("Transaction completed successfully")

            self.labelPrice.setText("0")
        else:
            self.warningMessage("Please sell first.")
    
    def saleHis(self):
        self.saleHiss = salesHistoryPage()
        self.saleHiss.show()
        self.hide()

def run():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

run()