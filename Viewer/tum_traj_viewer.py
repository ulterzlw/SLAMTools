
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d  # Ensure 3D support is imported
from matplotlib.font_manager import FontProperties

def load_tum_format_trajectory(filename):
    data = pd.read_csv(filename, sep=' ', header=None, names=['timestamp', 'tx', 'ty', 'tz', 'qx', 'qy', 'qz', 'qw'])
    return data

def visualize_final_complete_trajectories_2D(datasets, ax, labels, font):
    markers = ['^', 'o', 's', 'p', '*']
    colors = ['b', 'g', 'r', 'c', 'm']
    linewidth = 1.8
    for i, data in enumerate(datasets):
        ax.plot(data['tx'], data['ty'], color=colors[i], linewidth=linewidth, label=labels[i])
        ax.scatter(data['tx'].iloc[0], data['ty'].iloc[0], c=colors[i], marker=markers[0], s=100)
        ax.scatter(data['tx'].iloc[-1], data['ty'].iloc[-1], c=colors[i], marker=markers[1], s=100)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    for spine in ax.spines.values():
        spine.set_color('black')
        spine.set_linewidth(1.5)
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    ax.set_xlabel('X [m]', fontproperties=font)
    ax.set_ylabel('Y [m]', fontproperties=font)
    ax.set_title('2D Trajectories', fontproperties=font)
    ax.legend(handles=ax.lines + [plt.Line2D([0], [0], color=colors[0], marker=markers[0], linestyle='None', markersize=10, label='Start'),
                                  plt.Line2D([0], [0], color=colors[0], marker=markers[1], linestyle='None', markersize=10, label='End')],
              prop=font, loc='upper right', edgecolor='black', facecolor='none', framealpha=1, markerscale=1.5, frameon=True).get_frame().set_linewidth(1.5)
    ax.axis('equal')

def visualize_final_complete_trajectories_3D(datasets, ax, labels, font):
    markers = ['^', 'o', 's', 'p', '*']
    colors = ['b', 'g', 'r', 'c', 'm']
    linewidth = 1.8
    for i, data in enumerate(datasets):
        ax.plot(data['tx'], data['ty'], data['tz'], color=colors[i], linewidth=linewidth, label=labels[i])
        ax.scatter(data['tx'].iloc[0], data['ty'].iloc[0], data['tz'].iloc[0], c=colors[i], marker=markers[0], s=100)
        ax.scatter(data['tx'].iloc[-1], data['ty'].iloc[-1], data['tz'].iloc[-1], c=colors[i], marker=markers[1], s=100)
    ax.grid(True)
    ax.w_xaxis.pane.fill = False
    ax.w_yaxis.pane.fill = False
    ax.w_zaxis.pane.fill = False
    ax.w_xaxis.pane.set_edgecolor('black')
    ax.w_yaxis.pane.set_edgecolor('black')
    ax.w_zaxis.pane.set_edgecolor('black')
    ax.w_xaxis.pane.set_linewidth(1.5)
    ax.w_yaxis.pane.set_linewidth(1.5)
    ax.w_zaxis.pane.set_linewidth(1.5)
    ax.w_xaxis.line.set_color("black")
    ax.w_xaxis.line.set_linewidth(1.5)
    ax.w_yaxis.line.set_color("black")
    ax.w_yaxis.line.set_linewidth(1.5)
    ax.w_zaxis.line.set_color("black")
    ax.w_zaxis.line.set_linewidth(1.5)
    ax.set_xlabel('X [m]', fontproperties=font)
    ax.set_ylabel('Y [m]', fontproperties=font)
    ax.set_zlabel('Z [m]', fontproperties=font)
    ax.set_title('3D Trajectories', fontproperties=font)
    ax.legend(handles=ax.lines[:len(labels)] + [plt.Line2D([0], [0], color=colors[0], marker=markers[0], linestyle='None', markersize=10, label='Start'),
                                                plt.Line2D([0], [0], color=colors[0], marker=markers[1], linestyle='None', markersize=10, label='End')],
              prop=font, loc='upper left', edgecolor='black', facecolor='none', framealpha=1, markerscale=1.5, frameon=True).get_frame().set_linewidth(1.5)



