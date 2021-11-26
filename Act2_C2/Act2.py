from tkinter import *
from tkinter import messagebox
import afnd

iniciarCiclo = list()
indice = dict()
finalCiclo = list()
auxER = list()
alfabeto = set()
estados = {"q0"}
estadoFinal = set()
recorrido = list()

def CrearRecorrido(exprecion,actual,destino="",destinoFinal="",bandera=False): #! FUNCION SE ENCARGA DE crear el recorrido dependiendo de la ER
    indiceAuxiliar = 0
    indiceUtil = 0
    SaberRecorrido(exprecion)
    fin,final = "",""
    er = list(exprecion)
    i = 0
    while i < len(er):
        if er[i] in alfabeto:#verifico si el simbolo actual pertene a un simbolo del alfabeto
            if i == 0: #verifico si es el sombolo actual es el primero
                if (i+1) != len(er):#verifico si es el sombolo actual no es el ultimo de la cadena
                    j = i + 1 
                    if er[j] == "*": #?verifico si es el sombolo actual es una clausura de Klene o si se repite 0 o mas veces =*
                        j = i + 2
                        if j == len(er):
                            fin = ClausuraKleene(er[i],actual,destino)
                            final = fin
                            destino = fin
                        elif er[j] == "+":#?verifico si es el simbolo actual despues de la clausuara de Klene es una union =+
                            fin = ClausuraKleene(er[i],actual,destino)
                            final = fin
                            destino = fin
                        elif er[j] == ".":#?verifico si es el simbolo actual despues de la clausuara de Klene es una concadenacion =.
                            fin = ClausuraKleene(er[i],actual)
                            final = fin
                            actual = fin
                    elif er[j] == "°":#?verifico si el simbolo actual es una clausuara positiva o si se repite 1 o mas veces =°
                        fin = ClausuraPositiva(er[i],actual,destino)
                        j = i + 2
                        if j == len(er):
                            destino = fin
                            final = fin
                        elif er[j] == "+":#?verifico si es el simbolo actual despues de la clausuara de positiva es una union
                            destino = fin
                            final = fin
                        elif er[j] == ".":#?verifico si es el simbolo actual despues de la clausuara de positiva es una concadenacion
                            actual = fin
                    elif er[j] == "+":#?verifico si es el simbolo actual es una union
                        destino = union(er[i],actual,destino)
                    elif er[j] == ".":#?verifico si es el simbolo actual es una concadenacion
                        actual = Concatenacion(er[i],actual)
                else: #es el ultimo simbolo de la expresion 
                    if destino == "": #?evalua si existe un destino 
                        if bandera == True:#?si el simbolo actual pertene a una clausura de klene  
                            final = Concatenacion(er[i],actual,destinoFinal)
                        else:
                            final = Concatenacion(er[i],actual,destino)
                    else:
                        if bandera == True:#?si el simbolo actual pertene a una clausura de klene
                            final = Concatenacion(er[i],actual,destinoFinal)
                        else:
                            final = Concatenacion(er[i],actual,destino)
            elif i != 0: #?verifico si no es el primer sombolo de entrada
                j = i - 1
                if er[j] == "+":#?evalua si el simbolo anterior fue una union
                    j = i + 1 
                    if (i+1) == len(er):#?evalua si el simbolo actual es el ultimo dela cadena
                        if destino == "": #?evalua si existe un destino 
                            if bandera == True:#?si el simbolo actual pertene a una clausura de klene
                                final = union(er[i],actual,destinoFinal)
                            else:
                                final = union(er[i],actual,destino)
                        else:
                            if bandera == True:#?si el simbolo actual pertene a una clausura de klene
                                final = union(er[i],actual,destinoFinal)
                            else:
                                final = union(er[i],actual,destino)
                    elif er[j] == "*": #?verifico si es el sombolo actual es una clausura de Klene o si se repite 0 o mas veces =*
                        j = i + 2
                        if j == len(er):#?verifico si es el simbolo actual despues de la clausuara de klene es el simbolo final dela cadena
                            destino = ClausuraKleene(er[i],actual,destino)
                            final = destino
                        elif er[j] == "+":#?verifico si es el simbolo actual despues de la clausuara de Klene es una union =+
                            fin = ClausuraKleene(er[i],actual,destino,destino)
                            destino = fin
                        elif er[j] == ".":#?verifico si es el simbolo actual despues de la clausuara de Klene es una concadenacion =.
                            fin = ClausuraKleene(er[i],actual,destino)
                            actual = fin
                    elif er[j] == "°":#?verifico si el simbolo actual es una clausuara positiva o si se repite 1 o mas veces =°
                        j = i + 2
                        if j == len(er):#?verifico si es el simbolo actual despues de la clausuara positiva es el simbolo final dela cadena
                            if bandera == True:
                                destino = ClausuraPositiva(er[i],actual,destinoFinal)
                            else:
                                destino = ClausuraPositiva(er[i],actual,destino)
                            final = destino
                        elif er[j] == "+":#?verifico si es el simbolo actual despues de la clausuara positiva es una union
                            fin = ClausuraPositiva(er[i],actual,destino)
                            destino = fin
                            final = fin
                        elif er[j] == ".":#?verifico si es el simbolo actual despues de la clausuara positiva es una concadenacion
                            fin = ClausuraPositiva(er[i],actual,destino)
                            actual = fin
                    elif er[j] == "+":#?verifico si es el simbolo actual es una union
                        destino = union(er[i],actual,destino)
                        final = destino
                    elif er[j] == ".":#?v?erifico si es el simbolo actual es una concadenacion
                        fin = Concatenacion(er[i],actual,destino)
                elif er[j] == ".":#?evalua si el simbolo anterior fue una concadenacion
                    j = i + 1
                    if (i+1) == len(er):#?evalua si el simbolo actual es el ultimo dela cadena
                        if destino == "":
                            if bandera == True:
                                destino = Concatenacion(er[i],actual,destinoFinal)
                            else:
                                destino = Concatenacion(er[i],actual,destino)
                            final = destino
                        else:
                            if bandera == True:
                                destino = Concatenacion(er[i],actual,destinoFinal)
                            else:
                                destino = Concatenacion(er[i],actual,destino)
                            final = destino
                    elif er[j] == "*": #?verifico si es el sombolo actual es una clausura de Klene o si se repite 0 o mas veces =*
                        j = i + 2
                        if j == len(er):
                            if bandera == True:
                                destino = ClausuraKleene(er[i],actual,destinoFinal)
                            else:
                                destino = ClausuraKleene(er[i],actual,destino)
                            final = destino
                        elif er[j] == "+":#?verifico si es el simbolo actual despues de la clausuara de Klene es una union =+
                            fin = ClausuraKleene(er[i],actual,destino)
                            destino = fin
                            final = destino
                        elif er[j] == ".":#?verifico si es el simbolo actual despues de la clausuara de Klene es una concadenacion =.
                            fin = ClausuraKleene(er[i],actual,destino)
                            actual = fin
                    elif er[j] == "°":#?verifico si el simbolo actual es una clausuara positiva o si se repite 1 o mas veces =°
                        j = i + 2
                        if j == len(er):
                            if bandera == True:
                                destino = ClausuraPositiva(er[i],actual,destinoFinal)
                            else:
                                destino = ClausuraPositiva(er[i],actual,destino)
                            final = destino
                        elif er[j] == "+":#?verifico si es el simbolo actual despues de la clausuara Positiva es una union =+
                            fin = ClausuraPositiva(er[i],actual,destino)
                            destino = fin
                            final = destino
                        elif er[j] == ".":#?verifico si es el simbolo actual despues de la clausuara Positiva es una concadenacion =.
                            fin = ClausuraPositiva(er[i],actual,destino)
                            actual = fin
                    elif er[j] == "+":#?verifico si es el simbolo actual es una union
                        if bandera == True:
                            destino = union(er[i],actual,destinoFinal)
                        else:
                            destino = union(er[i],actual,destino)
                        destino = union(er[i],actual,destino)
                        final = destino
                    elif er[j] == ".":#?verifico si es el simbolo actual es una concadenacion
                        actual = Concatenacion(er[i],actual)
                        final = actual
        if er[i] == "(":#?verifico si es una agrupacion
            if er[indice.get(i)] == "*":#?verifico si la agrupacion es una clausura de klene
                bandera = True
                destino = actual
                j = indice.get(i)-1
                indiceAuxiliar = j+1
                destinoFinal = actual
                destino = CrearRecorrido(exprecion[(i+1):j],actual,destino,destinoFinal)
                i = indiceAuxiliar
            elif er[indice.get(i)] == ")":#?verifico si la agrupacion normal
                j = indice.get(i)
                indiceAuxiliar = j
                actual = CrearRecorrido(exprecion[(i+1):j],actual,destino,destinoFinal)
                i = indiceAuxiliar
                destino = ""
            elif  er[indice.get(i)] == "°":#?verifico si la agrupacion es una clausura positiva
                j = indice.get(i)-1
                indiceAuxiliar = j+1
                actual = CrearRecorrido(exprecion[(i+1):j],actual,destino,destinoFinal)
                destino = actual
                destinoFinal = actual
                destino = CrearRecorrido(exprecion[(i+1):j],actual,destino,destinoFinal)
                i = indiceAuxiliar
                destino = ""
        i = i + 1 #?incremento el contador
    estadoFinal.add(","+final)#?agrega el estado final de el recorrido
    return destino


