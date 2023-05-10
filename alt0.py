import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, QLabel, \
    QTextEdit, QLineEdit
from PyQt6.QtCore import QSize, Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Sección para diseño
        self.setWindowTitle("Hola otra ves 😉")
        self.setFixedSize(QSize(500, 500))

        self.txt = QLabel("dddd")
        self.entry = QLineEdit("Enter a value")
        box = QVBoxLayout()

        self.button = QPushButton("Press here")
        self.button.clicked.connect(self.react)

        #  self.setCentralWidget(button)
        #  self.setCentralWidget(button1)

        box.addWidget(self.txt)
        box.addWidget(self.button)
        box.addWidget(self.entry)

        window = QWidget()
        window.setLayout(box)
        self.setCentralWidget(window)

    def react(self):
        try:
            int(self.entry.text())
        except:
            return
        n = int(self.entry.text())

        self.txt.setText(f"El doble de {n} es {n * 2}")
        self.entry.setText(str(n*2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Obligatorio (dentro del init o fuera)

    app.exec()
