import pyqrcode
import png
from pyqrcode import QRCode

# Conteúdo do QR Code.
content = 'https://github.com/EnricoGregorio'

# Converte o Conteúdo em um QR Code.
convert = pyqrcode.create(content)

count = 0

# Cria um arquivo PNG do QR Code.
convert.png(r'qr.png', scale=8)
