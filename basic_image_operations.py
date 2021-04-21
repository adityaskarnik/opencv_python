import numpy as np
import cv2

# # ch2_1
# img = cv2.imread("opencv-logo.png")
# cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.imwrite("output.jpg", img)

# ch2_2 Accessing pixel data of an image
img = cv2.imread("opencv-logo.png", 1)
print(type(img)) # <class 'numpy.ndarray'>
print(len(img)) # 739
print(len(img[0])) # 600 - top row values, that is number of vertical columns
print(len(img[0][0])) # 3 - number of channels found
print(img.shape) # (739, 600, 3)
print(img.dtype) # uint8 - unsigned integer of value 8 - 2**8
print(img[10, 5]) # [255 255 255] - 10th row and 5th column values
print(img[:, :, 0]) # all values containing first channel array in it
print(img.size) # 1330200 - total number of pixels in the image