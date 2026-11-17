import os
from argparse import ArgumentParser

from viscometer import process_folder


def main():
    ap = ArgumentParser(
        description="Master's thesis Stokes' viscometer data analysis tool"
    )

    ap.add_argument("input_path", help="Folder containing input images")
    ap.add_argument("output_folder", default=".", help="Destination folder for output")
    # ap.add_argument(
    #     "-s",
    #     "--scale",
    #     required=False,
    #     help="""Scale factor for image processing, either as pixels per length
    #      (> 0), or length per pixel (< 0).""",
    # )
    # ap.add_argument("-p", "--plot", help="Output plots as PNG files")
    # ap.add_argument("-c", "--csv", help="Output CSV files")
    ap.add_argument("-s", "--show-plot", default="True", type=bool, help="Display Matplotlib plot as interactive window")

    args = ap.parse_args()

    if os.path.isdir(args.input_path):
        process_folder(args.input_path, args.output_folder)
    else:
        raise ValueError("Input must be a directory")

    process_folder(args.input_path, args.output_folder, show_plot=args.show_plot)


if __name__ == "__main__":
    main()
