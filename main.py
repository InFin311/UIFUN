import sys
from PyQt6.QtWidgets import QWidget, QApplication


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.MyUI()

    def MyUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Holaaaaaaaaaaa ☺")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    program0 = Window()
    sys.exit(app.exec())
