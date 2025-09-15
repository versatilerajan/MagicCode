# 1+0 = something special for you Rajan
# Run this on Google Colab
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.textpath import TextPath
from matplotlib.patches import PathPatch
from matplotlib.transforms import Affine2D
img_size = 400
fig, ax = plt.subplots(figsize=(12, 6)) 
ax.set_xlim(0, img_size * 2)  
ax.set_ylim(0, img_size)
ax.axis('off')
tp = TextPath((0, 0), "Rajan", size=img_size * 0.6, prop=None)
trans = Affine2D().translate(img_size * 0.15, img_size * 0.2)
tp = trans.transform_path(tp)
grid_size = 8  
x_vals = np.arange(0, img_size * 2, grid_size) 
y_vals = np.arange(0, img_size, grid_size)
xx, yy = np.meshgrid(x_vals, y_vals)
points = np.vstack((xx.flatten(), yy.flatten())).T
inside = tp.contains_points(points)
binary = np.random.choice(['0', '1'], size=points.shape[0])
for p, flag, char in zip(points, inside, binary):
    if flag:
        ax.text(p[0], p[1], char, color='red', fontsize=6, ha='center', va='center', weight='bold')
plt.title("Rajan in Binary Art!", fontsize=16, pad=20)
plt.tight_layout()
plt.show()
