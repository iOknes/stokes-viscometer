import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from cv2 import imread

import viscometer as vs

if len(sys.argv[1]) < 2:
    raise ValueError("Useage: python example.py [file/folder]")

if os.path.isdir(sys.argv[1]):
    print()
if sys.argv[1].endswith(".tif"):
    print("Argument is single .tif file. Creating histogram.")
    input_img = np.array(imread(sys.argv[1]))
    counts, bins = vs.hist_from_image(np.linalg.norm(input_img, axis=-1))
    fig, ax = plt.subplots(1, 1)
    ax.stairs(counts, bins)
    plt.savefig("histogram.png")
