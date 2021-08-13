import datetime
from backend import backend

totalAmount = 0
condiditon = True

while condiditon:
    barcodeNumber = int(input("Barcode Number =>  "))

    # if backend.checkBarcode(barcodeNumber):
    #     print("Alredy exist")
    # else:
    #     productName = input("Product Name =>  ")
    #     productAmount = input("Product Amount =>  ")

    #     backend.addProduct(barcodeNumber,productName,productAmount)

    data = backend.getProductWithBarcodeNumber(barcodeNumber)

    productCost = 0

    for row in data:
        print(f"\tProduct Name = {row[1]}\n\tProduct Amount = {row[2]} ₺\n\tBarcode Number = {row[0]}")
        productCost = row[2]
    quantity = int(input("Quantity =>  "))

    totalAmount += quantity*int(productCost)
    print("Total Amount : "+str(totalAmount))
    quitCondition = input("Quit = q ---   ").lower()
    if quitCondition == "q":
        condiditon = False
        print("Total Amount =>  "+str(totalAmount))
        date = datetime.datetime.now().date()
        date = str(date)
        backend.saveAmount(date,totalAmount)
