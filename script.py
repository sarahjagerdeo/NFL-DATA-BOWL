import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import imageio.v2 as imageio
import pandas as pd
import os

# Load the data
path = '/Users/sarahjagerdeo/Desktop/nfl-big-data-bowl-2025/tracking_week_1.csv'
data = pd.read_csv(path)
games = data['gameId'].unique().tolist()
data = data[data['gameId'] == games[0]]

# Unique times
times = sorted(data['time'].unique().tolist())
names = data['club'].unique().tolist()

# Define colors for each club
colors = np.array([(255, 255, 0), (255, 165, 0), (255, 0, 0)]) / 255
c_map = {names[0]: colors[0], names[1]: colors[1], names[2]: colors[2]}

# Create a function to draw the football field
def draw_football_field(ax):
    ax.plot([0, 120], [0, 0], color='white', linewidth=2)
    ax.plot([0, 120], [53.3, 53.3], color='white', linewidth=2)
    ax.plot([10, 10], [0, 53.3], color='white', linewidth=2)
    ax.plot([110, 110], [0, 53.3], color='white', linewidth=2)
    ax.plot([60, 60], [0, 53.3], color='white', linewidth=2)
    for x in range(20, 110, 10):
        ax.plot([x, x], [0, 53.3], color='white', linestyle='--', linewidth=1)

# Create a directory for frames
output_dir = "frames"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create frames for each unique time
for i, t in enumerate(times):
    if i % 10 == 0:
        datai = data[data['time'] == t].reset_index(drop=True)

        fig, ax = plt.subplots(figsize=(10, 5.5))
        ax.set_facecolor('green')
        draw_football_field(ax)

        # Plot the players' positions
        scatter = ax.scatter(datai['x'], datai['y'], c=datai['club'].map(c_map), s=100)

        ax.set_xlim(0, 120)
        ax.set_ylim(0, 53.3)
        ax.set_title(f'Time: {t}', fontsize=16)
        ax.set_xlabel('X position (yards)', fontsize=12)
        ax.set_ylabel('Y position (yards)', fontsize=12)
        ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
        plt.tight_layout()
        
        # Save the frame
        plt.savefig(f'{output_dir}/frame_{i:06d}.png')
        plt.close(fig)

# Create an animated GIF from saved frames
frames = []
for i in range(len(times)):
    if i % 10 == 0:
        frame = imageio.imread(f'{output_dir}/frame_{i:06d}.png')
        frames.append(frame)

imageio.mimsave('tracking.gif', frames, duration=300)

print("Animated GIF created: tracking.gif")



