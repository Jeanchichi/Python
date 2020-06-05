from pyzbar.pyzbar import decode
from PIL import Image

d = decode(Image.open("My qrcode.png"))
print(d[0].data.decode())
