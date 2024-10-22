from skimage.filters import threshold_local
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Pathto the image")
args = vars(ap.parse_args())
# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)
# instead of manually specifying the threshold value, we canuse adaptive
# thresholding to examine neighborhoods of pixels andadaptively threshold
# each neighborhood -- in this example, we'll calculate themean value
# of the neighborhood area of 25 pixels and threshold basedn that value;
# finally, our constant C is subtracted from the meancalculation (in this
# case 15)
thresh = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 15
)
cv2.imshow("OpenCV Mean Thresh", thresh)
# personally, I prefer the scikit-image adaptive thresholding,it just
# feels a lot more "Pythonic"
T = threshold_local(blurred, 29, offset=5, method="gaussian")
thresh = (blurred < T).astype("uint8") * 255
cv2.imshow("scikit-image Mean Thresh", thresh)
cv2.waitKey(0)


blurred = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Image", image)
# apply basic thresholding -- the first parameter is the image
# we want to threshold, the second value is is our threshold
# check; if a pixel value is greater than our threshold (in this
# case, 200), we set it to be BLACK, otherwise it is WHITE.
(T, threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)
# using normal thresholding (rather than inverse thresholding),
# we can change the last argument in the function to make the coins
# black rather than white.
(T, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
print(T)

cv2.imshow("Threshold Binary", thresh)
# finally, we can visualize only the masked regions in the image
cv2.imshow("Output", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)

# apply Otsu's automatic thresholding -- Otsu's method automatically
# determines the best threshold value `T` for us
(T, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold", threshInv)
print("Otsu's thresholding value: {}".format(T))
# finally, we can visualize only the masked regions in the image
cv2.imshow("Output2", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)

