# This file contains the revised cluster profile charts,
# showing the practically attainable values of MCC (the minimum case)
# as described in the revised version of the paper.


from pathlib import Path
from typing import List

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgb


def plot_cluster_profile_chart(
        class_names: List[str],
        class_colors: List[str],
        mcc_values: List[float],
        r_mcc_values: List[float],
        c_purity_values: List[float],
        cluster_color: str,
        export_path: Path | str,
        file_name: str,
        exclude_absent_classes: bool = False,
        measure_threshold_medium: float = 0.4,
        measure_threshold_strong: float = 0.7,
        bar_width: float = 0.3,
        bar_gap: float = 0.03,
        bar_text: bool = False,
        scale_factor: float = 2,
        fig_height: float = 10,
        export_format: str = 'svg'
) -> None:
    """
    Creates Cluster Profile Charts for an Augmented Patient Similarity Network visualization.
    :param class_names: List of category names (groups).
    :param class_colors: List of class color-codes (as hex strings).
    :param mcc_values: List of float values of raw MCC.
    :param r_mcc_values: List of float values of rescaled MCC (rMCC).
    :param c_purity_values: List of float values of Connection Purity (cPurity).
    :param cluster_color: A hex string of the color of the band above the chart denoting cluster membership.
    :param export_path: Path of the desired export folder.
    :param file_name: Export file name.
    :param exclude_absent_classes: (default False) Exclude classes with MCC = -1.
    :param measure_threshold_medium: (default 0.4) Threshold for the "good" relationship.
    :param measure_threshold_strong: (default 0.7) Threshold for the "very good" relationship.
    :param bar_width: adjust width of plot bars.
    :param bar_gap: adjust gap between plot bars.
    :param bar_text: Toggle for rendering cluster name in the cluster membership bad.
    :param scale_factor: adjust how much will figure expand horizontally for each class
    :param fig_height: adjust figure height.
    :param export_format: One of the file extensions supported by matplotlib: png, pdf, ps, eps and svg.
    """

    if not len(class_names) == len(mcc_values) == len(r_mcc_values) == len(c_purity_values) == len(class_colors):
        raise ValueError("Lists of class names, class colors, MCC values, rMCC values, and cPurity values"
                         " must be of the same length.")

    export_path = Path(export_path)
    export_path.mkdir(parents=True, exist_ok=True)

    if exclude_absent_classes:
        filtered_data = [(name, color, mcc, r_mcc, purity) for name, color, mcc, r_mcc, purity in
                         zip(class_names, class_colors, mcc_values, r_mcc_values, c_purity_values) if mcc > -1]

        if not filtered_data:
            print("No valid data to plot.")
            return

        class_names, class_colors, mcc_values, r_mcc_values, c_purity_values = zip(*filtered_data)

    plt.style.use('seaborn-v0_8-darkgrid')
    plot_face_color = '#eaeaf2'
    hatch_styles = [None, 'X']
    fig_width = len(class_names) * scale_factor
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # preparing MCC and cPurity values
    series = ['rMCC', 'cPurity']
    values = np.array([mcc_values, c_purity_values]).T  # Convert to 2D array (rows: classes, columns: series)
    x = np.arange(len(class_names))
    group_centers = []

    for i in range(len(class_names)):
        group_x_positions = []
        for j in range(len(series)):
            bar_x_pos = x[i] + (j - len(series) / 2) * (bar_width + bar_gap)  # Adjust position
            if j == 0:  # underlay mcc (first series) with r_mcc
                bars = ax.bar(bar_x_pos, r_mcc_values[i], bar_width,
                              color="#ffffff",
                              edgecolor='black',
                              linewidth=2,
                              alpha=0.9,
                              zorder=3)
            plt.rcParams.update({'hatch.linewidth': 2})
            bars = ax.bar(bar_x_pos, values[i, j], bar_width,
                          color=class_colors[i],
                          edgecolor='black',
                          hatch=hatch_styles[j],
                          linewidth=2,
                          alpha=0.9,
                          zorder=4)

            group_x_positions.append(bar_x_pos)

        group_center = np.mean(group_x_positions)
        group_centers.append(group_center)

    # Axis settings
    ax.set_ylim((-1.01, 1.15))
    ax.set_yticks([])
    if len(class_names) == 1:
        ax.set_xlim((-1, 0.75))
    ax.set_xticks([])

    # cluster identity indicator band
    ax.axhspan(1.01, 1.2, color=cluster_color, clip_on=False)
    if bar_text:
        r, g, b = to_rgb(cluster_color)
        luminance = 0.2126*r + 0.7152*g + 0.0722*b
        ax.text(
            0.5, 1.025, file_name,
            transform=ax.get_yaxis_transform(),
            ha="center",
            fontsize=50, fontweight="bold",
            color="black" if luminance > 0.5 else "white",
            zorder=6
        )

    # Threshold lines
    # 0 line
    line_width = 14
    ax.axhline(y=0, linewidth=line_width*0.8, color="black", alpha=0.9, zorder=5)
    # positive lines
    ax.axhline(y=measure_threshold_strong, linewidth=line_width, color="tab:green", alpha=0.8, zorder=2)
    ax.axhline(y=measure_threshold_medium, linewidth=line_width, color="tab:red", alpha=0.8, zorder=2)
    # negative lines
    ax.axhline(y=-measure_threshold_strong, linewidth=line_width, color="tab:green", alpha=0.8, zorder=2)
    ax.axhline(y=-measure_threshold_medium, linewidth=line_width, color="tab:red", alpha=0.8, zorder=2)

    # Make gridlines subtle and adjust axes face color
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    ax.set_facecolor(plot_face_color)

    # Export
    fname = export_path / f"{file_name}{'_filtered' if exclude_absent_classes else ''}.{export_format}"
    plt.subplots_adjust(top=1, bottom=0, left=0, right=1)
    plt.savefig(fname=fname, dpi=300)
    print(f"Exported file: {fname}")


