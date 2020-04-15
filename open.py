from PIL import Image
from imtools import get_images as GI
import os

pil_im = Image.open('/home/name/Downloads/IMG-20200413-WA0005.jpg')

# pil_im.show()
# if using a home directory file use the sudo command

x = os.listdir('/home/name/Downloads/')

print(x)