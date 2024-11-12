import argparse
import cv2
from matplotlib import pyplot as plt
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
# load the image and convert it to grayscale
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# apply histogram equalization to stretch the constrast of our image
eq = cv2.equalizeHist(image)
# show our images -- notice how the constrast of the second image has
# been stretched
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
# matplotlib expects RGB images so convert and then displaythe image
# with matplotlib to avoid GUI conflicts/errors (mainly onmacOS)
plt.figure()
plt.axis("off")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))
# plot the histogram
plt.figure()
plt.title("ori")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])

hist = cv2.calcHist([eq], [0], None, [256], [0, 256])
# matplotlib expects RGB images so convert and then displaythe image
# with matplotlib to avoid GUI conflicts/errors (mainly onmacOS)
plt.figure()
plt.axis("off")
plt.imshow(cv2.cvtColor(eq, cv2.COLOR_GRAY2RGB))
# plot the histogram
plt.figure()
plt.title("eq")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.imshow("Original", image)
cv2.imshow("Histogram Equalization", eq)
cv2.waitKey(0)