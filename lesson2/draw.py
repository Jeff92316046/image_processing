import numpy as np
import cv2
canvas = np.zeros((400, 600, 3), dtype="uint8")
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
# draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
# draw another rectangle, this time we'll make it red and 5 pixels thick
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
# let's draw one last rectangle: blue and filled in
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, 1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
for i in range(0, 25):
# randomly generate a radius size between 5 and 200, generate a random
# color, and then pick a random point on our canvas where the circle
# will be drawn
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size = (3,)).tolist()
    pt = np.random.randint(0, high=300, size = (2,))
    # draw our random circle
    cv2.circle(canvas, tuple(pt), radius, color, -1)
# Show our masterpiece
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

image = cv2.imread("lesson2\giraffe.png")
# draw a circle around my face, two filled in circles covering my eyes, and
# a rectangle surrounding my mouth
print(image.shape)
cv2.circle(image, (172, 129), 90, (0, 0, 255), 2)
cv2.circle(image, (152, 121), 10, (0, 0, 255), -1)
cv2.circle(image, (197, 118), 10, (0, 0, 255), -1)
cv2.rectangle(image, (187, 156), (223, 178), (0, 0, 255), -1)
# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)