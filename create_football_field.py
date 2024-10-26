import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_football_field():
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 5.5))  # Aspect ratio matches the football field

    # Set field dimensions
    field_length = 120  # in yards (including end zones)
    field_width = 53.3  # in yards

    # Create the football field rectangle
    field = patches.Rectangle((0, 0), field_length, field_width, linewidth=2, edgecolor='green', facecolor='green', zorder=0)
    ax.add_patch(field)

    # Draw the yard lines (every 10 yards)
    for yard in range(0, 121, 10):
        plt.axvline(x=yard, color='white', linestyle='--', lw=1.5, zorder=1)
        ax.text(yard, field_width + 1, str(yard), ha='center', va='center', fontsize=10, color='white', zorder=2)

    # Set axis limits
    ax.set_xlim(0, field_length)
    ax.set_ylim(0, field_width)

    # Set axis labels
    ax.set_xlabel('Yards (0 to 120)', fontsize=12)
    ax.set_ylabel('Yards (0 to 53.3)', fontsize=12)

    # Hide axis ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Set title
    ax.set_title('Football Field', fontsize=14)

    return fig, ax

def plot_player_position(ax, x, y, player_number=None):
    # Plot player position
    ax.scatter(x, y, color='red', s=100, zorder=3)

    # Optionally annotate the player with a number
    if player_number is not None:
        ax.text(x, y, str(player_number), color='white', ha='center', va='center', fontsize=12, fontweight='bold', zorder=4)

# Example usage
fig, ax = create_football_field()

# Example player positions
#Load in the x,y and nflid data csv file
player_positions = [
    {'x': 51.06, 'y': 28.55, 'nflid': 35459},
    {'x': 50, 'y': 30, 'nflid': 2},
    {'x': 90, 'y': 15, 'nflid': 3},
    {'x': 110, 'y': 40, 'nflid': 4}
]

# Plot the player positions
for player in player_positions:
    plot_player_position(ax, player['x'], player['y'], player['nflid'])

# Show the plot
plt.show()


