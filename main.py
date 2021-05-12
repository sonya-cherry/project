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
        self.setWindowTitle('Теплопроводность')
        self.graph.setText('')
        self.time_input.setText('300')
        self.temp_value.setText('1.1')
        self.temp_deg.setText('4')
        self.min_temp_input.setText('300')
        self.max_temp_input.setText('800')

        self.draw.clicked.connect(self._plot_graph)

    def _plot_graph(self):
        try:
            self.graph.setText('')
            l = float(self.temp_value.text()) * 10 ** -int(self.temp_deg.text())
            T = int(self.time_input.text())
            t_min = int(self.min_temp_input.text())
            t_max = int(self.max_temp_input.text())
            make_plot(l, T, t_min, t_max)
            self._load_gif()
        except ValueError:
            self.graph.setText('Неправильный формат ввода! Попробуйте другие значения')
            return

    def _load_gif(self):
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

    def animate(x):
        line.set_data(np.array(range(len(matrix[0]))), np.array(matrix[x]))
        return line,

    ani = animation.FuncAnimation(
        fig, animate, frames=len(matrix), blit=True, repeat=True, cache_frame_data=False)

    try:
        ani.save('график.gif', writer='imagemagick', fps=30)
    except PermissionError:
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
