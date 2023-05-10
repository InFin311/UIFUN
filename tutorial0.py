
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLayout, QLineEdit, QPushButton, QMainWindow
from PyQt6.QtGui import QColor


class fefeVentana(QMainWindow):

    def setDarkMode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0 + amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ultrapoto")
        self.setMinimumSize(300, 200)

        self.label = QLabel("ultrapoto")
        self.boton1 = QPushButton("ultrapoto")
        self.entry = QLineEdit("ultrapoto")
        self.counter = 5

        self.boton1.clicked.connect(self.mi_funcion)

        box = QVBoxLayout()

        box.addWidget(self.label)
        box.addWidget(self.entry)
        box.addWidget(self.boton1)

        my_window = QWidget()
        my_window.setLayout(box)
        self.setDarkMode(my_window)
        self.setDarkMode(self.entry)
        self.setDarkMode(self.boton1, 70)
        self.setCentralWidget(my_window)

    def mi_funcion(self):
        self.label.setText(str(self.counter))
        self.counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = fefeVentana()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()
