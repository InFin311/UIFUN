import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont


class myWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Sección de ventana y configuración general
        self.setWindowTitle("pico")
        self.setMinimumSize(400, 200)

        # Constructor
        self.button = QPushButton("pico")
        self.label = QLabel("pico")
        self.entry = QLineEdit("pico")

        # Layout y reacción
        box = QVBoxLayout()
        self.button.clicked.connect(self.push_reaction)

        box.addWidget(self.label)
        box.addWidget(self.entry)
        box.addWidget(self.button)

        my_window = QWidget()
        my_window.setLayout(box)
        self.setCentralWidget(my_window)

    def push_reaction(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()
