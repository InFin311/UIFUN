import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont


class myWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Sección de ventana y configuración general
        self.setWindowTitle("MyProgram")
        self.setMinimumSize(400, 200)

        # Constructor
        aux = "0123456789/*-+="
        l = []
        for i in aux:
            button_aux = QPushButton(i)
            l += [button_aux]

        self.label = QLabel("HeHe")
        self.entry = QLineEdit("")

        # Layout y reacción
        main_box = QGridLayout()
        box = QVBoxLayout()

        main_box.addWidget(l[0], 0, 0)
        main_box.addWidget(l[1], 0, 1)

        box.addWidget(self.label)
        box.addLayout(main_box)

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
