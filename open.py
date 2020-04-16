from PIL import Image
from imtools import get_images as GI
import os

x = GI('/home/name/Downloads/',['.jpg', '.png'])

# croping and save image 
im_two = Image.open(x[1])
box = (100,100,400,400)
work = im_two.copy()
region = work.crop(box)
region.save('region.jpg')

# resize and rotate 
im_three = Image.open(x[2])
new_size = (512, 512)
copy_3 = im_three.copy()
work_3 = copy_3.resize(new_size)
rot_3 = work_3.rotate(45)
rot_3.save('im3.jpg')

# displaying the image 
rot_3.show()