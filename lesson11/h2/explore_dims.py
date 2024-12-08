from __future__ import print_function
import conf
from scipy import io
import numpy as np
import argparse
import glob
# construct the argument parser and parse the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True, help="path to the configuration file")
args = vars(ap.parse_args())
# load the configuration file and initialize the list of widths and heights
conf1 = conf.Conf(args["conf"])
widths = []
heights = []
# loop over all annotations paths
for p in glob.glob(conf1["image_annotations"] + "/*.mat"):
# load the bounding box associated with the path and update the width and height
    # lists
    (y, h, x, w) = io.loadmat(p)["box_coord"][0]
    widths.append(w - x)
    heights.append(h - y)
    # compute the average of both the width and height lists
    (avgWidth, avgHeight) = (np.mean(widths), np.mean(heights))
print("[INFO] avg. width: {:.2f}".format(avgWidth))
print("[INFO] avg. height: {:.2f}".format(avgHeight))
print("[INFO] aspect ratio: {:.2f}".format(avgWidth /avgHeight))