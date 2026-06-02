import os

# import matplotlib.pyplot as plt
import numpy as np
from cv2 import imread, imwrite


def load_folder(folder_path: str):
    images = []
    folder = os.listdir(folder_path)
    folder = [filename for filename in folder if filename.endswith(".tif")]
    folder.sort()
    for filename in folder:
        image = imread(os.path.join(folder_path, filename))
        images.append(image)
    return images


def image_diff(ref_image: np.ndarray, image: np.ndarray, scale=False):
    ref_image = ref_image.astype(np.int16)
    image = image.astype(np.int16)
    diff = np.abs(ref_image - image)
    if scale:
        diff *= int(255 / diff.max())
    return diff.astype(np.uint8)


def find_center(image: np.ndarray):
    # Extract the first channel (assuming grayscale)
    image = image[:, :, 0]
    return np.average(np.where(image == np.min(image)), axis=1)


def process_folder(
    image_folder_path: str,
    output_path: str,
):
    images = load_folder(image_folder_path)

    mean_img = np.mean(images, axis=0)

    diffs = images - mean_img
    # These two numbers are arbitrary constants that work. Maybe make this a variable…
    centers = [find_center(diff) for diff in diffs]

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # track = mean_img.copy()
    track = images[0].copy()
    for i in centers:
        track[*i.astype(int)] = [0, 0, 255]

    # plt.imshow(track)
    imwrite(os.path.join(output_path, "track.png"), track)
