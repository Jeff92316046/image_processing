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

# resized = imutils.resize(image, width=200)
# cv2.imshow("Resized via Function1", resized)
# resized2 = imutils.resize(image, width=700)
# cv2.imshow("Resized via Function2", resized2)
resized2 = imutils.resize(image,width=w*2, inter=cv2.INTER_CUBIC )
cv2.imshow("Resized via Function2", resized2)
print(resized2[367][170])
cv2.waitKey(0)
cv2.imwrite("temp.png", resized2)