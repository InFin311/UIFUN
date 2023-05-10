import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, \
    QStackedLayout, QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont


class myWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Sección de ventana y configuración general
        self.setWindowTitle("MyProgram")
        self.setMinimumSize(400, 200)

        # Constructor
        self.button = QPushButton("HeHe")
        self.entry = QLineEdit("")
        self.entry1 = QLineEdit("")

        title = QLabel("aaaaaaaaaaaaaa ")
        mass = QLabel(" kg")
        height = QLabel(" m")
        result = QLabel(" = ")

        # Layout y reacción
        box = QGridLayout()
        main_box = QVBoxLayout()
        self.button.clicked.connect(self.push_reaction)

        box.addWidget(mass, 0, 0)
        box.addWidget(height, 0, 1)
        box.addWidget(self.entry,  1, 0)
        box.addWidget(self.entry1, 1, 1)

        main_box.addWidget(title)
        main_box.addLayout(box)
        main_box.addWidget(self.button)
        main_box.addWidget(result)

        my_window = QWidget()
        my_window.setLayout(main_box)
        self.setCentralWidget(my_window)

    def push_reaction(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()
