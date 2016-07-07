import matplotlib.pyplot as plt
import numpy.random as rnd
from matplotlib.patches import Ellipse

matplotlib inline


ells = Ellipse(xy=(0,0), width=2, height=2, angle=0.0)


fig = plt.figure(0)
ax = fig.add_subplot(111, aspect='equal')

ax.add_artist(ells)
ells.set_clip_box(ax.bbox)
ells.set_facecolor("red")
ells.set_alpha(0.3)

plt.axvline(0, color="black")
plt.axhline(0, color="black")

sqr = plt.Rectangle(xy=(0,0), width=1, height=1, angle=0.0)

fig = plt.figure(0)
ax = fig.add_subplot(111, aspect='equal')

ax.add_artist(sqr)
sqr.set_alpha(0.3)


ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

plt.show()