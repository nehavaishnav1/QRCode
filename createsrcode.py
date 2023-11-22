from tkinter import Image
import qrcode
from pyzbar.pyzbar import decode
from PIL import image
myqr = qrcode.make("https://www.youtube.com/watch?v=kJQP7kiw5Fk&ab_channel=LuisFonsiVEVO")
myqr.save("myqr.png")
b = decode(Image.open("myqr.png"))
print(b)