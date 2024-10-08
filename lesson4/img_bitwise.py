# import the necessary packages
import numpy as np
import cv2
# first, let's draw a rectangle
rectangle = np.zeros((300, 300),dtype = "uint8")
cv2.rectangle(rectangle, (25, 25),(275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)
# secondly, let's draw a circle
circle = np.zeros((300, 300), dtype ="uint8")
cv2.circle(circle, (150, 150), 150, 255,-1)
cv2.imshow("Circle", circle)
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
# A bitwise 'OR' examines every pixel in rectangle and circle. If
# EITHER pixel in rectangle or circle is greater than zero, then
# the output pixel has a value of 255, otherwise it is 0.
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
# The bitwise 'XOR' is identical to the 'OR' function, with one
# exception: both rectangle and circle are not allowed to BOTH
# have values greater than 0.
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
# Finally, the bitwise 'NOT' inverts the values of the pixels. Pixels
# with a value of 255 become 0, and pixels with a value of 0become
# 255.
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)

cv2.waitKey(0)