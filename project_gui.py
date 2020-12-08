import sys
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)
        self._init_ui()

    def _init_ui(self):
        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle('Теплопроводность')
        self.graph.setText('')

        self.draw.clicked.connect(self._plot_graph)

    def _plot_graph(self):
        gif = QMovie('график.gif')
        self.graph.setMovie(gif)
        self.graph.setScaledContents(True)
        gif.start()


def make_plot(l, T, t_min, t_max):
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

    def update(x):
        line.set_data(np.array(range(len(matrix[0]))), np.array(matrix[x]))
        return line,

    ani = animation.FuncAnimation(
        fig, update, interval=5, blit=True, frames=range(len(matrix[0])), repeat=True)

    ani.save('график.gif', writer='ffmpeg', fps=30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
