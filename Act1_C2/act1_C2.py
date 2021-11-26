#Valide funciones de transición de AFND
import sys
from typing import Type 

with open("data.txt") as f:
    lineas = f.readlines()

i=0
lista = []

while i < len(lineas):
    lin = lineas[i].replace("=","")
    lin = lin.replace("  "," ")
    lin = lin.replace("\n","")
    lin = lin.replace("{","")
    lin = lin.replace("}","")
    lista.append(lin.split(" "))
    i = i + 1

q = lista[0][1].split(",")
s = lista[1][1].split(",")

#s.append('e')
q0 = lista[2][1].split(",")
f = lista[3][1].split(",")
aux = lista[4][1]
r = aux[1:len(aux)-1].split("),(")
estados = []


i=0

while i < len(r):
    estados.append(r[i].split(","))
    i = i + 1

repetidos = []

for i in range(len(estados)-1):
    estado_previo = estados[i][0]
    valor = estados[i][1]
    estado_despues = estados[i][2]
    
    if estado_previo == estado_despues:
        print(estado_previo," = ",valor," ",estado_despues)
    
    if estado_previo == estados[i+1][0]:
        print(estado_previo," = ",valor,estado_despues,"|",estados[i+1][1],estados[i+1][2])
    
    #print(estado_previo," = ",valor,estado_despues)









# private simbolo = /[.,:(-)\n\t ]/
# private identificador = /^[A-Za-z]+[\w_A-Zaz]+[\w]*$/
# private expresionNumero = /^\d{1,4}$/