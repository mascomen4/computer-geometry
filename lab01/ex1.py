from matplotlib import pyplot as plt
import numpy as np

import matplotlib.patches as mpatches

# TODO: Test the script in PyCharm.

# For use in Jupyter Notebook
# %matplotlib inline
plt.style.use('classic')

points = [(-7, -1), (-5, 1), (-5, 0), (1, 2)]
np_points = np.array(points)

def plot_polygons(points):
    # Check if the input array is actually numpy array
    assert type(points).split(".")[0] == "numpy"
    
    # If we have just one Polygon, expand it so we can use it in a loop
    if points.ndim == 2:
        points = np.expand_dims(points, axis=0)
        
    for pol_p in points:
        x = np_points[:, 0]
        y = np_points[:, 1]
        # To chooose (x,y) of the i-th point we write: x,y = np_fig[i, :]

        fig = plt.figure(num=1)
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.set_xlim(left=-8, right=3.1)
        ax1.set_ylim(bottom=-1.5, top=3.1)
        ax1.set_aspect('equal')
        ax1.grid()
        ax1.set_xlabel("X")
        ax1.set_ylabel("Y")

        polygon = mpatches.Polygon(xy=points, closed=True, fill=False, linewidth="2.0", color=(0, 1, 0), hatch='o')
        ax1.add_patch(polygon)

        ax1.scatter(x, y, c="black", s=100, marker="<")

        # Чтобы добавить точки на вершины, мы можем использовать функцию scatter. Также, можно использовать lines.Line2D с
        # указанием маркера.

        fig.savefig('ex1.pdf', format='pdf', bbox_inches='tight', pad_inches=0, dpi=300)
        
plot_polygons()