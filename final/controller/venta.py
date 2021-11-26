from PySide2.QtWidgets import QWidget, QTableWidgetItem,QMessageBox
from PySide2.QtCore import Qt
from views.venta import PrincipalView
from db.PuntoVenta import  BuscarPrecio, BuscarProduct
from controller.dicc import Diccionario


class VentaWindow(QWidget, PrincipalView,Diccionario):
    def __init__(self,parent = None ) -> None:
        self.datas = []
        self.Unuario = []
        self.bandera = True
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.AgregarUsuario.clicked.connect(self.RegistrarUsuario)
        self.AgregarProducto.clicked.connect(self.AgregarProductos)
        self.AddBtn.clicked.connect(self.AgregarProductoVenta)
        self.tableConfig()
        self.Cobrar.clicked.connect(self.Romper)
        self.EditarBtn.clicked.connect(self.Editar)
    
    
    def RegistrarUsuario(self):
        from controller.registro import Registrar
        window = Registrar(self)
        window.show()
    
    def RegistrarProveedor(self):
        pass
    
    def Editar(self):
        from controller.menuEditar import MenuEdit
        window = MenuEdit(self)
        window.show()
    
    def  AgregarProductos(self):
        from controller.producto import Productos
        window = Productos(self)
        window.show()
    
    def EliminarRegistros(self):
        pass
    
    def VentaProducto(self):
        pass
    
    def tableConfig(self):
        columnHeaders = ("Nombre","Codigo","Precio")
        self.ListaProducto.setColumnCount(len(columnHeaders))
        self.ListaProducto.setHorizontalHeaderLabels(columnHeaders)
    
    def AgregarProductoVenta(self,data):
       
        rowPosition = self.ListaProducto.rowCount()
        self.ListaProducto.insertRow(rowPosition)
        codigo = self.BarraCodigo.text()
        data = (codigo)
        
        if BuscarProduct(data):
            self.bandera = True
            valoresData = BuscarProduct(data)
            self.ListaProducto.setItem(rowPosition , 0, QTableWidgetItem(valoresData[0]))
            self.ListaProducto.setItem(rowPosition , 1, QTableWidgetItem(valoresData[1]))
            self.ListaProducto.setItem(rowPosition , 2, QTableWidgetItem("$"+str(valoresData[2])))
            if BuscarPrecio(data):
                totals = BuscarPrecio(data)
                self.Unuario.append("1,"*totals)
                self.Unuario.append("+,")

        else:
            QMessageBox.information(self, "UPSS!!", "ALGO SALIO MAL")
        
    def Romper(self):
        self.Unuario.pop(-1)
        cadena = "".join(self.Unuario)
        cadena = cadena.replace("+","0")
        self.ListaProducto.clear()
        archi1=open("controller\sumar.txt","w") 
        archi1.write("# Symbols\n") 
        archi1.write("sigma = {0,1}\n") 
        archi1.write("gamma = {0, 1, B}\n")  
        archi1.write("\n")
        archi1.write("# Transition function\n")
        archi1.write("sum(q0, 0) = (q0, 1, R)\n")
        archi1.write("sum(q0, 1) = (q0, 1, R)\n")
        archi1.write("sum(q0, B) = (q2, B, L)\n")
        archi1.write("sum(q2, 1) = (q1, B, R)\n")
        archi1.write("\n")
        archi1.write("# States\n")
        archi1.write("Q = {q0, q1, q2}\n")
        archi1.write("F = {q1}\n")
        archi1.write("\n")
        archi1.write("# Turing machine description\n")
        archi1.write("M = (sigma, gamma, Q, sum, B, q0, F)\n")
        archi1.write("\n")
        archi1.write("# Arrays\n")
        archi1.write("input = ["+cadena+"]\n")
        archi1.write("\n")
        archi1.write("# Run machine M with input array l\n")
        archi1.write("!run(M, input)")
        archi1.close() 
        self.Unuario.clear()
        Diccionario("controller\sumar.txt")
        with open('controller\suma.txt') as f:
            lineas = f.readlines()
        total = "".join(lineas)
        
        self.TotalLabel.setText(total)
        
        
        
              
    def Productito(self):
       pass
    
    def CantidadProducto(self):
        pass
    
            