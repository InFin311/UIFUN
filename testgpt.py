import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class numerorandom(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.button = QPushButton('Generar número aleatorio')
        self.random_number_label = QLabel('')
        self.button.clicked.connect(self.generate_random_number)

        self.layout.addWidget(self.random_number_label)
        self.layout.addWidget(self.button)

    def generate_random_number(self):
        random_number = random.randint(1, 100)

        self.random_number_label.setText(f'El número aleatorio es: {random_number}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = numerorandom()
    window.show()

    sys.exit(app.exec())