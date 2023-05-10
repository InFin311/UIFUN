import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QColor, QFont, QMouseEvent


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
        #  box.addWidget(self.entry)
        box.addWidget(self.button)

        my_window = QWidget()
        my_window.setLayout(box)
        self.setCentralWidget(my_window)

    def push_reaction(self):
        self.entry.setText("")

    # Eventos de mouse
    def mouseMoveEvent(self, ev):
        self.label.setText("The mouse is moving")

    def mousePressEvent(self, a0: QMouseEvent):
        if a0.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Click lef 🤳")
        if a0.button() == Qt.MouseButton.RightButton:
            self.label.setText("Click rit🤳")
        if a0.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Click mid🤳")

    def mouseReleaseEvent(self, a0):
        if a0.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Release lef 🤳")
        if a0.button() == Qt.MouseButton.RightButton:
            self.label.setText("Release rit🤳")
        if a0.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Release mid🤳")
        if a0.button() == Qt.MouseButton.ExtraButton1:
            self.label.setText("Release extra1🤳")

    def mouseDoubleClickEvent(self, a0):
        if a0.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Nice ⭐")

    def keyPressEvent(self, a0):
        self.label.setText(f"La tecla presionada es: {a0.key()}")
        if a0.key() == Qt.Key.Key_W:
            self.label.setText("⬆")
        if a0.key() == Qt.Key.Key_S:
            self.label.setText("⬇")
        if a0.key() == Qt.Key.Key_A:
            self.label.setText("⬅")
        if a0.key() == Qt.Key.Key_D:
            self.label.setText("➡")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()
