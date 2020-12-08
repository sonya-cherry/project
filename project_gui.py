import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic


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
        try:
            self.graph.setText('')
            l = float(self.temp_val.text()) * 10 ** -int(self.temp_deg.text())
            T = int(self.time_input.text())
            t_min = int(self.min_temp_input.text())
            t_max = int(self.max_temp_input.text())
            self.return_values(l, T, t_min, t_max)
        except ValueError:
            self.graph.setText('Неправильный формат ввода! Попробуйте другие значения')
            return

    def return_values(self, l, T, t_min, t_max):
        return l, T, t_min, t_max


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
