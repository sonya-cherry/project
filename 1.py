import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
import matplotlib.animation as animation
from math import sin, pi

l = 1.11 * (10 ** (-4))
d_x = 0.001
d_t = d_x ** 2 / (2* l)
T = 300
T0 = 300
J = round(T / d_t)
K = round(0.1 / d_x)
matrix = [[0] * K for _ in range(J)]

for j in range(len(matrix[0])):
    matrix[0][j] = T0


for i in range(len(matrix)):
    matrix[i][0] = T0 * (1 + 0.5 * abs((sin(i * d_t * (pi / 15)))))
    matrix[i][0] = 1200


for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[0]) - 1):
        matrix[i][j] = (d_t * l / (d_x ** 2)) * (
                matrix[i - 1][j - 1] - 2 * matrix[i - 1][j] + matrix[i - 1][j + 1]) + \
                       matrix[i - 1][j]
    matrix[i][len(matrix[0]) - 1]=matrix[i][len(matrix[0]) - 2]
    print(i)


print(matrix[-2])
line, = plt.plot(np.array(range(len(matrix[0]))), np.array(matrix[1]))


fig, ax = plt.subplots()


def init():
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    return line,


def update(x):
    line.set_data(np.array(range(len(matrix[0]))), np.array(matrix[x]))
    return line,


ani = animation.FuncAnimation(
    fig, update, interval=5, blit=True, frames=range(len(matrix)), repeat=True, init_func=init)

# ani.save('график.gif', writer='imagemagick', fps=30)
plt.show()
