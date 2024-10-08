import numpy as np
import argparse
import cv2
# construct the argument parser and parsethe arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
required=True, help="Path to the image")
args = vars(ap.parse_args())
# load the image and display it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# Masking allows us to focus only on parts ofan image that interest us.
# A mask is the same size as our image, but hasonly two pixel values,
# 0 and 255. Pixels with a value of 0 areignored in the orignal image,
# and mask pixels with a value of 255 are allowed to be kept. For example,
# let's construct a rectangular mask thatdisplays only the person in
# the image
mask = np.zeros(image.shape[:2],dtype="uint8")
cv2.rectangle(mask, (110,80), (220,230), 255, -1)
cv2.imshow("Mask", mask)

# Apply our mask -- notice how only the personin the image is cropped out
masked = cv2.bitwise_and(image, image,mask=mask)
mask1 = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask1, (165, 155), 80, 255, -1)
masked1 = cv2.bitwise_and(image, image, mask=mask1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask1", mask1)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.imshow("Masked", masked1)

cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)