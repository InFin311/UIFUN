import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, \
    QGridLayout, QStackedLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont


class myWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Sección de ventana y configuración general
        self.setWindowTitle("MyProgram")
        self.setMinimumSize(400, 200)

        # Constructor
        container0 = QWidget()
        container1 = QWidget()
        container2 = QWidget()
        layout = QVBoxLayout(container0)
        layout1 = QVBoxLayout(container1)
        layout2 = QVBoxLayout(container2)
        self.button0 = QPushButton("0")
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")

        self.button0.clicked.connect(self.click_0)
        self.button1.clicked.connect(self.click_1)
        self.button2.clicked.connect(self.click_2)

        # Layout y reacción

        # Layout 0
        text_login = QLabel("Inicio de sesión")
        form_login = QGridLayout()
        form_login.addWidget(QLabel("Nombre se usuario:"), 0, 0)
        form_login.addWidget(QLineEdit(""), 0, 1)
        form_login.addWidget(QLabel("Contraseña:"), 1, 0)
        pasw = QLineEdit()
        pasw.setEchoMode(QLineEdit.EchoMode.Password)
        form_login.addWidget(pasw, 1, 1)
        button = QPushButton("Iniciar Sesión")
        form_login.addWidget(button, 2, 1)
        button.clicked.connect(self.login)

        layout.addWidget(text_login)
        layout.addLayout(form_login)

        # Layout 1
        text_register = QLabel("Registro de sesión")
        form_register = QGridLayout()
        form_register.addWidget(QLabel("Nombre:"), 0, 0)
        form_register.addWidget(QLineEdit(""), 0, 1)
        form_register.addWidget(QLabel("Apellido:"), 0, 2)
        form_register.addWidget(QLineEdit(""), 0, 3)
        form_register.addWidget(QLabel("Contraseña:"), 1, 0)
        form_register.addWidget(QLineEdit(""), 1, 1)
        form_register.addWidget(QLabel("Contraseña otra vez:"), 1, 2)
        form_register.addWidget(QLineEdit(""), 1, 3)
        form_register.addWidget(QPushButton("Iniciar Sesión"), 2, 3)

        layout1.addWidget(text_register)
        layout1.addLayout(form_register)

        self.main_box = QStackedLayout()
        box_top = QVBoxLayout()
        box_bottom = QHBoxLayout()

        box_bottom.addWidget(self.button0)
        box_bottom.addWidget(self.button1)
        box_bottom.addWidget(self.button2)

        self.main_box.addWidget(container0)
        self.main_box.addWidget(container1)
        self.main_box.addWidget(container2)

        box_top.addLayout(box_bottom)
        box_top.addLayout(self.main_box)

        my_window = QWidget()
        my_window.setLayout(box_top)
        self.setCentralWidget(my_window)

    def click_0(self):
        self.main_box.setCurrentIndex(0)

    def click_1(self):
        self.main_box.setCurrentIndex(1)

    def click_2(self):
        self.main_box.setCurrentIndex(2)

    def login(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()
