import os
from argparse import ArgumentParser, BooleanOptionalAction

from viscometer import process_folder


def main():
    ap = ArgumentParser(
        description="Master's thesis Stokes' viscometer data analysis tool"
    )

    ap.add_argument("input_path", help="Folder containing input images")
    ap.add_argument("output_folder", default=".", help="Destination folder for output")
    ap.add_argument("-s", "--show-plot", action=BooleanOptionalAction, default=False, help="Display Matplotlib plot as interactive window")
    ap.add_argument("-dt", "--delta-time", default="6.45", type=bool, help="Delta time between frames (default 6.45ms / 155 fps)")

    args = ap.parse_args()

    if os.path.isdir(args.input_path):
        # process_folder(args.input_path, args.output_folder)
        process_folder(args.input_path, args.output_folder, show_plot=args.show_plot, dt=float(args.delta_time))
    else:
        raise ValueError("Input must be a directory")



if __name__ == "__main__":
    main()
