from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget
from views.editar_proveedores import VentanaProveeores
from PySide2.QtCore import Qt

class EditarProveedores(QWidget, VentanaProveeores):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.Boton_Buscar.clicked.connect(self.buscarProveedor)
        self.Boton_Confirmar.clicked.connect(self.confirmarCambios)

    def buscarProveedor(self):
        print("Boton de buscar, funciona.")
    def confirmarCambios(self):
        print("Boton de cambios, funciona.")