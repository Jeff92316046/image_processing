from skimage import measure
import numpy as np
import cv2
import argparse
import imutils
# load the license plate image from disk
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
# load the image and convert it to grayscale
image = cv2.imread(args["image"])
# extract the Value component from the HSV color space and apply adaptive thresholding
# to reveal the characters on the license plate
V = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))[2]
thresh = cv2.adaptiveThreshold(V, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV, 17, 3)
# show the images
cv2.imshow("License Plate", image)
cv2.imshow("Thresh", thresh)
# perform connected components analysis on the thresholded images and initialize the
# mask to hold only the "large" components we are interested in
labels = measure.label(thresh, connectivity=2, background=0)
mask = np.zeros(thresh.shape, dtype="uint8")
print("[INFO] found {} blobs".format(len(np.unique(labels))))

for (i, label) in enumerate(np.unique(labels)):
# if this is the background label, ignore it
    if label == 0:
        print("[INFO] label: 0 (background)")
        continue
    # otherwise, construct the label mask to display onlyconnected components for
    # the current label
    print("[INFO] label: {} (foreground)".format(i))
    labelMask = np.zeros(thresh.shape, dtype="uint8")
    labelMask[labels == label] = 255
    numPixels = cv2.countNonZero(labelMask)
    # if the number of pixels in the component issufficiently large, add it to our
    # mask of "large" blobs
    if numPixels > 500 and numPixels < 1500:
        mask = cv2.add(mask, labelMask)
    # show the label mask
    # cv2.imshow("Label", labelMask)
    # cv2.waitKey(0)
clone = image.copy()
cnts = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# loop over the contours
for c in cnts:
# fit a bounding box to the contour
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(clone, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # show the output image
    cv2.imshow("Bounding Boxes", clone)
    # cv2.waitKey(0)
# show the large components in the image
cv2.imshow("Large Blobs", mask)
cv2.waitKey(0)