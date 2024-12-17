import imutils
import cv2
def crop_ct101_bb(image, bb, padding=10, dstSize=(32, 32)):
    # unpack the bounding box, extract the ROI from teh image, while taking into account
    # the supplied offset
    (y, h, x, w) = bb
    (x, y) = (max(x - padding, 0), max(y - padding, 0))
    roi = image[y:h + padding, x:w + padding]
    # resize the ROI to the desired destination size
    roi = cv2.resize(roi, dstSize, interpolation=cv2.INTER_AREA)
    # return the ROI
    return roi