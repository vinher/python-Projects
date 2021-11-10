#Creación de códigos QR Con Python y la librería qrcode
#Para instalar la librería ocupamos el comando
#pip install qrcode[pil]

from qrcode import make

class QrCode():
    def __init__(self):
        self.image = make(input("Ingresa un link: "))
        self.qr_name = input("Nombre del archivo: ")

    def save(self):
        self.image.save(self.qr_name)
    def show(self):
        self.image.show(self.qr_name)

qr = QrCode()
qr.save()
qr.show()
