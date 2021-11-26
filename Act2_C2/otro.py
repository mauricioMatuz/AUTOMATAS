

iniciarCiclo = list()
indice = dict()
finalCiclo = list()
auxER = list()
alfabeto = set()
estados = {"q0"}
estadoFinal = set()
recorrido = list()


def ReescribirER(
    er,
):  # #Reescribimos la expresion regular para poder manejarlo mejor y a nuestra manera
    er = er.replace("^+", "@").replace(
        "^*", "*"
    )  #! reemplazamos las elevaciones por signos especiales
    er = er + "&"  #! le agregamos un signo especial al final para saber cuando parar
    for i in range(0, len(er), 1):
        if (
            er[i] != "("
            and er[i] != ")"
            and er[i] != "*"
            and er[i] != "+"
            and er[i] != "@"
            and er[i] != "."
            and er[i] != "&"
        ):
            # * el if de arriba sirve para agregar el alfabeto en la lista
            alfabeto.add(er[i])
        elif er[i - 1] == "(" and er[i] == ")":
            alfabeto.add("(")
            alfabeto.add(")")

    pos = 0
    aux = list(er)

    while aux[pos] != "&":
        #! este while solo sirve para dar formato a la ER, si no trae punto la ER
        if aux[pos] in alfabeto:
            pos = pos + 1
            if (aux[pos] in alfabeto) or (aux[pos] == "("):
                aux.insert(pos, ".")
                pos = pos + 1
        elif aux[pos] == "+" or aux[pos] == "." or aux[pos] == "(":
            pos = pos + 1
        elif aux[pos] == "*" or aux == "@":
            pos = pos + 1
            if (aux[pos] in alfabeto) or (aux[pos] == "("):
                aux.insert(pos, ".")
                pos = pos + 1
        elif aux[pos] == ")":
            pos = pos + 1
            if aux[pos] == "+" or aux[pos] == ".":
                pos = pos + 1
            elif aux[pos] == "*" or aux[pos] == "@":
                pos = pos + 1
                if aux[pos] == "+" or aux[pos] == ".":
                    pos = pos + 1
                elif (aux[pos] in alfabeto) or (aux[pos] == "("):
                    aux.insert(pos, ".")
                    pos = pos + 1
            elif (aux[pos] in alfabeto) or (aux[pos] == "("):
                aux.insert(pos, ".")
                pos = pos + 1
    aux.pop(len(aux) - 1)
    cadenaAux = "".join(aux)
    print(cadenaAux)
    return cadenaAux


def ReccorridoCiclo(er):
    inicio = 0
    fin = 0
    tam = 0
    aux = list(er)
    cadena = "".join(aux)
    pos = 0

    while len(aux) > pos:
        bandera = True
        if aux[pos] == "+":
            if -1 not in finalCiclo:
                final = pos
                aux.append(er[inicio:fin])
                inicio = fin + 1
        elif aux[pos] == "(":
            iniciarCiclo.append(pos)
            finalCiclo.append(-1)
        elif aux[pos] == ")":
            if pos < (len(aux) - 1):
                indice = pos + 1
                if aux[indice] == "*" or aux[indice] == "@":
                    pos = pos + 1
            tam = len(iniciarCiclo)
            while bandera:
                tam = tam - 1
                if finalCiclo[tam] == -1:
                    finalCiclo[tam] = pos
                    bandera = False
        if len(aux) > pos:
            pos = pos + 1
        else:
            break
    auxER.append(er[inicio:])

    iniciarCiclo.clear()
    finalCiclo.clear()


def CrearEstados(estado):
    while True:
        nuevoEstado = "q" + str(int(estado[1:]) + 1)
        estado = nuevoEstado
        if nuevoEstado not in estados:
            estados.add(estado)
            break
    return estado


def Concatenacion(simbolo, acutal, destino=""):
    fin = CrearEstados(acutal)
    recorrido.append("("+acutal + "," + "e" + "," + fin+"),")
    acutal = fin
    fin = CrearEstados(acutal)
    recorrido.append("("+acutal + "," + simbolo + "," + fin+"),")
    acutal = fin
    if destino == "":
        fin = CrearEstados(acutal)
        recorrido.append("("+acutal + "," + "e" + "," + fin+"),")
        return fin
    else:
        recorrido.append("("+acutal + "," + "e" + "," + destino+"),")
        return destino


