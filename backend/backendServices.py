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

def saveAmount(date,amount):
    conn.execute("INSERT INTO AMOUNTHISTORY (DATE,AMOUNT) VALUES (?,?)",(date,amount))
    conn.commit()

def dailyEarnings(date):
    total = 0
    counter = 0
    cursor2 = conn.execute("SELECT * FROM AMOUNTHISTORY ")
    for row2 in cursor2:
        if str(date) == row2[counter]:
            total += int(row2[counter+1])
    return total
