import os
from sys import argv, exit

import matplotlib.pyplot as plt
import numpy as np
from cv2 import imread


def hist_from_image(image: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    flat_image = image.flatten()
    hist, bin_edges = np.histogram(flat_image, bins=np.arange(256))
    return hist, bin_edges

def find_magnitudes(image_list: list[np.ndarray]) -> list[float]:
    baseline = np.average(image_list[0])
    magnitudes = [np.average(np.array(i), axis=0) / baseline for i in image_list]
    return magnitudes

def plot_magnitudes(fpath: str):
    dir = os.listdir(fpath)
    dir.sort()
    idx = []
    mag = []
    for f in dir:
        print(f"Loadgin file {f}")
        idx.append(int(f[:5]))
        mag.append(np.average(np.array(imread(os.path.join(fpath, f)))))
    plt.plot(idx, mag)
    plt.xlabel("Image index")
    plt.ylabel("Average magnitude of image")
    plt.show()

def plot_magnitudes_sh():
    if len(argv) != 2:
        print("Usage: plot-mag DIR")
        exit()
    plot_magnitudes(argv[1])
