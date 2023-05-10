
# Hecho por Ricardo Angulo 10-05-2023

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QImage, QColor


class Window(QMainWindow):

    def setDarkMode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0 + amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")

    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 200)

        main_box = QVBoxLayout()
        box1 = QHBoxLayout()
        box2 = QVBoxLayout()
        box3 = QGridLayout()
        box_bottom = QGridLayout()

        box2.addWidget(QLabel("No Imagen"))
        box2.addWidget(QLabel("Texto descripción de imagen"))

        box3.addWidget(QLabel("Atributo 1"), 0, 0)
        box3.addWidget(QLabel("Atributo 2"), 1, 0)
        box3.addWidget(QLabel("Atributo 3"), 2, 0)
        box3.addWidget(QLabel("Atributo 4"), 3, 0)
        box3.addWidget(QLabel("Valor 1"), 0, 1)
        box3.addWidget(QLabel("Valor 2"), 1, 1)
        box3.addWidget(QLabel("Valor 3"), 2, 1)
        box3.addWidget(QLabel("Valor 4"), 3, 1)

        box_bottom.addWidget(QLabel(""), 0, 0)
        box_bottom.addWidget(QLabel(""), 0, 1)
        box_bottom.addWidget(QPushButton("OK"), 0, 2)

        box1.addLayout(box2)
        box1.addLayout(box3)

        main_box.addWidget(QLabel("Nombre Usuario"))
        main_box.addLayout(box1)
        main_box.addLayout(box_bottom)

        my_window = QWidget()
        my_window.setLayout(main_box)
        self.setCentralWidget(my_window)
        self.setDarkMode(my_window)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()
