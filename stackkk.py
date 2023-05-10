import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QStackedLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont


class myWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Sección de ventana y configuración general
        self.setWindowTitle("MyProgram")
        self.setMinimumSize(400, 200)

        # Constructor
        self.button = QPushButton("1")
        self.button1 = QPushButton("2")
        self.button2 = QPushButton("3")
        self.label = QLabel("HeHeaaaaaaaaaaa")
        self.label1 = QLabel("HeHessssssssss")
        self.label2 = QLabel("HeHeddddddddddd")

        # Layout y reacción
        self.box = QStackedLayout()
        box1 = QVBoxLayout()
        box2 = QHBoxLayout()
        self.button.clicked.connect(self.click_0)
        self.button1.clicked.connect(self.click_1)
        self.button2.clicked.connect(self.click_2)

        box2.addWidget(self.button)
        box2.addWidget(self.button1)
        box2.addWidget(self.button2)
        self.box.addWidget(self.label)
        self.box.addWidget(self.label1)
        self.box.addWidget(self.label2)

        box1.addLayout(box2)
        box1.addLayout(self.box)

        my_window = QWidget()
        my_window.setLayout(box1)
        self.setCentralWidget(my_window)

    def click_0(self):
        self.box.setCurrentIndex(0)

    def click_1(self):
        self.box.setCurrentIndex(1)

    def click_2(self):
        self.box.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()
