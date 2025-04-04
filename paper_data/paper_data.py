from cluster_profile_charts import plot_dataset_cluster_profile_charts


def exp1():
    class_names = [
        "Iris-setosa",
        "Iris-versicolor",
        "Iris-virginica"
    ]
    class_colors = [
        "#9A96E5",
        "#F97743",
        "#28B36A"
    ]
    mcc_rescaled_values = {
        "C1": [1, -1, -1],
        "C2": [-1, 0.532, -0.571],
        "C3": [-1, 0.617, -1],
        "C4": [-1, -0.875, 0.91]

    }
    purity_values = {
        "C1": [1, -1, -1],
        "C2": [-1, 0.723, -0.75],
        "C3": [-1, 1, -1],
        "C4": [-1, -0.986, 0.95]
    }
    cluster_colors = {
        "C1": "#D27CCE",
        "C2": "#FF743E",
        "C3": "#00B7DA",
        "C4": "#68AD36"
    }


    plot_dataset_cluster_profile_charts(
        rMCC_values=mcc_rescaled_values,
        cPurity_values=purity_values,
        cluster_colors=cluster_colors,
        class_names=class_names,
        class_colors=class_colors,
        export_path="export/paper_figures/exp1/",
        exclude_absent_classes=False
    )


def exp2():
    class_names = ["cp", "im", "imS", "imL",
                   "imU", "om", "omL", "pp"]
    class_colors = ["#FC0014", "#00C9FF", "#8AFF00", "#2700FA",
                    "#6A005F", "#FF9224", "#009900", "#FF69CC"]
    mcc_rescaled_values = {
        "C1": [0.587, -1, -1, -1, -1, -1, -1, -0.909],
        "C2": [0.522, -0.709, -1, -1, -1, -1, -1, -0.828],
        "C3": [-0.847, -0.83, 0.05, -1, -0.875, 0.431, -1, 0.706],
        "C4": [-1, 0.568, -1, -1, -0.435, -1, -1, -1],
        "C5": [-1, 0.36, 0.055, 0.055, 0.563, -1, -1, -0.909],
        "C6": [-1, -1, -1, 0.242, 0.011, 0.043, 0.787, -1]
    }
    purity_values = {
        "C1": [0.987, -1, -1, -1, -1, -1, -1, -0.923],
        "C2": [0.809, -0.999, -1, -1, -1, -1, -1, -0.997],
        "C3": [-0.68, 0, -0.882, -1, -0.923, -0.733, -1, 0.464],
        "C4": [-1, 0.9, -1, -1, -0.988, -1, -1, -1],
        "C5": [-1, 0.127, -0.992, -0.6, 0.173, -1, -1, -0.8],
        "C6": [-1, -1, -1, -0.923, -0.6, -0.882, 0.333, -1]
    }
    cluster_colors = {
        "C1": "#00CAFF",
        "C2": "#5FC613",
        "C3": "#C686E9",
        "C4": "#2E9072",
        "C5": "#EA8615",
        "C6": "#FF306A"
    }

    plot_dataset_cluster_profile_charts(
        rMCC_values=mcc_rescaled_values,
        cPurity_values=purity_values,
        cluster_colors=cluster_colors,
        class_names=class_names,
        class_colors=class_colors,
        export_path="export/paper_figures/exp2/",
        exclude_absent_classes=False
    )

def exp3():
    class_names = [
        "1",
        "2",
        "3"
    ]
    class_colors = [
        "#F97743",
        "#9A96E5",
        "#28B36A"
    ]
    mcc_rescaled_values = {
        "C1": [0.749, -0.803, -0.852],
        "C2": [-0.591, 0.385, -1],
        "C3": [-0.291, -1, 0.544],
        "C4": [-1, 0.759, -1],
        "C5": [-1, -1, 0.52]
    }
    purity_values = {
        "C1": [0.879, -0.652, -0.586],
        "C2": [-0.636, 0.876, -1],
        "C3": [-0.167, -1, 0.789],
        "C4": [-1, 1, -1],
        "C5": [-1, -1, 1]
    }
    cluster_colors = {
        "C1": "#D97DD8",
        "C2": "#23966F",
        "C3": "#4EED69",
        "C4": "#00C7FF",
        "C5": "#FF7045"
    }

    plot_dataset_cluster_profile_charts(
        rMCC_values=mcc_rescaled_values,
        cPurity_values=purity_values,
        cluster_colors=cluster_colors,
        class_names=class_names,
        class_colors=class_colors,
        export_path="export/paper_figures/exp3/",
        exclude_absent_classes=False
    )