def visualize_xyz_over_time_adjusted(datasets, labels, font):
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    colors = ['b', 'g', 'r', 'c', 'm']
    linewidth = 1.5

    for i, data in enumerate(datasets):
        axs[0].plot(data['timestamp'], data['tx'], linewidth=linewidth, label=labels[i], color=colors[i])
        axs[1].plot(data['timestamp'], data['ty'], linewidth=linewidth, label=labels[i], color=colors[i])
        axs[2].plot(data['timestamp'], data['tz'], linewidth=linewidth, label=labels[i], color=colors[i])
    axs[0].set_title('X', fontproperties=font)
    axs[1].set_title('Y', fontproperties=font)
    axs[2].set_title('Z', fontproperties=font)
    for ax in axs:
        ax.set_xlabel('Timestamp', fontproperties=font)
        ax.set_ylabel('[m]', fontproperties=font)
        ax.legend(prop=font, edgecolor='black', facecolor='none', framealpha=1, markerscale=1.5, frameon=True).get_frame().set_linewidth(1.5)
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        for spine in ax.spines.values():
            spine.set_color('black')
            spine.set_linewidth(1.5)
        ax.spines['right'].set_visible(True)
        ax.spines['top'].set_visible(True)

    fig.savefig("XYZ_over_time_visualization.pdf", bbox_inches='tight', dpi=300)


def visualize_xyz_over_time_adjusted_v2(datasets, labels, font):
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    colors = ['b', 'g', 'r', 'c', 'm']
    linewidth = 1.5
    for i, data in enumerate(datasets):
        axs[0].plot(data['timestamp'], data['tx'], linewidth=linewidth, label=labels[i], color=colors[i])
        axs[1].plot(data['timestamp'], data['ty'], linewidth=linewidth, label=labels[i], color=colors[i])
        axs[2].plot(data['timestamp'], data['tz'], linewidth=linewidth, label=labels[i], color=colors[i])
    axs[0].set_title('X', fontproperties=font)
    axs[1].set_title('Y', fontproperties=font)
    axs[2].set_title('Z', fontproperties=font)
    for ax in axs:
        ax.set_ylabel('Coordinate [m]', fontproperties=font)
        ax.legend(prop=font, edgecolor='black', facecolor='none', framealpha=1, markerscale=1.5, frameon=True).get_frame().set_linewidth(1.5)
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        for spine in ax.spines.values():
            spine.set_color('black')
            spine.set_linewidth(1.5)
        ax.spines['right'].set_visible(True)
        ax.spines['top'].set_visible(True)
    axs[2].set_xlabel('Timestamp', fontproperties=font)  # Only bottom plot shows x-axis label
    plt.tight_layout()
    return fig


# Adjusted font properties
font = FontProperties()
font.set_family('serif')
font.set_name('Times New Roman')
font.set_size(12)


# Load the data
filename = "sample"
datasets = [load_tum_format_trajectory(filename + "_gnss1_tum_format.txt"),
            load_tum_format_trajectory(filename + "_gnss2_tum_format.txt"),
            load_tum_format_trajectory(filename + "_gnss_sbg_tum_format.txt"),
            load_tum_format_trajectory(filename + "_ins_tum_format.txt")]
labels = ["GNSS1", "GNSS2", "SBG","INS"]

# 过滤空的数据集并更新标签
datasets, labels = zip(*[(data, label) for data, label in zip(datasets, labels) if not data.empty])

# Plot final complete 2D trajectories
fig_2d, ax_2d = plt.subplots(figsize=(8, 6))
visualize_final_complete_trajectories_2D(datasets, ax_2d, labels, font)
plt.tight_layout()

# Plot final complete 3D trajectories
fig_3d = plt.figure(figsize=(8, 6))
ax_3d = fig_3d.add_subplot(111, projection='3d')
visualize_final_complete_trajectories_3D(datasets, ax_3d, labels, font)
plt.tight_layout()

# Visualize x, y, z trajectories over time with adjustments
fig_time = visualize_xyz_over_time_adjusted_v2(datasets, labels, font)
plt.tight_layout()
plt.show()

fig_3d.savefig("3D_trajectory_visualization.pdf", bbox_inches='tight', dpi=300)
fig_2d.savefig("2D_trajectory_visualization.pdf", bbox_inches='tight', dpi=300)
fig_time.savefig("XYZ_over_time_visualization.pdf", bbox_inches='tight', dpi=300)