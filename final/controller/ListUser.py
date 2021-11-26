from PySide2.QtWidgets import QWidget, QTableWidgetItem,QMessageBox,QAbstractItemView
from PySide2.QtCore import Qt
from views.ListUsuarios import ListUser
from db.PuntoVenta import SelectUser

class ListadoUsuarios(QWidget, ListUser):
      def __init__(self,parent = None):
            super().__init__(parent)
            self.setupUi(self)
            self.setWindowFlag(Qt.Window)
            self.EditarBtn.clicked.connect(self.AbrirEdit)
            self.tableConfi()
            self.ListaroUsuario(SelectUser())
      
      
      def AbrirEdit(self):
            from controller.editarUsuario import editarUsuarios
            selecRow = self.ListaUsuarios.selectedItems()
            if selecRow:
                  idU = int(selecRow[0].text())
                  window = editarUsuarios(self,idU)
                  window.show()
            
            self.ListaUsuarios.clearSelection() 
            
      def tableConfi(self):
            columHeader = ("ID","NOMBRE","USUARIO","CORREO")
            self.ListaUsuarios.setColumnCount(len(columHeader))
            self.ListaUsuarios.setHorizontalHeaderLabels(columHeader)
            
            self.ListaUsuarios.setSelectionBehavior(QAbstractItemView.SelectRows)
            
      
      def ListaroUsuario(self, data):
            self.ListaUsuarios.setRowCount(len(data))
            
            
            for (indexRow, row) in enumerate(data):
                  for(indexCell, cell) in enumerate(row):
                        self.ListaUsuarios.setItem(indexRow,indexCell,QTableWidgetItem(str(cell)))
      
      def selectUser(self):
            pass