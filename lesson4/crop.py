# import the necessary packages
import cv2, argparse
# load the image and show it
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
required=True, help = "Path to the image")
args = vars(ap.parse_args())
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# cropping an image is accomplishedusing simple NumPy array slices --
# let's crop the face from the image
giraffe = image[70:250, 110:230]
cv2.imshow("giraffe", giraffe)
# ...and now let's crop the entire body
people = image[100:350,280:1000]
cv2.imshow("people", people)
# temp1 = image[90:450, 0:290]
# temp2 = image[124:212, 225:380]
# temp3 = image[173:235, 13:81]
# temp4 = image[85:250, 85:220] 
# cv2.imshow("1",temp1)
# cv2.imshow("2",temp2)
# cv2.imshow("3",temp3)
# cv2.imshow("4",temp4)
cv2.waitKey(0)