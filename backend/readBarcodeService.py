import cv2
from pyzbar import pyzbar
import winsound


barcodeList = []

def readBarcode(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcodeText = barcode.data.decode('utf-8')
        if barcodeText not in barcodeList:
            winsound.Beep(1600,400)
            barcodeList.append(barcodeText)
        cv2.rectangle(frame, (x,y), (x+w, h+y), (0,255,0), 2)
    return frame

def generate():

    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()

    while ret:
        
        ret, frame = camera.read()
        frame = readBarcode(frame)
        cv2.imshow('Barcode Redader',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()

generate()
print(barcodeList)