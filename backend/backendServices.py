from datetime import date
import sqlite3

conn = sqlite3.connect('barcodes.db')

def addProduct(barcodeNumber,productName,productAmount):
    conn.execute("INSERT INTO DESCRIPTION (BARCODENUMBER,PRODUCTNAME,PRODUCTAMOUNT) VALUES (?,?,?)",(barcodeNumber,productName,productAmount))
    conn.commit()
    
def checkBarcode(barcodeNumber):
    condition = False
    cursor = conn.execute("SELECT BARCODENUMBER FROM DESCRIPTION")
    for row in cursor:
        if barcodeNumber == row[0]:
            condition = True
    return condition

def getProductWithBarcodeNumber(barcodeNumber):
    cursor = conn.execute("SELECT BARCODENUMBER,PRODUCTNAME, PRODUCTAMOUNT FROM DESCRIPTION WHERE BARCODENUMBER = "+str(barcodeNumber))
    return cursor

def saveAmount(date,amount,time):
    conn.execute("INSERT INTO AMOUNTHISTORY (DATE,AMOUNT,TIME) VALUES (?,?,?)",(date,amount,time))
    conn.commit()

def dailyEarnings(date):
    total = 0
    counter = 0
    cursor2 = conn.execute("SELECT * FROM AMOUNTHISTORY ")
    for row2 in cursor2:
        if str(date) == row2[counter]:
            total += int(row2[counter+1])
    return total

def getDateQuantity():
    dates = []
    cursor = conn.execute("SELECT DATE FROM AMOUNTHISTORY")
    for row in cursor:
        dates.append(row[0])
    return len(dates)

def getHistory():
    dates = []
    cursor = conn.execute("SELECT * FROM AMOUNTHISTORY")
    for row in cursor:
        newList = []
        # dates.append[row[0]+"**"+str(row[1])+"**"+row[2]+"**"]
        newList.append(row[0])
        newList.append(row[2])
        newList.append(row[1])
        dates.append(newList)
    return dates
getHistory()
