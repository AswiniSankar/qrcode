import pyqrcode
qr="https://pypi.org/project/PyQRCode/"
url=pyqrcode.create(qr)
url.eps('as.eps', scale=2)

