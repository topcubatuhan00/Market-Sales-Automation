from os import SEEK_CUR
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from backend import backendServices


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('X Market')
        self.setGeometry(450, 250, 960, 540)

        self.setWindowIcon(QIcon('./frontend/icons/market.png'))
        self.setStyleSheet('background-color: #293241')
        self.initUI()

    def initUI(self):
        

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.text1 = QtWidgets.QLabel(self)
        self.text1.setStyleSheet("font-size:20px; color:#fff; border-bottom: 1px solid #fff;")
        self.text1.setAlignment(QtCore.Qt.AlignCenter)
        self.text1.setText("Date")
        self.text1.resize(75,50)
        self.text1.move(320,0)
        self.text2 = QtWidgets.QLabel(self)
        self.text2.setStyleSheet("font-size:20px; color:#fff;border-bottom: 1px solid #fff;")
        self.text2.setAlignment(QtCore.Qt.AlignCenter)
        self.text2.setText("Time")
        self.text2.resize(75,50)
        self.text2.move(455,0)
        self.text3 = QtWidgets.QLabel(self)
        self.text3.setStyleSheet("font-size:20px; color:#fff;border-bottom: 1px solid #fff;")
        self.text3.setAlignment(QtCore.Qt.AlignCenter)
        self.text3.setText("Price")
        self.text3.resize(75,50)
        self.text3.move(575,0)

        self.buttonBackHome = QPushButton("Home", self)
        self.buttonBackHome.setStyleSheet('background-color:#e76f51; color:#e9edc9; font-size:24px; border: 1px solid #293241; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px')
        self.buttonBackHome.resize(100,50)
        self.buttonBackHome.move(0,542)
        self.buttonBackHome.clicked.connect(self.backHome)

        # Show widget
        self.show()
    def backHome(self):
        self.hide()
    def createTable(self):
        # Create table

        self.data = backendServices.getHistory()


        self.tableWidget = QTableWidget()
        self.tableWidget.setStyleSheet("""
                font-size:24px; color:#fff;
                margin-left: 250px;
                margin-top: 75px;
                border: none;
            """)
        header = self.tableWidget.horizontalHeader()
        
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.move(100, 50)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
