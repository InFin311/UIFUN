import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QApplication
import random


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generador de números aleatorios")

        self.my_layout = QVBoxLayout()
        self.txt = QLabel("[]")

        self.button = QPushButton("Generar número aleatorio")
        self.button.clicked.connect(self.generate)
        self.my_layout.addWidget(self.txt)
        self.my_layout.addWidget(self.button)

        window = QWidget()
        window.setLayout(self.my_layout)
        self.setCentralWidget(window)

    def generate(self):
        random_number = random.randint(1, 100)

        self.txt.setText(f"[{random_number}]")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()  # Obligatorio (dentro del init o fuera)

    app.exec()
