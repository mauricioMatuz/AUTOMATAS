#from _typeshed import Self
from tabulate import tabulate

class AFND():
    
    
    print("EJEM:")
    print("Estados (S) = 0 1 2 3 4 5")
    print("Alfabeto (sigma) = x y z")
    print("Tabla de transigciones = [[1,2,3],[5,1,1],[[1,3],[0,5],5],[[0,2],4,3],[4,2,[3,5]],[4,1,5]]")
    print("Estados inicio (s.) =0 3")
    print("Estado de aceptacion (F) = 5")
    print(" ")
    print("NOTA: SI LA TRANSICION ES NULA SOLO PRESIONE ENTER Y PASE A LA SGTE TRANS")
    print(" ")
    def estado():
        S = input("S = ").split(" ")
        return S
    def sigma():
        z = input("sigma = ").split(" ")
        return z
    
    def funcion(estados,sigma):
        n = len(estados)
        m = len(sigma)
        print("Recorrido=\n")
        fi = []
        for x in range(0,n):
            fi.append([])
            for y in range(0,m):
                fi[x].append(list(map(lambda x: -1 if x=='' else int(x),input("valor de recorrido(q"+str(x)+","+sigma[y]+") en recorrido = ").split(" "))))
        return fi
    
   # print(tabulate(funcion,headers=estado,showindex=sigma,tablefmt='fancy_grid',stralign='center',floatfmt='.0f'))
    
    def inicio():
        s = list(map(lambda x: int(x),input("s. = ").split(" ")))
        return s
    def final():
        F = input("F = ").split(" ")
        F = int(F[0])
        return F
    print(" ")
    

class Automata:
    def __init__(self,estados,inicial,final,alfabeto,transiccion):
        print(estados)
        self.estados = estados
        self.inicial = inicial
        self.final = final
        self.alfabeto = alfabeto
        self.transiccion = transiccion
        self.listaEcuacion = []
        
    def generarEcuacion(self):
        print("ESTADOS ", self.estados)
        self.listaEcuacion = []
        for i in self.estados:
            self.listaEcuacion.append([])
            for j in range(len(self.alfabeto)):
                self.listaEcuacion[int(i)].append(self.alfabeto[j]+str(self.transiccion[int(i)][j]))
        print(self.final, "final")
        self.listaEcuacion[int(self.final)].append("")
    
    def agrupar(self,lista):
        for i in self.estados:
            filtro = list(filter(lambda x : x.endswith(str(i)),lista))
            if(len(filtro)>1):
                pos = lista.index(filtro[0])
                for j in filtro:
                    lista.remove(j)
                filtro = list(map(lambda x : x[:-1],filtro))
                nuevo = "+".join(filtro)
                nuevo = "("+nuevo+")"+str(i)
                lista.insert(pos,nuevo)
    
    def arden(self,estado,lista):
        pos = -1
        for i in lista:
            if(i.endswith(str(estado))):
                pos = lista.index(i)
        
        if(pos != -1):
            valor = "["+lista[pos][:-1]+"]*"
            for j in range(len(lista)):
                if(pos !=j):
                    lista[j] = valor + lista[j]
            lista.pop(pos)
    
    def reemplazarValores(self,estados,lista1,lista2):
        listaEliminar = []
        for i in lista2:
            if(i.endswith(str(estados))):
                listaEliminar.append(i)
                valor = i[:-1]
                for j in lista1:
                    lista2.append(valor+j)
        for m in listaEliminar:
            lista2.remove(m)
    
    def generarExpresionRegular(self):
        self.generarEcuacion()
        for i in self.estados:
            self.agrupar(self.listaEcuacion[int(i)])
            self.arden(i,self.listaEcuacion[int(i)])
        
        for i in range(1,len(self.estados)-1):
            for j in range(int(i)+1,len(self.estados)):
                self.reemplazarValores(int(i),self.listaEcuacion[int(i)],self.listaEcuacion[j])
                self.agrupar(self.listaEcuacion[j])
                self.arden(j,self.listaEcuacion[j])
        
        for i in reversed(self.estados):
            for j in range(int(i)+1,len(self.estados)):
                self.reemplazarValores(j,self.listaEcuacion[j],self.listaEcuacion[int(i)])
                self.agrupar(self.listaEcuacion[int(i)])
                self.arden(int(i),self.listaEcuacion[int(i)])
        
        re = "+".join(self.listaEcuacion[0])
        
        for i in range(0,len(self.estados)):
            re = "+".join(self.listaEcuacion[i])
            
            print("A"+str(int(i))+" = "+re)
    
def MENU():
    print("="*10,"MENU","="*10)
    print("OPCION")
    print("1. AFD")
    print("2. AFND")
    o = 2
    if o == 2:
        estados = AFND.estado()
        print(estados)
        inicial = AFND.inicio()
        final = AFND.final()
        alfabeto = AFND.sigma()
        transiccion = AFND.funcion(estados,alfabeto)
        a = Automata(estados,inicial,final,alfabeto,transiccion)
        a.generarExpresionRegular()
    else:
        return

MENU()