import matplotlib.pyplot as plt
import numpy as np
from typing import List
import os


def plot_cluster_profile_chart(
        class_names: List[str],
        class_colors: List[str],
        rMCC_values: List[float],
        cPurity_values: List[float],
        cluster_color: str,
        export_path: str,
        file_name: str,
        exclude_absent_classes: bool = False,
        measure_threshold_medium: float = 0.4,
        measure_threshold_strong: float = 0.7) -> None:
    """
    Creates Cluster Profile Charts for an Augmented Patient Similarity Network visualization.

    :param class_names: List of category names (groups).
    :param class_colors: List of class color-codes (as hex strings).
    :param rMCC_values: List of float values of rescaled MCC (rMCC).
    :param cPurity_values: List of float values of Connection Purity (cPurity).
    :param cluster_color: A color of the horizontal line above the chart denoting cluster membership (as a hex string).
    :param export_path: Path of the desired export folder.
    :param file_name: Export file name.
    :param exclude_absent_classes: (default False) Exclude classes with MCC = -1.
    :param measure_threshold_medium: (default 0.4) Threshold for the "good" relationship.
    :param measure_threshold_strong: (default 0.7) Threshold for the "very good" relationship.
    """

    assert len(class_names) == len(rMCC_values) == len(cPurity_values) == len(class_colors), \
        "Lists of class names, class colors, rMCC values, and cPurity values must be of the same length."

    if exclude_absent_classes:
        filtered_data = [(name, color, mcc, purity) for name, color, mcc, purity in
                         zip(class_names, class_colors, rMCC_values, cPurity_values) if mcc > -1]

        if not filtered_data:
            print("No valid data to plot.")
            return

        class_names, class_colors, rMCC_values, cPurity_values = zip(*filtered_data)

    # Settings for an automatic adjustment of figure width according to the number of classes
    scale_factor = 2  # Controls how much the width expands per class
    fig_width = len(class_names) * scale_factor
    fig_height = 10
    bar_width = 0.3

    plt.style.use('seaborn-v0_8-darkgrid')
    hatch_styles = [None, '//']

    series = ['rMCC', 'cPurity']
    values = np.array([rMCC_values, cPurity_values]).T  # Convert to 2D array (rows: classes, columns: series)
    x = np.arange(len(class_names))

    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    group_centers = []

    for i in range(len(class_names)):
        group_x_positions = []
        for j in range(len(series)):
            bar_x = x[i] + (j - len(series) / 2) * bar_width  # Adjust position
            bars = ax.bar(bar_x, values[i, j], bar_width,
                          color=class_colors[i],
                          edgecolor='black',
                          hatch=hatch_styles[j],
                          linewidth=1,
                          alpha=0.9,
                          zorder=3)
            group_x_positions.append(bar_x)

        group_center = np.mean(group_x_positions)
        group_centers.append(group_center)

    # Axis settings
    ax.set_ylim([-1, 1.15])
    ax.set_yticks([])
    if len(class_names) == 1:
        ax.set_xlim([-1, 0.75])
    ax.set_xticks([])

    # cluster identity indicator band
    ax.axhline(y=1.08   , xmin=0, xmax=1, color=cluster_color, linewidth=50, clip_on=False, solid_capstyle='butt')

    # Threshold lines
    # 0 line
    line_width = 14
    ax.axhline(y=0, linewidth=line_width, color="black", alpha=0.8, zorder=4)
    # positive lines
    ax.axhline(y=measure_threshold_strong, linewidth=line_width, color="tab:green", alpha=0.8, zorder=2)
    ax.axhline(y=measure_threshold_medium, linewidth=line_width, color="tab:red", alpha=0.8, zorder=2)
    # negative lines
    ax.axhline(y=-measure_threshold_strong, linewidth=line_width, color="tab:green", alpha=0.8, zorder=2)
    ax.axhline(y=-measure_threshold_medium, linewidth=line_width, color="tab:red", alpha=0.8, zorder=2)

    # Make gridlines subtle
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

    # Export
    if not os.path.isdir(export_path):
        os.makedirs(export_path)
    plt.subplots_adjust(top=0.99, bottom=0.01, left=0.01, right=0.99)
    fname = (export_path
             + ("/" if export_path[-1] != "/" else "")
             + file_name
             + ("_filtered.svg" if exclude_absent_classes else ".svg"))
    plt.savefig(fname=fname)
    print(f"Exported file: {fname}")


def plot_dataset_cluster_profile_charts(
        class_names: List,
        class_colors: List,
        rMCC_values: dict,
        cPurity_values: dict,
        cluster_colors: dict,
        export_path: str,
        exclude_absent_classes: bool) -> None:
    """
    Generates Cluster Profile Charts for all clusters in a provided dataset.

    :param class_names: List of category names (groups).
    :param class_colors: List of class color-codes (as hex strings).
    :param rMCC_values: dict(str, float) where keys = cluster names, values = values of rescaled MCC (rMCC).
    :param cPurity_values: dict(str, float) where keys = cluster names, values = values of Connection Purity (cPurity).
    :param cluster_colors: dict (str, str) where keys = cluster names, values = hex codes of cluster identity colors.
    :param export_path:Path of the desired export folder.
    :param exclude_absent_classes: (default False) Exclude classes with MCC = -1.
    """
    for key in rMCC_values.keys():
        plot_cluster_profile_chart(
            class_names=class_names,
            class_colors=class_colors,
            rMCC_values=rMCC_values[key],
            cPurity_values=cPurity_values[key],
            cluster_color=cluster_colors[key],
            export_path=export_path,
            file_name=key,
            exclude_absent_classes=exclude_absent_classes
        )