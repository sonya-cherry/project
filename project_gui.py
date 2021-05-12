import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


l = 1.1 * 10 ** (-4)
T = 300
t_min = 300
t_max = 800
d_x = 0.01
d_t = d_x ** 2 / (2 * l)
J = round(T / d_t)
K = round(1 / d_x)
matrix = [[0] * K for _ in range(J)]

for j in range(len(matrix[0]) // 2):
    matrix[0][j] = t_min
for j in range(len(matrix[0]) // 2, len(matrix[0])):
    matrix[0][j] = t_max

for i in range(len(matrix)):
    matrix[i][0] = t_min
    matrix[i][len(matrix[0]) - 1] = t_max

for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[0]) - 1):
        matrix[i][j] = (d_t * l / (d_x ** 2)) * (
                matrix[i - 1][j - 1] - 2 * matrix[i - 1][j] + matrix[i - 1][j + 1]) + \
                       matrix[i - 1][j]

fig, ax = plt.subplots()
line, = ax.plot(np.array(range(len(matrix[0]))), np.array(matrix[1]))


def animate(x):
    line.set_data(np.array(range(len(matrix[0]))), np.array(matrix[x]))
    return line,


ani = animation.FuncAnimation(
    fig, animate, frames=len(matrix), blit=True, repeat=True, cache_frame_data=False)

plt.show()
