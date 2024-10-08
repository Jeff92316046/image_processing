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
cv2.imshow("Original", image)
# images are NumPy arrays, stored as unsigned 8 bit integers --this
# implies that the values of our pixels will be in the range [0,255]; when
# using functions like cv2.add and cv2.subtract, values will beclipped
# to this range, even if the added or subtracted values falloutside the
# range of [0, 255]. Check out an example:
print(f"max of 255: {str(cv2.add(np.uint8([200]),np.uint8([100])))}")
print(f"min of 0: {str(cv2.subtract(np.uint8([50]),np.uint8([100])))}")
# NOTE: if you use NumPy arithmetic operations on these arrays,the value
# will be modulo (wrap around) instead of being clipped to the[0, 255]
# range. This is important to keep in mind when working withimages.
print(f"wrap around: {str(np.uint8([200]) +np.uint8([68]))}")
print(f"wrap around: {str(np.uint8([1]) -np.uint8([251]))}")

M = np.ones(image.shape,dtype="uint8")*75
added = cv2.add(image,M)
print(added[152][61])
cv2.imshow("add",added)

M = np.ones(image.shape,dtype="uint8")*50
subtract = cv2.subtract(image,M)
cv2.imshow("sub",subtract)
cv2.waitKey(0)