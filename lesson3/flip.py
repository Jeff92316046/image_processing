import argparse
import cv2
# construct the argument parser and parsethe arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
required=True, help = "Path to the image")
args = vars(ap.parse_args())
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# flip the image horizontally
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)

flipped = cv2.flip(image, 1)
# cv2.imshow("Flipped Horizontally",flipped)
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(flipped, M, (w, h))
flipped = cv2.flip(rotated, 0)
print(flipped[189][441])
cv2.imshow("Flipped Vertically", flipped)

# print(flipped[235][259])
# flip the image vertically
# flipped = cv2.flip(image, 0)
# cv2.imshow("Flipped Vertically", flipped)
# # flip the image along both axes
# flipped = cv2.flip(image, -1)
# cv2.imshow("Flipped Horizontally &Vertically", flipped)
cv2.waitKey(0)