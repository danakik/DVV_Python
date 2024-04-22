import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox, QMdiArea, QMdiSubWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('lab 9.6')

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        bar = self.menuBar()
        file = bar.addMenu('Файл')

        new_action = QAction('Новий', self)
        new_action.triggered.connect(self.new_file)
        file.addAction(new_action)

        cascade_action = QAction('Каскадом', self)
        cascade_action.triggered.connect(self.cascade)
        file.addAction(cascade_action)

        tile_action = QAction('Плиткою', self)
        tile_action.triggered.connect(self.tile)
        file.addAction(tile_action)

        self.new_file()

    def new_file(self):
        sub = QMdiSubWindow()
        sub.setWidget(QTextEdit())
        self.mdi.addSubWindow(sub)
        sub.show()

    def cascade(self):
        self.mdi.cascadeSubWindows()

    def tile(self):
        self.mdi.tileSubWindows()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
