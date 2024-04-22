import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QColor
import random

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('lab 9.1')

        self.label = QLabel('Це я', self)
        self.label.setGeometry(100, 50, 200, 100)
        self.label.setStyleSheet('font-size: 16pt')

        self.button = QPushButton('Змінити колір', self)
        self.button.setGeometry(50, 120, 200, 50)
        self.button.clicked.connect(self.change_color)

    def change_color(self):
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.label.setStyleSheet('font-size: 16pt; color: {}'.format(color.name()))

app = QApplication(sys.argv)
window = MainWindow()
window.setGeometry(300, 300, 300, 300)
window.show()
sys.exit(app.exec_())
