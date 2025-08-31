# This file contains the data used in the paper where this package was introduced.
# (reference to be added once published)


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
    mcc_values = {
        "C1": [1, -0.5, -0.5],
        "C2": [-0.339, 0.532, -0.194],
        "C3": [-0.309, 0.617, -0.309],
        "C4": [-0.485, -0.424, 0.91]
    }
    r_mcc_values = {
        "C1": [1, -1, -1],
        "C2": [-1, 0.786, -0.571],
        "C3": [-1, 1, -1],
        "C4": [-1, -0.875, 0.938]
    }
    c_purity_values = {
        "C1": [1, -1, -1],
        "C2": [-1, 0.508, -0.968],
        "C3": [-1, 1, -1],
        "C4": [-1, -1, 0.943]
    }
    cluster_colors = {
        "C1": "#D27CCE",
        "C2": "#FF743E",
        "C3": "#00B7DA",
        "C4": "#68AD36"
    }
    plot_dataset_cluster_profile_charts(
        mcc_values=mcc_values,
        r_mcc_values=r_mcc_values,
        c_purity_values=c_purity_values,
        cluster_colors=cluster_colors,
        class_names=class_names,
        class_colors=class_colors,
        export_path="demo_data/paper_figures/exp1/",
        exclude_absent_classes=False,
        bar_text=True
    )

