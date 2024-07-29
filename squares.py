import matplotlib.pyplot as plt
import numpy as np

use_numpy = False
export_instead_of_show = False

# define sample points via one list for the x values and one for the y values
if use_numpy:
    x_values = np.arange(0, 51)
    y_values = x_values**2
else:
    x_values = range(0, 51)
    y_values = [v ** 2 for v in x_values]

# print predefined styles and use one
print(plt.style.available)
plt.style.use("seaborn-v0_8")

# get the figure and the one subplot we use
fig, ax = plt.subplots()

# set the range of the plots axis
ax.axis([0, 51, 0, 51**2])

# change tick-label style
ax.ticklabel_format(style='plain')

# draw graph
ax.plot(x_values, y_values, color='black')

# draw a point of size s at each sample point of the graph
# the color of the points fades according to the y value and the Blues color map
ax.scatter(x_values, y_values, s=20, c=y_values, cmap=plt.cm.Blues)

# adapt plot style
ax.set_title("Square Numbers", fontsize=18)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y = x**2", fontsize=14)
ax.tick_params(labelsize=12)

if export_instead_of_show:
    # save plot to file
    plt.savefig('squares_plot.png', bbox_inches='tight')
else:
    # show the figure in the matpolotlib window
    plt.show()

