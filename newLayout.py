import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont

# Grid layout


class myWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Sección de ventana y configuración general
        self.setWindowTitle("MyProgram")
        self.setMinimumSize(400, 200)

        # Constructor
        self.button = QPushButton("HeHe")
        self.label = QLabel("HeHe")
        self.entry = QLineEdit("")

        # Layout y reacción
        box = QGridLayout()
        self.button.clicked.connect(self.push_reaction)

        box.addWidget(self.label, 0, 0)
        box.addWidget(self.entry, 1, 0)
        box.addWidget(self.button, 1, 1)

        my_window = QWidget()
        my_window.setLayout(box)
        self.setCentralWidget(my_window)

    def push_reaction(self):
        self.entry.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()
