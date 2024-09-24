# import the necessary packages
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-s", "--save", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
print("width: %d pixels" % (image.shape[1]))
print("height: %d pixels" % (image.shape[0]))
print("channels: %d" % (image.shape[2]))
# show the image and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.imwrite(args["save"], image)