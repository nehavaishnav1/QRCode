import cv2
from pyzbar.pyzbar import decode

cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Set width
cam.set(4, 480)  # Set height

while True:
    success, frame = cam.read()
    
    for barcode in decode(frame):
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        print(f'Type: {barcode_type}, Data: {barcode_data}')

    cv2.imshow("Our QR Code Scanner", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit the loop
        break

cam.release()
cv2.destroyAllWindows()
