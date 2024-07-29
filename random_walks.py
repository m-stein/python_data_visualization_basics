from random import choice
from random import randint
import matplotlib.pyplot as plt
import numpy as np


def length(vector2):
    return np.linalg.norm(vector2)


def normalized(vector2):
    return vector2 / length(vector2)


class RandomWalk:
    def __init__(self, num_points):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
        while len(self.x_values) < self.num_points:
            direction = np.array([choice([0, 1, -1]), choice([0, 1, -1])])
            if length(direction) == 0:
                continue

            step = direction * randint(1, 1001)
            self.x_values.append(self.x_values[-1] + step[0])
            self.y_values.append(self.y_values[-1] + step[1])


rw = RandomWalk(50_000)
fig, ax = plt.subplots(figsize=(20, 9))
ax.set_aspect('equal')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.plot(rw.x_values, rw.y_values, linewidth=2, color="black", zorder=0)
ax.scatter(rw.x_values, rw.y_values, c=range(rw.num_points), cmap=plt.cm.Blues, s=10, edgecolors=None, zorder=1)
ax.scatter(rw.x_values[0], rw.y_values[0], color="green", s=50, zorder=2)
ax.scatter(rw.x_values[-1], rw.y_values[-1], color="red", s=50, zorder=3)
plt.show()
