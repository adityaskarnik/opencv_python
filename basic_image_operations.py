import numpy as np
import cv2

# # ch2_1
# img = cv2.imread("opencv-logo.png")
# cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.imwrite("output.jpg", img)

# ch2_2 Accessing pixel data of an image
# img = cv2.imread("opencv-logo.png", 1)
# print(type(img)) # <class 'numpy.ndarray'>
# print(len(img)) # 739
# print(len(img[0])) # 600 - top row values, that is number of vertical columns
# print(len(img[0][0])) # 3 - number of channels found
# print(img.shape) # (739, 600, 3)
# print(img.dtype) # uint8 - unsigned integer of value 8 - 2**8
# print(img[10, 5]) # [255 255 255] - 10th row and 5th column values
# print(img[:, :, 0]) # all values containing first channel array in it
# print(img.size) # 1330200 - total number of pixels in the image

# ch2_3 Matrix and Scalar operations
# black = np.zeros([150, 200, 1], 'uint8')
# cv2.imshow("Black", black)
# print(black[0,0,:])
# ones = np.ones([150, 200, 3], 'uint8')
# cv2.imshow("Ones", ones)
# print(ones[0,0,:])
# white = np.ones([150, 200, 3], 'uint16')
# white *= (2**16-1)
# cv2.imshow("White", white)
# print(white[0,0,:])
# color = ones.copy()
# color[:,:] = (255, 0, 0)
# cv2.imshow("Blues", color)
# print(color[0,0,:])
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ch2_4 Image types and color channels
color = cv2.imread("butterfly.jpg", 1)
cv2.imshow("Image", color)
cv2.moveWindow("Image", 0,0)
print(color.shape)
height, width,channels = color.shape
b,g,r = cv2.split(color)
rgb_split = np.empty([height, width*3, 3], 'uint8')
rgb_split[:, 0:width] = cv2.merge([b, b, b])
rgb_split[:, width:width*2] = cv2.merge([g,g,g])
rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])
cv2.imshow("Channels", rgb_split)
cv2.moveWindow("Channels", 0, height)
# hue saturation
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("Split hsv", hsv_split)
cv2.waitKey(0)
cv2.destroyAllWindows()