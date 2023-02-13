
import cv2

import numpy as np

base = './test_cases/inpaint/03'
name = 'honey'

path = f'{base}/{name}.png'


img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, (512, 512))

mask = img[:,:,3]



cv2.imwrite(f'{base}/mask_{name}.jpg', mask)