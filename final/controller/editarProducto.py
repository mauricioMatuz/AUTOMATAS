from PySide2.QtWidgets import QWidget
from views.editar_productos import VentanaEditarProductos
from PySide2.QtCore import Qt

class editarProductos(QWidget, VentanaEditarProductos):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.Boton_GuardarCambios.clicked.connect(self.confirmarCambios)

    def confirmarCambios(self):
        print("Boton de productos, funciona.")
        