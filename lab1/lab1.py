import cv2

img = cv2.imread('../liverpool_church.jpeg')
cv2.imshow('image', img)

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread('../liverpool_church.jpeg')
plt.imshow(img)
plt.show()

from PIL import Image

img = Image.open('../liverpool_church.jpeg')
img.show()