def union(simbolo, actual, destino=""):
    fin = CrearEstados(actual)
    recorrido.append("("+actual + "," + "e" + "," + fin+"),")
    actual = fin
    fin = CrearEstados(actual)
    recorrido.append("("+actual + "," + simbolo + "," + fin+"),")
    actual = fin
    if destino == "":
        destino = CrearEstados(actual)
        recorrido.append("("+actual + "," + "e" + "," + destino+"),")
        return destino
    else:
        recorrido.append("("+actual + "," + "e" + "," + destino+"),")
        return destino


def ClausuraKleene(simbolo, actual, destino=""):
    print(actual, " ACTUAL :D")
    fin = CrearEstados(actual)
    recorrido.append("("+actual + "," + "e" + "," + fin+"),")
    acutal = fin
    recorrido.append("("+actual + "," + simbolo + "," + acutal+"),")
    if destino == "":
        fin = CrearEstados(acutal)
        recorrido.append("("+actual + "," + "e" + "," + fin+"),")
        return fin
    else:
        recorrido.append("("+actual + "," + "e" + "," + destino+"),")
        return destino


def ClausuraPositiva(simbolo, actual, destino=""):
    fin = CrearEstados(actual)
    recorrido.append("("+actual + "," + "e" + "," + fin+"),")
    actual = fin
    fin = CrearEstados(actual)
    recorrido.append("("+actual + "," + simbolo + "," + fin+"),")
    actual = fin
    fin = CrearEstados(actual)
    recorrido.append("("+actual + "," + "e" + "," + fin+"),")
    actual = fin
    fin = CrearEstados(actual)
    recorrido.append("("+actual + "," + "e" + "," + fin+"),")
    actual = fin
    recorrido.append("("+actual + "," + simbolo + "," + actual+"),")
    if destino == "":
        fin = CrearEstados(actual)
        recorrido.append("("+actual + "," + "e" + "," + fin+"),")
        return fin
    else:
        recorrido.appen("("+actual + "," + "e" + destino+"),")
        return destino


def SepararParen():
    for i in range(0, len(iniciarCiclo), 1):
        indice[iniciarCiclo[i]] = finalCiclo[i]
    iniciarCiclo.clear()
    finalCiclo.clear()


def SaberRecorrido(er):
    pos = 0
    aux = list(er)
    while len(er) > pos:
        bandera = True
        if aux[pos] == "(":
            iniciarCiclo.append(pos)
            finalCiclo.append(-1)
        elif aux[pos] == ")":
            if pos < len(aux) - 1:
                indice = pos + 1
                if aux[indice] == "*" or aux[indice] == "@":
                    pos = pos + 1
            tam = len(iniciarCiclo)
            while bandera:
                tam = tam - 1
                if finalCiclo[tam] == -1:
                    finalCiclo[tam] = pos
                    bandera = False
        if len(aux) > pos:
            pos = pos + 1
        else:
            break
    DefinirIndice()


def DefinirIndice():
    for i in range(0, len(iniciarCiclo), 1):
        indice[iniciarCiclo[i]] = finalCiclo[i]
    iniciarCiclo.clear()
    finalCiclo.clear()


