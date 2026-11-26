import os
from argparse import ArgumentParser, BooleanOptionalAction

from viscometer import plot_all_data, process_folder


def main():
    ap = ArgumentParser(
        description="Master's thesis Stokes' viscometer data analysis tool"
    )

    ap.add_argument("input_path", help="Folder containing input images")
    ap.add_argument("output_folder", default=".", help="Destination folder for output")
    ap.add_argument(
        "-s",
        "--show-plot",
        action=BooleanOptionalAction,
        default=False,
        help="Display Matplotlib plot as interactive window",
    )
    ap.add_argument(
        "-dt",
        "--delta-time",
        default=5.26,
        type=float,
        help="Delta time between frames (default 5.26ms / 190 fps)",
    )
    ap.add_argument(
        "-i",
        "--interval",
        default=1,
        type=int,
        help="Interval of image to use (every i-th frame) when calculating velocity (default: 1)",
    )

    args = ap.parse_args()

    if os.path.isdir(args.input_path):
        # process_folder(args.input_path, args.output_folder)
        process_folder(
            args.input_path,
            args.output_folder,
            show_plot=args.show_plot,
            dt=float(args.delta_time),
            interval=int(args.interval),
        )
    else:
        raise ValueError("Input must be a directory")


def plot_data():
    ap = ArgumentParser(
        description="Create plots from data (requires file strcture as used in thesis.)"
    )
    ap.add_argument(
        "input_path",
        help="Folder of data, with folders of samples, with run* folders containing out folder",
    )

    args = ap.parse_args()

    if os.path.isdir(args.input_path):
        plot_all_data(args.input_path)
    else:
        raise ValueError("Input must be a directory")


if __name__ == "__main__":
    main()
