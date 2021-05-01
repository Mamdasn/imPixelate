import cv2, os
import numpy as np
from imPixelate import pix
 

img_fullname = "assets/lotus.jpg"
img_name, img_ext = os.path.splitext(img_fullname)
 
img = cv2.imread(img_fullname)
img_out = img.copy()

[h, w, d] = img.shape
for i in range(d):
    img_out[:, :, i] = pix(img[:, :, i].copy())
cv2.imwrite(f'{img_name}-pixelate{img_ext}', img_out)




