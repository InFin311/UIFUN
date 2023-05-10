import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, \
    QDialog, QDialogButtonBox, QMessageBox
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont


class MiniWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MiniWindow")
        self.setMinimumSize(200, 100)

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.button = QDialogButtonBox(QBtn)
        self.button.accepted.connect(self.accept)
        self.button.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Ventanita desplegada.."))
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


class myWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Sección de ventana y configuración general
        self.setWindowTitle("MyProgram")
        self.setMinimumSize(400, 200)

        # Constructor
        self.button = QPushButton("HeHe")
        self.label = QLabel("HeHe")
        self.entry = QLineEdit("")

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
        # Comportamientos o modos de ventana:
        # - about
        # - critical
        # - information
        # - question
        # - warning

        button = QMessageBox.critical(
            self, "modo critical", "AAAAAAAAAAAAAAAAAAAAaaaa",
            buttons=QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.NoToAll | QMessageBox.StandardButton.Ignore,
            defaultButton=QMessageBox.StandardButton.Discard
        )

        if button == QMessageBox.StandardButton.Yes:
            print("wha")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()
