# import modules
import pyth.qrcodetest as qrcodetest
from PIL import Image
 
# taking image which user wants
# in the QR code center
Logo_link = '../assets/logo/zombie_logo.png'
 
logo = Image.open(Logo_link)
 
# taking base width
basewidth = 50
 
# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcodetest.QRCode(
    error_correction=qrcodetest.constants.ERROR_CORRECT_H
)
 
# taking url or text
url = 'Zombie1'
 
# adding URL or text to QRcode
QRcode.add_data(url)
 
# generating QR code
QRcode.make()
 
# taking color name from user
QRcolor = 'Black'
 
# adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')
 
# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
QRimg = QRimg.resize((250,250), Image.ANTIALIAS)
QRimg = QRimg.crop((25, 25, 225, 225))
# save the QR code generated
QRimg.save('../assets/qrcode/qrcode_zombie.png')
 
print('QR code generated!')