def CrearRecorrido(
    exprecion, actual, destino="", destinoFinal="", bandera=False
):  # evalua la expresion que se le pasa y crea las tranciones de esta
    indiceAuxiliar = 0
    indiceUtil = 0
    SaberRecorrido(exprecion)
    fin, final = "", ""
    er = list(exprecion)
    i = 0
    while i < len(er):
        if er[i] in alfabeto:
            if i == 0:
                if (i + 1) != len(er):
                    j = i + 1
                    if er[j] == "*":
                        j = i + 2
                        if j == len(er):
                            fin = ClausuraKleene(er[i], actual, destino)
                            final = fin
                            destino = fin
                        elif (
                            er[j] == "+"
                        ):  # verifico si es el simbolo actual despues de la clausuara de Klene es una union =+
                            fin = ClausuraKleene(er[i], actual, destino)
                            final = fin
                            destino = fin
                        elif (
                            er[j] == "."
                        ):  # verifico si es el simbolo actual despues de la clausuara de Klene es una concadenacion =.
                            fin = ClausuraKleene(er[i], actual)
                            final = fin
                            actual = fin
                    # aca termina el if (er[j] == "*"):
                    elif (
                        er[j] == "°"
                    ):  # verifico si el simbolo actual es una clausuara positiva o si se repite 1 o mas veces =°
                        fin = ClausuraPositiva(er[i], actual, destino)
                        j = i + 2
                        if j == len(er):
                            destino = fin
                            final = fin
                        elif (
                            er[j] == "+"
                        ):  # verifico si es el simbolo actual despues de la clausuara de positiva es una union
                            destino = fin
                            final = fin
                        elif (
                            er[j] == "."
                        ):  # verifico si es el simbolo actual despues de la clausuara de positiva es una concadenacion
                            actual = fin
                    # aca termina elif (er[j] == "°"):
                    elif er[j] == "+":  # verifico si es el simbolo actual es una union
                        destino = union(er[i], actual, destino)
                    elif (
                        er[j] == "."
                    ):  # verifico si es el simbolo actual es una concadenacion
                        actual = Concatenacion(er[i], actual)
                # aca termina el if (i + 1) != len(er):
                else:  # es el ultimo simbolo de la expresion
                    if destino == "":  # evalua si existe un destino
                        if (
                            bandera == True
                        ):  # si el simbolo actual pertene a una clausura de klene
                            final = Concatenacion(
                                er[i],
                                actual,
                            )
                        else:
                            final = Concatenacion(er[i], actual, destino)
                    else:
                        if (
                            bandera == True
                        ):  # si el simbolo actual pertene a una clausura de klene
                            final = Concatenacion(er[i], actual, destinoFinal)
                        else:
                            final = Concatenacion(er[i], actual, destino)
            # aqui termina el if == 0
            elif i != 0:  # verifico si no es el primer sombolo de entrada
                j = i - 1
                if er[j] == "+":  # evalua si el simbolo anterior fue una union
                    j = i + 1
                    if (i + 1) == len(
                        er
                    ):  # evalua si el simbolo actual es el ultimo dela cadena
                        if destino == "":  # evalua si existe un destino
                            if (
                                bandera == True
                            ):  # si el simbolo actual pertene a una clausura de klene
                                final = union(er[i], actual, destinoFinal)
                            else:
                                final = union(er[i], actual, destino)
                        else:
                            if (
                                bandera == True
                            ):  # si el simbolo actual pertene a una clausura de klene
                                final = union(er[i], actual, destinoFinal)
                            else:
                                final = union(er[i], actual, destino)
                    elif (
                        er[j] == "*"
                    ):  # verifico si es el sombolo actual es una clausura de Klene o si se repite 0 o mas veces =*
                        j = i + 2
                        if j == len(
                            er
                        ):  # verifico si es el simbolo actual despues de la clausuara de klene es el simbolo final dela cadena
                            destino = ClausuraKleene(er[i], actual, destino)
                            final = destino
                        elif (
                            er[j] == "+"
                        ):  # verifico si es el simbolo actual despues de la clausuara de Klene es una union =+
                            fin = ClausuraKleene(er[i], actual, destino, destino)
                            destino = fin
                        elif (
                            er[j] == "."
                        ):  # verifico si es el simbolo actual despues de la clausuara de Klene es una concadenacion =.
                            fin = ClausuraKleene(er[i], actual, destino)
                            actual = fin
                    # termina elif (er[j] == "*"):
                    elif (
                        er[j] == "°"
                    ):  # verifico si el simbolo actual es una clausuara positiva o si se repite 1 o mas veces =°
                        j = i + 2
                        if j == len(
                            er
                        ):  # verifico si es el simbolo actual despues de la clausuara positiva es el simbolo final dela cadena
                            if bandera == True:
                                destino = ClausuraPositiva(er[i], actual, destinoFinal)
                            else:
                                destino = ClausuraPositiva(er[i], actual, destino)
                            final = destino
                        elif (
                            er[j] == "+"
                        ):  # verifico si es el simbolo actual despues de la clausuara positiva es una union
                            fin = ClausuraPositiva(er[i], actual, destino)
                            destino = fin
                            final = fin
                        elif (
                            er[j] == "."
                        ):  # verifico si es el simbolo actual despues de la clausuara positiva es una concadenacion
                            fin = ClausuraPositiva(er[i], actual, destino)
                            actual = fin
                    elif er[j] == "+":  # verifico si es el simbolo actual es una union
                        destino = union(er[i], actual, destino)
                        final = destino
                    elif (
                        er[j] == "."
                    ):  # verifico si es el simbolo actual es una concadenacion
                        fin = Concatenacion(er[i], actual, destino)
                # termina if er[j] == "+"
                elif (
                    er[j] == "."
                ):  # evalua si el simbolo anterior fue una concadenacion
                    j = i + 1
                    if (i + 1) == len(
                        er
                    ):  # evalua si el simbolo actual es el ultimo dela cadena
                        if destino == "":
                            if bandera == True:
                                destino = Concatenacion(er[i], actual, destinoFinal)
                            else:
                                destino = Concatenacion(er[i], actual, destino)
                            final = destino
                        else:
                            if bandera == True:
                                destino = Concatenacion(er[i], actual, destinoFinal)
                            else:
                                destino = Concatenacion(er[i], actual, destino)
                            final = destino
                    # termina  if (i + 1) == len(er):
                    elif (
                        er[j] == "*"
                    ):  # verifico si es el sombolo actual es una clausura de Klene o si se repite 0 o mas veces =*
                        j = i + 2
                        if j == len(er):
                            if bandera == True:
                                destino = ClausuraKleene(er[i], actual, destinoFinal)
                            else:
                                destino = ClausuraKleene(er[i], actual, destino)
                            final = destino
                        elif (
                            er[j] == "+"
                        ):  # verifico si es el simbolo actual despues de la clausuara de Klene es una union =+
                            fin = ClausuraKleene(er[i], actual, destino)
                            destino = fin
                            final = destino
                        elif (
                            er[j] == "."
                        ):  # verifico si es el simbolo actual despues de la clausuara de Klene es una concadenacion =.
                            print(actual, " ENTODO EL DES")
                            fin = ClausuraKleene(er[i], actual, destino)
                            actual = fin
                    # termina  elif (er[j] == "*"):
                    elif (
                        er[j] == "°"
                    ):  # verifico si el simbolo actual es una clausuara positiva o si se repite 1 o mas veces =°
                        j = i + 2
                        if j == len(er):
                            if bandera == True:
                                destino = ClausuraPositiva(er[i], actual, destinoFinal)
                            else:
                                destino = ClausuraPositiva(er[i], actual, destino)
                            final = destino
                        elif (
                            er[j] == "+"
                        ):  # verifico si es el simbolo actual despues de la clausuara Positiva es una union =+
                            fin = ClausuraPositiva(er[i], actual, destino)
                            destino = fin
                            final = destino
                        elif (
                            er[j] == "."
                        ):  # verifico si es el simbolo actual despues de la clausuara Positiva es una concadenacion =.
                            fin = ClausuraPositiva(er[i], actual, destino)
                            actual = fin
                    # termina elif (er[j] == "°"):
                    elif er[j] == "+":  # verifico si es el simbolo actual es una union
                        if bandera == True:
                            destino = union(er[i], actual, destinoFinal)
                        else:
                            destino = union(er[i], actual, destino)
                        destino = union(er[i], actual, destino)
                        final = destino
                    # aca termina  elif er[j] == "+":
                    elif (
                        er[j] == "."
                    ):  # verifico si es el simbolo actual es una concadenacion
                        actual = Concatenacion(er[i], actual)
                        final = actual
        # termina if (er[i] in alfabeto):
        if er[i] == "(":  # verifico si es una agrupacion
            if (
                er[indice.get(i)] == "*"
            ):  # verifico si la agrupacion es una clausura de klene
                bandera = True
                destino = actual
                j = indice.get(i) - 1
                indiceAuxiliar = j + 1
                destinoFinal = actual
                destino = CrearRecorrido(
                    exprecion[(i + 1) : j], actual, destino, destinoFinal
                )
                i = indiceAuxiliar
            elif er[indice.get(i)] == ")":  # verifico si la agrupacion normal
                j = indice.get(i)
                indiceAuxiliar = j
                actual = CrearRecorrido(
                    exprecion[(i + 1) : j], actual, destino, destinoFinal
                )
                i = indiceAuxiliar
                destino = ""
            elif (
                er[indice.get(i)] == "°"
            ):  # verifico si la agrupacion es una clausura positiva
                j = indice.get(i) - 1
                indiceAuxiliar = j + 1
                actual = CrearRecorrido(
                    exprecion[(i + 1) : j], actual, destino, destinoFinal
                )
                destino = actual
                destinoFinal = actual
                destino = CrearRecorrido(
                    exprecion[(i + 1) : j], actual, destino, destinoFinal
                )
                i = indiceAuxiliar
                destino = ""
        i = i + 1  # incremento el contador
    estadoFinal.add(","+final)  # agrega el estado final de el recorrido
    return destino


def Imprimir():
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
    exec(open("afnd.py").read())
    #!cuando termine esto agrega una ventana que diga automata realizado 


def main():
    inicio = "q0"
    er = ReescribirER("(a+b)^++(a+c+ε)*(b+c)^*")
    ReccorridoCiclo(er)
    bandera = False
    for expre in auxER:
        CrearRecorrido(expre, inicio)
        
    
    Imprimir()


main()
