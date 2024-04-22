import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QSpinBox, QFileDialog
import csv

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('lab 9.2_3')
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.lineEdit_Student = QLineEdit()
        self.lineEdit_Discipline = QLineEdit()
        self.spinBox_Mark = QSpinBox()
        self.spinBox_Mark.setMaximum(5)

        self.layout.addWidget(self.lineEdit_Student)
        self.layout.addWidget(self.lineEdit_Discipline)
        self.layout.addWidget(self.spinBox_Mark)

        self.pushButton = QPushButton('Куди')
        self.pushButton.clicked.connect(self.save_data)
        self.layout.addWidget(self.pushButton)

    def save_data(self):
        student = self.lineEdit_Student.text()
        discipline = self.lineEdit_Discipline.text()
        mark = self.spinBox_Mark.value()

        file_path, _ = QFileDialog.getOpenFileName(self, "Виберіть файл для збереження", "", "CSV Files (*.csv)")

        if file_path:
            with open(file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([student, discipline, mark])

        self.lineEdit_Student.clear()
        self.lineEdit_Discipline.clear()
        self.spinBox_Mark.setValue(0)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
