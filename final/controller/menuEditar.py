from PySide2.QtWidgets import QWidget, QTableWidgetItem,QMessageBox
from PySide2.QtCore import Qt
from views.menu_editar import MenuEditar

class MenuEdit(QWidget,MenuEditar):
      def __init__(self, parent = None) -> None:
            super().__init__(parent)
            self.setupUi(self)
            self.setWindowFlag(Qt.Window)
            self.BotonActivar.clicked.connect(self.EditUsuario)
            
      def EditUsuario(self):
            from controller.ListUser import ListadoUsuarios
            window = ListadoUsuarios(self)
            window.show()
      
      
      def EditProvedooer(self):
            pass
      
      
          