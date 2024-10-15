# import the necessary packages
import cv2, argparse
import numpy as np

# load the image and show it
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
required=True, help = "Path to the image")
args = vars(ap.parse_args())
# load the image and show it
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Dilated {} times".format(i + 1), dilated)
    cv2.waitKey(0)
for i in range(0, 3):
    dilated = cv2.erode(gray.copy(), None, iterations=i + 1)
    cv2.imshow("erode {} times".format(i + 1), dilated)
    cv2.waitKey(0)
cv2.getStructuringElement()