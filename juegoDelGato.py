import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, \
    QPushButton, \
    QDialog, QDialogButtonBox, QMessageBox
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont
from random import randint


class otherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 200)
        layer = QVBoxLayout()
        self.label0 = QLabel(f"WWOAAAAAA LOOOOK : {randint(5, 69)}")
        self.setWindowTitle("Ventana secundaria")
        layer.addWidget(self.label0)

        self.setLayout(layer)


class MiniWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MiniWindow")
        self.setMinimumSize(400, 200)

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.button = QDialogButtonBox(QBtn)
        self.button.accepted.connect(self.accept)
        self.button.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Ventanita desplegada.."))
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


class myWindow(QMainWindow):

    def setDarkMode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0 + amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")

    def __init__(self):
        super().__init__()

        # Sección de ventana y configuración general
        self.setWindowTitle("HeHe")
        self.setMinimumSize(400, 200)

        miniWin = MiniWindow()

        # Constructor
        self.alt_window = otherWindow()
        self.setDarkMode(self.alt_window)
        self.button = QPushButton()
        self.button.clicked.connect(self.push_reaction)

        # Layout y reacción
        box = QVBoxLayout()

        box.addWidget(self.button)

        my_window = QWidget()
        my_window.setLayout(box)
        self.setDarkMode(my_window)
        self.setCentralWidget(my_window)

    def push_reaction(self, window: otherWindow):
        """
        if self.alt_window is None:
            self.alt_window = otherWindow()
            self.alt_window.show()  # Permite desplegar la ventana en la pantalla
        else:
            self.alt_window.close()
            self.alt_window = None
        """
        window.label0.setText("Nombre:")

        if window.isVisible():
            window.hide()
        else:
            window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()
