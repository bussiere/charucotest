from pylibdmtx.pylibdmtx import encode
from PIL import Image
encoded = encode('entermanoir1door1'.encode('utf8'))
#img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
img = img.resize((200,200), Image.ANTIALIAS)
img.save('../assets/datamatrix/dmtxmanoirdoor1.png')