def exp4():
    class_names = ["c-CS-m", "c-SC-m", "c-CS-s", "c-SC-s",
                   "t-CS-m", "t-SC-m", "t-CS-s", "t-SC-s"]
    class_colors = ["#73C000", "#DF89FF", "#660068", "#00C4FF",
                    "#FF8805", "#FF5584", "#0000FF", "#00BD94"]
    mcc_rescaled_values = {
        "C1": [0.045, -1, 0.219, -1, 0.255, -1, 0.24, -1],
        "C2": [0.354, -0.961, 0.053, -0.694, 0.053, -1, 0.185, -1],
        "C3": [0.075, -0.933, 0.064, -0.442, 0.127, -1, -0.282, 0.239],
        "C4": [-1, 0.724, -1, -1, -1, 0.264, -0.946, -0.958],
        "C5": [-1, -0.132, -1, 0.028, -1, 0.103, -1, 0.46],
        "C6": [-1, -1, 0.303, -1, -1, -1, -1, -1],
        "C7": [-1, -1, -1, 0.657, -1, 0.035, -1, -1],
        "C8": [-1, -1, -1, 0.131, -1, 0.342, -1, -1]
    }
    purity_values = {
        "C1": [-0.168, -1, 0.194, -1, 0.461, -1, 0.162, -1],
        "C2": [0.301, -0.882, -0.158, -0.102, 0.07, -1, 0.117, -1],
        "C3": [-0.051, -0.986, -0.02, -0.319, -0.056, -1, 0.166, 0.393],
        "C4": [-1, 0.38, -1, -1, -1, -0.037, -0.882, -0.992],
        "C5": [-1, -0.115, -1, 0.29, -1, 0.143, -1, 0.903],
        "C6": [-1, -1, 1, -1, -1, -1, -1, -1],
        "C7": [-1, -1, -1, 0.807, -1, -0.172, -1, -1],
        "C8": [-1, -1, -1, 0.32, -1, 0.776, -1, -1]
    }
    cluster_colors = {
        "C1": "#FF821B",
        "C2": "#FF6092",
        "C3": "#0307FF",
        "C4": "#7FC800",
        "C5": "#00BA81",
        "C6": "#7F00AA",
        "C7": "#DF93FF",
        "C8": "#00D1FF"
    }

    plot_dataset_cluster_profile_charts(
        rMCC_values=mcc_rescaled_values,
        cPurity_values=purity_values,
        cluster_colors=cluster_colors,
        class_names=class_names,
        class_colors=class_colors,
        export_path="export/paper_figures/exp4/",
        exclude_absent_classes=False
    )

def exp_network_ans2023():
    class_names = ["2", "3", "4", "1"]
    class_colors = ["#FFE808", "#FF974A", "#FF4030", "#00AD00"]
    mcc_rescaled_values = {
        "C1": [0.083, 0.017, -0.25, -0.04],
        "C2": [-1, 0.029, 0.484, -1],
        "C3": [-0.627, 0.334, 0.11, -0.821],
        "C4": [0.193, -0.646, -1, 0.51]
    }
    purity_values = {
        "C1":    [-0.6, -0.256, -0.75, -0.394],
        "C2":    [-1, -0.5, 0.25, -1],
        "C3":    [-0.96, 0.226, -0.467, -0.8],
        "C4":    [-0.855, -0.75, -1, 0.321]
    }
    cluster_colors = {
        "C1": "#80E1DF",
        "C2": "#C2DB7C",
        "C3": "#F9C0E9",
        "C4": "#FDB788"
    }

    plot_dataset_cluster_profile_charts(
        rMCC_values=mcc_rescaled_values,
        cPurity_values=purity_values,
        cluster_colors=cluster_colors,
        class_names=class_names,
        class_colors=class_colors,
        export_path="export/paper_figures/exp5_RA/",
        exclude_absent_classes=False
    )


exp1()
exp2()
exp3()
exp4()
exp_network_ans2023()