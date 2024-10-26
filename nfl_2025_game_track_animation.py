import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import os
#from IPython.display import display

path = '/Users/sarahjagerdeo/Desktop/nfl-big-data-bowl-2025/tracking_week_1.csv'
data0=pd.read_csv(path)
games=data0['gameId'].unique().tolist()
data=data0[data0['gameId']==games[0]]
print(data)
#display(data)

times=sorted(data['time'].unique().tolist())
names=data['club'].unique().tolist()
print(names)

colors= np.array([(255,255,0),(255,165,0),(255,0,0)]) / 255 
c_map={names[0]:colors[0],names[1]:colors[1],names[2]:colors[2]}

#data['color']=data['club'].map(c_map)

def draw_football_field(ax):
    
    ax.plot([0, 120], [0, 0], color='white', linewidth=2)
    ax.plot([0, 120], [53.3, 53.3], color='white', linewidth=2)
    ax.plot([10, 10], [0, 53.3], color='white', linewidth=2)
    ax.plot([110, 110], [0, 53.3], color='white', linewidth=2)
    ax.plot([60, 60], [0, 53.3], color='white', linewidth=2)

    ax.axvspan(0, 10, facecolor='blue', alpha=0.2)
    ax.axvspan(110, 120, facecolor='red', alpha=0.2)

    for x in range(20, 110, 10):
        ax.plot([x, x], [0, 53.3], color='white', linestyle='--', linewidth=1)

output_dir = "frames"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i, t in enumerate(times):    
    if i%10==0:
    
        datai = data[data['time'] == t].reset_index(drop=True)

        fig, ax = plt.subplots(figsize=(15, 8))

        ax.set_facecolor('green')
        draw_football_field(ax)

        sns.scatterplot(data=datai, x='x', y='y', hue='club', palette=c_map, ax=ax, s=100)

        ax.set_xlim(0, 120)
        ax.set_ylim(0, 53.3)
        ax.set_title(f'{t}', fontsize=16)
        ax.set_xlabel('X position (yards)', fontsize=12)
        ax.set_ylabel('Y position (yards)', fontsize=12)
        ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
        plt.tight_layout()
        plt.savefig(f'frames/frame_{i:06d}.png')

        if i<=10:
            plt.show()
        else:
            plt.close(fig)

frames = []
for i in range(len(times)):
    if i%10==0:
        frame = Image.open(f'frames/frame_{i:06d}.png')
        frames.append(frame)

frames[0].save('tracking.gif', save_all=True, append_images=frames[1:], duration=300, loop=0)

from IPython.display import Image
Image(open('./tracking.gif','rb').read())

