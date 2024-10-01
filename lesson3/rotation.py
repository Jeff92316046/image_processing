import numpy as np
import argparse
import imutils
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
help="Path to the image")
args = vars(ap.parse_args())
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# grab the dimensions of the image and calculate the center of the image
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)
# rotate our image by 45 degrees
#(cx,cy) rotate center point
M = cv2.getRotationMatrix2D((cX, cY), -30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
print(rotated[335,254])
cv2.imshow("Rotated by 45 Degrees", rotated)
# rotate our image by -90 degrees
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

cv2.waitKey(0)