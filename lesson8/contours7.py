# import the necessary packages
import numpy as np
import argparse
import cv2
import imutils
def sort_contours(cnts, method="left-to-right"):
# initialize the reverse flag and sort index
    reverse = False
    i = 0
    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-totop":
        reverse = True
    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottomto-top":
        i = 1
    # construct the list of bounding boxes and sort them from top to bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts,boundingBoxes),key=lambda b:b[1][i], reverse=reverse))
    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)
def draw_contour(image, c, i):
# compute the center of the contour area and draw a circle
# representing the center
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # draw the countour number on the image
    cv2.putText(image, "#{}".format(i + 1), (cX - 20, cY),cv2.FONT_HERSHEY_SIMPLEX,1.0, (100, 255, 255), 2)
    # return the image with the contour number drawn o it
    return image
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")
ap.add_argument("-m", "--method", required=True, help="Sorting method")
args = vars(ap.parse_args())
# load the image and initialize the accumulated edge image
image = cv2.imread(args["image"])
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (3, 3), 0)
# image = imutils.auto_canny(blurred)
cv2.imshow("ori", image)
cv2.waitKey(0)
accumEdged = np.zeros(image.shape[:2], dtype="uint8")
# loop over the blue, green, and red channels, respectively
for chan in cv2.split(image):
# blur the channel, extract edges from it, and accumulate the set
# of edges for the image
    chan = cv2.GaussianBlur(chan, (3, 3), 0)
    edged = cv2.Canny(chan, 240, 250)
    accumEdged = cv2.bitwise_or(accumEdged, edged)
    # show the accumulated edge map
cv2.imshow("Edge Map", accumEdged)
cv2.waitKey(0)
# find contours in the accumulated image, keeping only the largest
# ones
cnts= cv2.findContours(accumEdged.copy(),
cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:7]
orig = image.copy()
# loop over the (unsorted) contours and draw them
for (i, c) in enumerate(cnts):
    orig = draw_contour(orig, c, i)
    # show the original, unsorted contour image
    cv2.imshow("Unsorted", orig)
    # sort the contours according to the provided method
(cnts, boundingBoxes) = sort_contours(cnts, method=args["method"])
# loop over the (now sorted) contours and draw them
orig_2 = image.copy()
for (i, c) in enumerate(cnts):
    draw_contour(orig_2, c, i)
# show the output image
cv2.imshow("Sorted", orig_2)
cv2.waitKey(0)
clone = image.copy()
for c in cnts:
# compute the moments of the contour which can be used to compute the
# centroid or "center of mass" of the region
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # draw the center of the contour on the image
    cv2.circle(clone, (cX, cY), 10, (0, 255, 0), -1)
    # show the output image
    cv2.imshow("Centroids", clone)
    cv2.waitKey(0)
clone = image.copy()
for (i, c) in enumerate(cnts):
# compute the area and the perimeter of the contour
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    print("Contour #{} -- area: {:.2f}, perimeter: {:.2f}".format(i + 1, area, perimeter))
    # draw the contour on the image
    cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
    # compute the center of the contour and draw the contour number
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # cv2.putText(clone, "#{}".format(i + 1), (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX,
    # 0.75, (255, 255, 255), 4)
    # show the output image
cv2.imshow("Contours", clone)
cv2.waitKey(0)
clone = image.copy()
# loop over the contours
for c in cnts:
# fit a bounding box to the contour
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(clone, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # show the output image
    cv2.imshow("Bounding Boxes", clone)
    cv2.waitKey(0)
clone = image.copy()

