import os
from argparse import ArgumentParser

import matplotlib.pyplot as plt

from viscometer import find_center, load_folder


def main():
    ap = ArgumentParser(description="Tool to plot darkest points in image")

    ap.add_argument("input_path", help="Folder containing input images")

    args = ap.parse_args()

    if os.path.isdir(args.input_path):
        images = load_folder(args.input_path)
        centers = [find_center(i) for i in images]

        plt.plot(centers)
        plt.show()
    else:
        raise ValueError("Input must be a directory")



if __name__ == "__main__":
    main()
