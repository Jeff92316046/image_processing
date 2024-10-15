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

kernelSizes = [(3, 3), (5, 5), (7, 7)]
# loop over the kernels and apply an "opening" operation to the image
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)
cv2.waitKey(0)

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(kernelSize[0], kernelSize[1]), closing)
cv2.waitKey(0)

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient: ({}, {})".format(kernelSize[0], kernelSize[1]), gradient)
cv2.waitKey(0)
rectKernel =cv2.getStructuringElement(cv2.MORPH_RECT, (40,5))
blackhat = cv2.morphologyEx(gray,
cv2.MORPH_BLACKHAT, rectKernel)
# similarly, a tophat (also called a "whitehat")operation will enable
# us to find light regions on a dark background
tophat = cv2.morphologyEx(gray,cv2.MORPH_TOPHAT, rectKernel)
# show the output images
cv2.imshow("Original", image)
cv2.imshow("Blackhat", blackhat)
cv2.imshow("Tophat", tophat)
cv2.waitKey(0)