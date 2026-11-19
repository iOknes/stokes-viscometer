import os

import matplotlib.pyplot as plt
import numpy as np
from cv2 import imread, imwrite


def load_folder(folder_path: str) -> list[np.ndarray]:
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


def process_folder(image_folder_path: str, output_path: str, dt: float = 6.45, show_plot=False):
    images = load_folder(image_folder_path)

    mean_img = np.mean(images, axis=0)

    diffs = images - mean_img
    centers = np.array([find_center(diff) for diff in diffs])

    # For x-direction only
    # velocity = np.diff(centers[:, 0]) / dt
    velocity = np.sum(np.diff(centers, axis=0)**2, axis=1)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Write statistics to a file
    with open(os.path.join(output_path, "stats.txt"), 'w') as outfile:
        outfile.write(f"Average velocity: {np.average(velocity):.3f}\n")
        outfile.write(f"Average velocity for second half: {np.average(velocity[len(velocity)//2:]):.3f}\n")

    # Create image with particle tracking points
    track_img = images[0].copy()
    for i in centers:
        track_img[*i.astype(int)] = [0, 0, 255]
    imwrite(os.path.join(output_path, "track.png"), track_img)

    # Plot velocity
    time_series = np.ones_like(velocity)
    time_series[1:] *= dt
    time_series = np.cumsum(time_series)
    time_series[0] = 0

    plt.plot(time_series, velocity, label="Vel")
    plt.xlabel("Time [ms]")
    plt.ylabel("Velocity [px/ms]")
    plt.savefig(os.path.join(output_path, "velocity.png"), dpi=300)
    plt.legend()
    plt.grid()
    if show_plot:
        plt.show()
