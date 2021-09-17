from PIL import Image
from pyzbar.pyzbar import decode

read = decode(Image.open('img/qr.png'))
print(read[0].data)