def Concatenacion(simbolo,actual,destino=""): # #! genera las tranciones de A. | .A
    fin = CrearEstados(actual)
    recorrido.append("("+actual+","+"e"+","+fin+"),")
    actual = fin
    fin = CrearEstados(actual)
    recorrido.append("("+actual+","+simbolo+","+fin+"),")
    actual = fin
    if destino == "":
        fin = CrearEstados(actual)
        recorrido.append("("+actual+","+"e"+","+fin+"),")
        return fin
    else:
        recorrido.append("("+actual+","+"e"+","+destino+"),")
        return destino

def union(simbolo,actual,destino=""): # #! genera las tranciones de A+ | +A
    fin = CrearEstados(actual)
    recorrido.append("("+actual+","+"e"+","+fin+"),")
    actual = fin
    fin = CrearEstados(actual)
    recorrido.append("("+actual+","+simbolo+","+fin+"),")
    actual = fin
    if destino == "":
        destino = CrearEstados(actual)
        recorrido.append("("+actual+","+"e"+","+destino+"),")
        return destino
    else:
        recorrido.append("("+actual+","+"e"+","+destino+"),")
        return destino

def ClausuraKleene(simbolo,actual,destino=""): # # !genera las tranciones de A^* | ()^* | A* | ()*
    fin = CrearEstados(actual)
    recorrido.append("("+actual+","+"e"+","+fin+"),")
    actual = fin
    recorrido.append("("+actual+","+simbolo+","+actual+"),")
    if destino == "":
        fin = CrearEstados(actual)
        recorrido.append("("+actual+","+"e"+","+fin+"),")
        return fin
    else:
        recorrido.append("("+actual+","+"e"+","+destino+"),")
        return destino

