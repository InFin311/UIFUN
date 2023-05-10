import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QLineEdit
from re import search


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.entry = QLineEdit()
        self.txt = QLabel("Ingrese correo")
        self.button = QPushButton("Ingresar")
        box = QVBoxLayout()
        self.button.clicked.connect(self.verify)

        box.addWidget(self.txt)
        box.addWidget(self.entry)
        box.addWidget(self.button)

        win = QWidget()
        win.setLayout(box)
        self.setCentralWidget(win)

    def verify(self):
        aux = self.entry.text()

        if search(""):
            pass

        if "@" in aux and "." in aux:
            print("nice")
        else:
            print("not nice")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()  # Obligatorio (dentro del init o fuera)

    app.exec()