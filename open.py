from PIL import Image
from imtools import get_images as GI
import os

x = GI('/home/name/Downloads/',['.jpg', '.png'])

pil_im = Image.open(x[1])

box = (100,100,400,400)
work = pil_im.copy()
region = work.crop(box)
region.save('region.jpg')

# displaying the image 
region.show()