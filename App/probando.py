import openpyxl as xl
import math


book = xl.load_workbook("App.xlsx", data_only=True)
hoja = book.active
celda = hoja['A2':'C60']
numero_telefono = []
datos = []

for fila in celda:
    numero = [celda.value for celda in fila]
    datos.append(numero)

for numeritos in datos:
    num = numeritos[2].split("(")
    numero_telefono.append(num)

lada = []

for evaluar in numero_telefono:
    lad = evaluar[0]
    lada.append(lad)

n = 0
#Variables ciudad que sirven para saber la cantidad exacta de cada ciudad. 
ciudad1 = 0
ciudad2 = 0
ciudad3 = 0
ciudad4 = 0
ciudad5 = 0
ciudad6 = 0
ciudad7 = 0
ciudad8 = 0
ciudad9 = 0
ciudad10 = 0
ciudad11 = 0
total = 0
totalin = 0
while n < len(lada):
    with open("data.txt") as f:
        lineas = f.readlines()
    
    i = 0
    lista = []

    while i < len(lineas):
        lin = lineas[i].replace("=", "")
        lin = lin.replace("  ", "-")
        lin = lin.replace("\n", "")
        lin = lin.replace("{", "")
        lin = lin.replace("}", "")
        lista.append(lin.split("-"))
        i = i + 1

    q = lista[0][1].split(",")
    s = lista[1][1].split(",")

    # s.append('e')
    q0 = lista[2][1].split(",")
    f = lista[3][1].split(",")
    aux = lista[4][1]
    r = aux[1:len(aux)-1].split("),(")
    estados = []
    i = 0
    while i < len(r):
        estados.append(r[i].split(","))
        i = i + 1


    estado_final = False
    estados_actuales = []
    estados_actuales.append(q0[0])
    

    cadena = list(lada[n])

    while cadena:
       # print("evaluand la cadena >>>>",cadena,"<<<<")
        if(cadena[0] in s):
            num_estados = len(estados_actuales)
            for i in range(len(estados)):
                for j in range(num_estados):
                    if estados[i][0] == estados_actuales[j] and estados[i][1] == cadena[0]:
                        estados_actuales.append(estados[i][2])
                        #print(estados_actuales[j]," dentro del for")
            for y in range(num_estados):
                estados_actuales.remove(estados_actuales[0])
            #print(estados_actuales," fuera del for")
            cadena.remove(cadena[0])
        else:
            #print("Un estado en la cadena no es valido", ">>>", cadena[0], "<<<")
            break

    
    if 'q1' in estados_actuales:
        ciudad1 = ciudad1 + 1
    elif 'q2'in estados_actuales:
        ciudad2 = ciudad2 + 1
    elif 'q4'in estados_actuales:
        ciudad3 = ciudad3 + 1
    elif 'q6'in estados_actuales:
        ciudad4 = ciudad4 + 1
    elif 'q8'in estados_actuales:
        ciudad5 = ciudad5 + 1
    elif 'q11' in estados_actuales:
        ciudad6 = ciudad6 +1
    elif 'q13'in estados_actuales:
        ciudad7 = ciudad7 + 1
    elif 'q15'in estados_actuales:
        ciudad8 = ciudad8 + 1
    elif 'q17'in estados_actuales:
        ciudad9 = ciudad9 + 1
    elif 'q19'in estados_actuales:
        ciudad10 = ciudad10 + 1
    elif 'q20' in estados_actuales:
        ciudad11 = ciudad11 + 1
        
    
    for i in range(len(estados_actuales)):
        if(estados_actuales[i] in f):
            estado_final = True
            break
        else:
            estado_final = False

    if estado_final == True:
       # print("cadena valida")
        total = total +1
    else:
        totalin = totalin +1
        #print("cadena invalida") 
    n = n + 1
print("Hay un total de ",ciudad1," en la ciudad de Albania")
print("Hay un total de ",ciudad2," en la ciudad de Finlandia")
print("Hay un total de ",ciudad3," en la ciudad de Alemania")
print("Hay un total de ",ciudad4," en la ciudad de Andorra")
print("Hay un total de ",ciudad5," en la ciudad de Angola")
print("Hay un total de ",ciudad6," en la ciudad de Antártida")
print("Hay un total de ",ciudad7," en la ciudad de Arabia Saudita")
print("Hay un total de ",ciudad8," en la ciudad de Argelia")
print("Hay un total de ",ciudad9," en la ciudad de Cuba")
print("Hay un total de ",ciudad10," en la ciudad de Armenia")
print("Hay un total de ",ciudad11," en la ciudad de Ascensión, Isla")


