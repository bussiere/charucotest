# import modules
import qrcode
from PIL import Image
 
# taking image which user wants
# in the QR code center

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
 
# taking url or text
url = 'Zombie2'
 
# adding URL or text to QRcode
QRcode.add_data(url)
 
# generating QR code
QRcode.make()
 
# taking color name from user
QRcolor = 'Black'
 
# adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')

QRimg = QRimg.resize((250,250), Image.ANTIALIAS)
QRimg = QRimg.crop((25, 25, 225, 225))
# save the QR code generated
QRimg.save('../assets/qrcode/qrcode_zombie2.png')
 
print('QR code generated!')