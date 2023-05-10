import sys
from PyQt6 import QtWidgets, uic

from VentanaPrincipal import Ui_VentanaPrincipal

class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso: float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} anios de la especie {self.especie} con {self.peso} Kg."


class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)

        self.obj = obj
        self.pushButton.clicked.connect(self.guardar_mascota)

    def guardar_mascota(self):
        print(self.obj.nombre)

        self.obj.nombre = self.entrada_nombre.text()
        self.obj.especie = self.entrada_especie.text()
        self.obj.edad = self.entrada_edad.text()
        self.obj.peso = self.entrada_peso.text()

        self.entrada_nombre.setText("")
        self.entrada_especie.setText("")
        self.entrada_edad.setValue(0)
        self.entrada_peso.setValue(0)

        print(self.obj.nombre)
        print(self.obj.especie)
        print(self.obj.edad)
        print(self.obj.peso)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana(obj=Mascota("", "", 0, 0))
    vista.show()
    app.exec()