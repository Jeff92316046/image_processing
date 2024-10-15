# import the necessary packages
import cv2, argparse
import numpy as np

# load the image and show it
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True, help = "Path to the image")
args = vars(ap.parse_args())
# load the image and show it
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

kernelSizes = [(3, 3), (9, 9), (15, 15)]
# loop over the kernel sizes and apply an "average" blur to the image
for (kX, kY) in kernelSizes: 
    blurred = cv2.blur(image, (kX,kY))
    cv2.imshow("Average ({},{})".format(kX, kY), blurred)
cv2.waitKey(0)
for (kX, kY) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)
cv2.waitKey(0)
for k in (3, 9, 15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("Median {}".format(k), blurred)
cv2.waitKey(0)