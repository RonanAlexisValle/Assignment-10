import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime

#import camera
picture = cv2.VideoCapture(0)
picture.set(3, 640) #width
picture.set (4, 480) #height

while True:
    success, img = picture.read()
    for barcode in decode(img):
        insideqr = barcode.data.decode("utf-8")

        #add lines to the qrcode
        color = np.array([barcode.polygon], np.int32)
        color = color.reshape((-1,1,2))
        cv2.polylines(img,[color],True,(0,0,255),3)

        #adds date and time to the txtfile
        timedate = datetime.now()
        thedateandtime = timedate.strftime("Time: %H:%M:%S %p %z\nDate: %d %B, %Y")

        #new text file that shows contents inside qrcodes
        textFile = open('Valle.txt', 'w')
        textFile.write(f'{insideqr}\n\n{thedateandtime}')

        cv2.imshow('Result',img)
        if cv2.waitKey(1) == ord('q'):
            break