def exp2():
    class_names = ["cp", "im", "imS", "imL",
                   "imU", "om", "omL", "pp"]
    class_colors = ["#FC0014", "#00C9FF", "#8AFF00", "#2700FA",
                    "#6A005F", "#FF9224", "#009900", "#FF69CC"]
    mcc_values = {
        "C1": [0.587, -0.282, -0.04, -0.04, -0.177, -0.13, -0.064, -0.201],
        "C2": [0.522, -0.207, -0.041, -0.041, -0.183, -0.135, -0.066, -0.19],
        "C3": [-0.398, -0.247, 0.05, -0.042, -0.163, 0.431, -0.067, 0.706],
        "C4": [-0.289, 0.568, -0.026, -0.026, -0.05, -0.084, -0.041, -0.144],
        "C5": [-0.446, 0.36, 0.055, 0.055, 0.563, -0.13, -0.064, -0.201],
        "C6": [-0.134, -0.085, -0.012, 0.242, 0.011, 0.043, 0.787, -0.067]
    }
    r_mcc_values = {
        "C1": [0.975, -1, -1, -1, -1, -1, -1, -0.909],
        "C2": [0.838, -0.709, -1, -1, -1, -1, -1, -0.828],
        "C3": [-0.847, -0.83, 0.351, -1, -0.875, 0.935, -1, 0.9],
        "C4": [-1, 0.924, -1, -1, -0.435, -1, -1, -1],
        "C5": [-1, 0.379, 0.366, 0.366, 0.855, -1, -1, -0.909],
        "C6": [-1, -1, -1, 0.488, 0.023, 0.07, 1, -1]
    }
    c_purity_values = {
        "C1": [0.988, -1, -1, -1, -1, -1, -1, -1],
        "C2": [0.641, -1, -1, -1, -1, -1, -1, -1],
        "C3": [-0.975, -0.999, -1, -1, -1, -0.965, -1, 0.293],
        "C4": [-1, 0.843, -1, -1, -1, -1, -1, -1],
        "C5": [-1, -0.53, -1, -1, -0.322, -1, -1, -1],
        "C6": [-1, -1, -1, -1, -1, -1, -0.032, -1]
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
        mcc_values=mcc_values,
        r_mcc_values=r_mcc_values,
        c_purity_values=c_purity_values,
        cluster_colors=cluster_colors,
        class_names=class_names,
        class_colors=class_colors,
        export_path="demo_data/paper_figures/exp2/",
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
    mcc_values = {
        "C1": [0.749, -0.363, -0.386],
        "C2": [-0.143, 0.385, -0.242],
        "C3": [-0.123, -0.421, 0.544],
        "C4": [-0.38, 0.759, -0.38],
        "C5": [-0.26, -0.26, 0.52]
    }
    r_mcc_values = {
        "C1": [0.828, -0.803, -0.852],
        "C2": [-0.591, 0.795, -1],
        "C3": [-0.291, -1, 0.645],
        "C4": [-1, 1, -1],
        "C5": [-1, -1, 1]
    }
    c_purity_values = {
        "C1": [0.848, -0.995, -0.988],
        "C2": [-0.988, 0.87, -1],
        "C3": [-0.924, -1, 0.688],
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
        mcc_values=mcc_values,
        r_mcc_values=r_mcc_values,
        c_purity_values=c_purity_values,
        cluster_colors=cluster_colors,
        class_names=class_names,
        class_colors=class_colors,
        export_path="demo_data/paper_figures/exp3/",
        exclude_absent_classes=False
    )

def exp4():
    class_names = ["c-CS-m", "c-SC-m", "c-CS-s", "c-SC-s",
                   "t-CS-m", "t-SC-m", "t-CS-s", "t-SC-s"]
    class_colors = ["#73C000", "#DF89FF", "#660068", "#00C4FF",
                    "#FF8805", "#FF5584", "#0000FF", "#00BD94"]
    mcc_values = {
        "C1": [0.045, -0.19, 0.219, -0.179, 0.255, -0.179, 0.24, -0.179],
        "C2": [0.354, -0.174, 0.053, -0.118, 0.053, -0.171, 0.185, -0.171],
        "C3": [0.075, -0.187, 0.064, -0.083, 0.127, -0.188, -0.046, 0.239],
        "C4": [-0.187, 0.724, -0.176, -0.176, -0.176, 0.264, -0.144, -0.168],
        "C5": [-0.156, -0.021, -0.146, 0.028, -0.146, 0.103, -0.127, 0.46],
        "C6": [-0.046, -0.046, 0.303, -0.043, -0.043, -0.043, -0.038, -0.043],
        "C7": [-0.123, -0.123, -0.115, 0.657, -0.115, 0.035, -0.1, -0.115],
        "C8": [-0.084, -0.084, -0.079, 0.131, -0.079, 0.342, -0.068, -0.079]

    }
    r_mcc_values = {
        "C1": [0.053, -1, 0.274, -1, 0.32, -1, 0.347, -1],
        "C2": [0.398, -0.961, 0.064, -0.694, 0.064, -1, 0.255, -1],
        "C3": [0.093, -0.933, 0.084, -0.442, 0.168, -1, -0.282, 0.316],
        "C4": [-1, 0.838, -1, -1, -1, 0.324, -0.946, -0.958],
        "C5": [-1, -0.132, -1, 0.029, -1, 0.105, -1, 0.472],
        "C6": [-1, -1, 1, -1, -1, -1, -1, -1],
        "C7": [-1, -1, -1, 0.814, -1, 0.043, -1, -1],
        "C8": [-1, -1, -1, 0.238, -1, 0.619, -1, -1]

    }
    c_purity_values = {
        "C1": [-0.896, -1, -0.559, -1, -0.519, -1, -0.778, -1],
        "C2": [-0.357, -1, -0.875, -0.992, -0.875, -1, -0.709, -1],
        "C3": [-0.756, -1, -0.856, -0.905, -0.821, -1, -0.94, -0.671],
        "C4": [-1, -0.238, -1, -1, -1, -0.57, -1, -1],
        "C5": [-1, -0.888, -1, -0.809, -1, -0.684, -1, -0.135],
        "C6": [-1, -1, 1, -1, -1, -1, -1, -1],
        "C7": [-1, -1, -1, 0.611, -1, -0.901, -1, -1],
        "C8": [-1, -1, -1, -0.77, -1, 0.503, -1, -1]

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
        mcc_values=mcc_values,
        r_mcc_values=r_mcc_values,
        c_purity_values=c_purity_values,
        cluster_colors=cluster_colors,
        class_names=class_names,
        class_colors=class_colors,
        export_path="demo_data/paper_figures/exp4/",
        exclude_absent_classes=False
    )

def exp_network_ans2023():
    class_names = [
        "2",
        "3",
        "4",
        "1"
    ]
    class_colors = [
        "#FFE808",
        "#FF974A",
        "#FF4030",
        "#00AD00"
    ]
    mcc_values = {
        "C1": [0.083, 0.017, -0.075, -0.016],
        "C2": [-0.188, 0.029, 0.484, -0.303],
        "C3": [-0.146, 0.334, 0.11, -0.309],
        "C4": [0.193, -0.325, -0.394, 0.51]

    }
    r_mcc_values = {
        "C1": [0.111, 0.019, -0.25, -0.04],
        "C2": [-1, 0.044, 0.578, -1],
        "C3": [-0.627, 0.41, 0.114, -0.821],
        "C4": [0.34, -0.646, -1, 0.557]

    }
    c_purity_values = {
        "C1": [-0.879, -0.702, -0.973, -0.867],
        "C2": [-1, -0.833, -0.169, -1],
        "C3": [-1, -0.204, -0.847, -1],
        "C4": [-0.981, -0.972, -1, 0.069]
    }
    cluster_colors = {
        "C1": "#80E1DF",
        "C2": "#C2DB7C",
        "C3": "#F9C0E9",
        "C4": "#FDB788"
    }

    plot_dataset_cluster_profile_charts(
        mcc_values=mcc_values,
        r_mcc_values=r_mcc_values,
        c_purity_values=c_purity_values,
        cluster_colors=cluster_colors,
        class_names=class_names,
        class_colors=class_colors,
        export_path="demo_data/paper_figures/ra_network/",
        exclude_absent_classes=False
    )

def run_demo():
    print("Plotting demo data...\n"
          "---------------------")
    exp1()
    exp2()
    exp3()
    exp4()
    exp_network_ans2023()
    print("----------------------------\n"
          "Demo data plotting finished.")

run_demo()