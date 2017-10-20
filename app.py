import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reads image in gray scale 
# img=cv2.imread('beti.jpg' , cv2.IMREAD_GRAYSCALE)


# Reads the orignal image without any changes 
img=cv2.imread('beti.jpg' , cv2.IMREAD_UNCHANGED)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()