def ClausuraPositiva(simbolo,actual,destino=""): #! genera las tranciones de A^+ | ()^+ | A° | ()°|
    fin = CrearEstados(actual)
    recorrido.append("("+actual+","+"e"+","+fin+"),")
    actual = fin
    fin = CrearEstados(actual)
    recorrido.append("("+actual+","+simbolo+","+fin+"),")
    actual = fin
    fin = CrearEstados(actual)
    recorrido.append("("+actual+","+"e"+","+fin+"),")
    actual = fin
    fin = CrearEstados(actual)
    recorrido.append("("+actual+","+"e"+","+fin+"),")
    actual = fin
    recorrido.append("("+actual+","+simbolo+","+actual+"),")
    if destino == "":
        fin = CrearEstados(actual)
        recorrido.append("("+actual+","+"e"+","+fin+"),")
        return fin
    else:
        recorrido.append("("+actual+","+"e"+","+destino+"),")
        return destino

def CrearEstados(estado): #!#crea nuevos estados
    while True:
        nuevoEstado = "q" + str(int(estado[1:])+1)
        estado = nuevoEstado
        if nuevoEstado not in estados:
            estados.add(estado)
            break
    return estado

def Imprimir():##! muestra todas la trasiciones existentes
      guardarEstados = []
      guardarAlfabet = []
      for e in estados:
            guardarEstados.append(e+",")     
      for alfa in alfabeto:
            guardarAlfabet.append(alfa+",")
      
      guardarAlfabet.append("e")
      
      cadenaEstados = "".join(guardarEstados)
      cadenaEstados = "Q = {"+cadenaEstados+"}"
      cadenaAlfabeto = "".join(guardarAlfabet)
      cadenaAlfabeto = "S = {"+cadenaAlfabeto+"}"
      cadenaInicio = "Q0 = q0"
      cadenaFinal = "".join(estadoFinal)
      cadenaFinal = "F = {"+cadenaFinal+"}"
      cadenaRecorrido = "".join(recorrido)
      cadenaRecorrido = "R = {"+cadenaRecorrido+"}"
      archi1=open("datos.txt",'w', encoding='utf-8') 
      archi1.write(cadenaEstados+"\n") 
      archi1.write(cadenaAlfabeto+"\n") 
      archi1.write(cadenaInicio+"\n")
      archi1.write(cadenaFinal+"\n")
      archi1.write(cadenaRecorrido)
      archi1.close()
      afnd.proceso()
      messagebox.showinfo("AUTOMATA REALIZADO")
      #return cadenaRecorrido
    #!cuando termine esto agrega una ventana que diga automata realizado 