def plot_dataset_cluster_profile_charts(
        class_names: List[str],
        class_colors: List[str],
        mcc_values: dict[str, List[float]],
        r_mcc_values: dict[str, List[float]],
        c_purity_values: dict[str, List[float]],
        cluster_colors: dict[str, str],
        export_path: Path | str,
        exclude_absent_classes: bool,
        measure_threshold_medium: float = 0.4,
        measure_threshold_strong: float = 0.7,
        bar_width: float = 0.3,
        bar_gap: float = 0.03,
        bar_text: bool = False,
        scale_factor: float = 2,
        fig_height: float = 10,
        export_format: str = 'svg'
) -> None:
    """
    Generates Cluster Profile Charts for all clusters in a provided dataset.
    :param class_names: List of category names (groups).
    :param class_colors: List of class color-codes (as hex strings).
    :param mcc_values: dict(str, List[float]) where keys = cluster names, values = lists of raw MCC values.
    :param r_mcc_values: dict(str, List[float]) where keys = cluster names, values = lists of rescaled MCC (rMCC) values.
    :param c_purity_values: dict(str, List[float]) where keys = cluster names, values = lists of Connection Purity (cPurity) values.
    :param cluster_colors: dict (str, str) where keys = cluster names, values = hex codes of cluster identity colors.
    :param export_path: Path of the desired export folder.
    :param exclude_absent_classes: (default False) Exclude classes with MCC = -1.
    :param measure_threshold_medium: (default 0.4) Threshold for the "good" relationship.
    :param measure_threshold_strong: (default 0.7) Threshold for the "very good" relationship.
    :param bar_width: adjust width of plot bars.
    :param bar_gap: adjust gap between plot bars.
    :param bar_text: Toggle for rendering cluster name in the cluster membership bad.
    :param scale_factor: adjust how much will figure expand horizontally for each class
    :param fig_height: adjust figure height.
    :param export_format: One of the file extensions supported by matplotlib: png, pdf, ps, eps and svg.
    """
    for key in mcc_values.keys():
        if not mcc_values.keys() == r_mcc_values.keys() == c_purity_values.keys() == cluster_colors.keys():
            raise ValueError("The cluster names must be consistent between mcc_values, r_mcc_values,"
                             " c_purity_values, and cluster_colors.")
        plot_cluster_profile_chart(
            class_names=class_names,
            class_colors=class_colors,
            mcc_values=mcc_values[key],
            r_mcc_values=r_mcc_values[key],
            c_purity_values=c_purity_values[key],
            cluster_color=cluster_colors[key],
            export_path=export_path,
            file_name=key,
            exclude_absent_classes=exclude_absent_classes,
            measure_threshold_medium=measure_threshold_medium,
            measure_threshold_strong=measure_threshold_strong,
            bar_width=bar_width,
            bar_gap=bar_gap,
            bar_text=bar_text,
            scale_factor=scale_factor,
            fig_height=fig_height,
            export_format=export_format
        )
