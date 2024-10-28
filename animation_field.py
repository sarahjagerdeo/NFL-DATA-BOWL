import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import imageio.v2 as imageio

def create_football_field(ax):
    # Create the football field rectangle
    field = patches.Rectangle((0, 0), 120, 53.3, linewidth=2, edgecolor='green', facecolor='green', zorder=0)
    ax.add_patch(field)
    # Draw the yard lines (every 10 yards)
    for yard in range(0, 121, 10):
        plt.axvline(x=yard, color='white', linestyle='--', lw=1.5, zorder=1)
        ax.text(yard, 53.5, str(yard), ha='center', va='center', fontsize=10, color='white', zorder=2)

    ax.set_xlim(0, 120)
    ax.set_ylim(0, 53.3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title('Football Play Animation', fontsize=14)

def plot_player_position(ax, x, y, player_number):
    ax.scatter(x, y, color='red', s=100, zorder=3)
    ax.text(x, y, str(player_number), color='white', ha='center', va='center', fontsize=12, fontweight='bold', zorder=4)


fig, ax = plt.subplots(figsize=(10, 5.5))
create_football_field(ax)

# player movement
player_positions = [
    {'x': 51.06, 'y': 28.55, 'nflid': 35459},
    {'x': 50, 'y': 30, 'nflid': 2},
    {'x': 90, 'y': 15, 'nflid': 3},
    {'x': 110, 'y': 40, 'nflid': 4}
]


frames = []

# Simulate the player movement over 20 frames
for t in range(20):
    ax.cla()
    create_football_field(ax)

    # Update player positions 
    for player in player_positions:
        player['x'] += 5  # Move the player to the right
        plot_player_position(ax, player['x'], player['y'], player['nflid'])

    # Save the current frame
    plt.xlim(0, 120)
    plt.ylim(0, 53.3)
    plt.axis('off')  # Hide axes
    plt.tight_layout()
    plt.draw()
    
    # Save the figure to a temporary file
    plt.savefig('temp_frame.png')
    # Append the frame to the list
    frames.append(imageio.imread('temp_frame.png'))

# Create an animated GIF
imageio.mimsave('football_play.gif', frames, duration=0.2)

# Clean up the temporary frame file
import os
os.remove('temp_frame.png')

print("Animated GIF created: football_play.gif")