def ReccorridoCiclo(er): ##! divide la expresion en los distintos recorridos  para saber si es un cliclo o no :3
    inicioRecorrido = 0
    finRecorrido = 0
    tam = 0
    listAux = list(er)
    er = "".join(listAux)
    i = 0
    while len(listAux) > i:
        bandera=True
        if listAux[i]=="+":
            if (-1 not in finalCiclo):
                finRecorrido = i
                auxER.append(er[inicioRecorrido:finRecorrido])
                inicioRecorrido = finRecorrido + 1 
        elif listAux[i] == "(":
            iniciarCiclo.append(i)
            finalCiclo.append(-1)
        elif listAux[i] == ")":
            if i < (len(listAux)-1):
                indice = i+1
                if listAux[indice] == "*" or listAux[indice] == "°":
                    i = i+1
            tam = len(iniciarCiclo)
            while bandera:
                tam = tam - 1
                if finalCiclo[tam]==-1:    
                    finalCiclo[tam] = i
                    bandera = False
        if len(listAux) > i:
            i = i+1
        else:
            break
    auxER.append(er[inicioRecorrido:])
    iniciarCiclo.clear()
    finalCiclo.clear()

def SaberRecorrido(er):#! aca descubrimos que tipo de recorrido hara, es decir, si es union kleene etc
    i = 0
    listAux = list(er)
    while len(er) > i:
        bandera=True
        if listAux[i] == "(":
            iniciarCiclo.append(i)
            finalCiclo.append(-1)
        elif listAux[i] == ")":
            if i < (len(listAux)-1):
                indice = i+1
                if listAux[indice] == "*" or listAux[indice] == "°":
                    i = i+1
            tam = len(iniciarCiclo)
            while bandera:
                tam = tam - 1
                if finalCiclo[tam]==-1:    
                    finalCiclo[tam] = i
                    bandera = False
        if len(listAux) > i:
            i = i+1
        else:
            break
    DefinirIndice()

def DefinirIndice(): #! asigna que indice es de que corchete y cual es el que le corresponde ejemplo indice 0 = ( le corresponde indice 1 = ) | )* | )°
    for i in range(0,len(iniciarCiclo),1):
        indice[iniciarCiclo[i]] = finalCiclo[i]
    iniciarCiclo.clear()
    finalCiclo.clear()

def ReescribirER(er):#! metodo que rescribe la expresion a una que el programa pueda leer devolviendo la nueva expresion
    er = er.replace("^+","°")
    er = er.replace("^*","*")
    er = er + "$"
    #para recolectar los simbolos que van a conformar el alfabeto
    for i in range(0,len(er),1):
        if er[i]!="(" and er[i]!=")" and er[i]!="*" and er[i]!="+" and er[i]!="°" and er[i]!="." and er[i]!="$":
            alfabeto.add(er[i])
        elif er[i-1]=="(" and er[i]==")":
            alfabeto.add("(")
            alfabeto.add(")")
    i = 0
    erAux = list(er)
    #rescribe la expresion a una que se puede interpretar mejor
    while erAux[i] !="$":
        if erAux[i] in alfabeto:
            i=i+1
            if (erAux[i] in alfabeto) or (erAux[i] == "("):
                erAux.insert(i, ".")   
                i=i+1
        elif erAux[i]=="+" or erAux[i]=="." or erAux[i] == "(":
            i=i+1
        elif erAux[i] == "*" or erAux[i] == "°":
            i=i+1
            if (erAux[i] in alfabeto) or (erAux[i] == "("):
                erAux.insert(i, ".")   
                i=i+1
        elif erAux[i] == ")":
            i = i+1
            if  erAux[i]=="+" or erAux[i]==".":
                i = i+1
            elif erAux[i] == "*" or erAux[i] == "°":
                i = i+1
                if erAux[i]=="+" or erAux[i]==".":
                    i = i+1
                elif (erAux[i] in alfabeto) or (erAux[i] == "("):
                    erAux.insert(i, ".")   
                    i=i+1
            elif (erAux[i] in alfabeto) or (erAux[i] == "("):
                erAux.insert(i, ".")   
                i= i + 1
    erAux.pop(len(erAux)-1)
    cadenaAux = "".join(erAux) #une la lista de caracteres y lo convierte en una cadena 
    return cadenaAux

def main():
    inicio = "q0"
    nuevaER = ReescribirER("a+b")# metodo que rescribe la expresion a una que el programa pueda leer devolviendo la nueva expresion
    ReccorridoCiclo(nuevaER) # divide la expresion en los distintos recorridos que tienes la expresion y lo guarda en una lista
    for expre in auxER:
      CrearRecorrido(expre,inicio) # evalua la expresion y genera las distintas recorrido del recorrido
    Imprimir() # imprime todas las recorrido 
main()