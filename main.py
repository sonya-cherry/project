import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

l = 1.11 * (10 ** (-4))
d_x = 0.01
d_t = d_x ** 2 / (2 * l)
T = 900
J = round(T / d_t)
K = round(1 / d_x)
matrix = [[0] * K for _ in range(J)]

for j in range(len(matrix[0]) // 2):
    matrix[0][j] = 300
for j in range(len(matrix[0]) // 2, len(matrix[0])):
    matrix[0][j] = 800

for i in range(len(matrix)):
    matrix[i][0] = 300
    matrix[i][len(matrix[0]) - 1] = 800

for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[0]) - 1):
        matrix[i][j] = (d_t * l / (d_x ** 2)) * (
                matrix[i - 1][j - 1] - 2 * matrix[i - 1][j] + matrix[i - 1][j + 1]) + \
                       matrix[i - 1][j]

ln, = plt.plot(np.array(range(0, 100)), np.array(matrix[1]), 'ro')
fig, ax = plt.subplots()


def init():
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    return ln,


def update(frame):
    ln.set_data(np.array(range(0, 100)), np.array(matrix[frame]))
    return ln,


gif = FuncAnimation(fig, update, frames=range(0, 100),
                    init_func=init, blit=True)

# gif.save('график.gif', writer='imagemagick', fps=30)
plt.show()
