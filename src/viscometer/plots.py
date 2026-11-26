import os

import matplotlib.pyplot as plt
import numpy as np


def parse_stats(fpath: str) -> tuple[float, ...]:
    with open(fpath, "r") as infile:
        stats = tuple(float(line.split(":")[-1]) for line in infile)
    return stats

def plot_sample(key: str, val: dict, fpath):
    _fig, ax = plt.subplots()
    x = val["tds"]
    y = val["average_second_half_dcor"]

    if key != "Water":
        c = np.polyfit(x, y, 1)
        x_ = np.linspace(0, 2, 1001)
        y_ = c[0] * x_ + c[1]
        plt.plot(x_, y_, label=f"{c[0]:.3f}x + {c[1]:.3f}")

    ax.scatter(x, y, c="k", marker="x")
    ax.set_title(f"{key} - TDS vs Y-vel second half of sample")
    ax.set_xlabel("TDS [%]")
    ax.set_ylabel("Y-Velocity [px/ms]")
    ax.legend()
    plt.savefig(os.path.join(fpath, f"{key}-TDS-vel.png"), dpi=300)



def plot_all_data(fpath: str):
    data = {}
    dir = os.listdir(fpath)
    dir = [d for d in dir if os.path.isdir(d)]
    for d in dir:
        print(d)
        with open(os.path.join(d, "sample.txt"), "r") as samplefile:
            sample_type = samplefile.readline().split(":")[1].strip()
            ratio = samplefile.readline()
            ratio = ratio[ratio.find(":") :].strip()
            density = float(samplefile.readline().split(":")[1])
            tds = float(samplefile.readline().split(":")[1]) / 100
            temp_range = [
                float(i) for i in samplefile.readline().split(":")[1].split(",")
            ]

        if sample_type not in data:
            data[sample_type] = {
                "average": [],
                "average_second_half": [],
                "average_dcor": [],
                "average_second_half_dcor": [],
                "tds": [],
                "density": [],
                "temp": [],
            }

        runs = [i for i in os.listdir(os.path.join(fpath, d)) if i.startswith("run")]
        for run in runs:
            subdir = os.path.join(fpath, d, run, "out", "stats.txt")
            # print(subdir)
            avg, avg_half = parse_stats(subdir)
            data[sample_type]["average"].append(avg)
            data[sample_type]["average_dcor"].append(avg / density)
            data[sample_type]["average_second_half"].append(avg_half)
            data[sample_type]["average_second_half_dcor"].append(avg_half / (2.5 - density))
            data[sample_type]["tds"].append(tds * 100)
            data[sample_type]["density"].append(density)
            data[sample_type]["temp"].append(np.average(temp_range))

    plot_sample("Aeropress", data["Aeropress"], fpath)
    plot_sample("V60", data["V60"], fpath)

    fig, ax = plt.subplots()
    x = data["Water"]["temp"]
    y = data["Water"]["average_second_half_dcor"]
    c = np.polyfit(x, y, 1)
    x_ = np.linspace(18, 22, 1001)
    y_ = c[0] * x_ + c[1]
    plt.plot(x_, y_, label=f"{c[0]:.3f}x + {c[1]:.3f}")
    ax.scatter(x, y, c='k', marker='x')
    ax.set_title("Water - temperature vs Y-vel second half of sample")
    ax.set_xlabel("Temperature [ºC]")
    ax.set_ylabel("Y-Velocity [px/ms]")
    ax.legend()
    plt.savefig(os.path.join(fpath, "Water-temp-vel.png"), dpi=300)
