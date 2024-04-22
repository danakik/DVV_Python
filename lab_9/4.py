import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QSpinBox, QFileDialog, QRadioButton, QHBoxLayout, QProgressBar, QMessageBox
import csv

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Форма для виведення даних')
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.radio_layout = QHBoxLayout()
        self.radio_layout.addWidget(QRadioButton('Студент'))
        self.radio_layout.addWidget(QRadioButton('Дисципліна'))
        self.radio_layout.addWidget(QRadioButton('Оцінка'))
        self.layout.addLayout(self.radio_layout)

        self.pushButton = QPushButton('Вивести інформацію')
        self.pushButton.clicked.connect(self.display_data)
        self.layout.addWidget(self.pushButton)

        self.output = QLineEdit()
        self.layout.addWidget(self.output)

        self.progress_bar = QProgressBar()
        self.layout.addWidget(self.progress_bar)

    def display_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Виберіть файл', '', 'CSV Files (*.csv)')

        if file_path:
            selected_info = ''
            marks = []
            with open(file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                row = next(reader)
                if self.radio_layout.itemAt(0).widget().isChecked():
                    selected_info += row[0] + '\n'
                elif self.radio_layout.itemAt(1).widget().isChecked():
                    selected_info += row[1] + '\n'
                elif self.radio_layout.itemAt(2).widget().isChecked():
                    selected_info += row[2] + '\n'
                    self.progress_bar.setValue(int(row[2]))
            self.output.setText(selected_info)
            QMessageBox.information(self, 'Інформація', 'Дані було успішно виведено!')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
