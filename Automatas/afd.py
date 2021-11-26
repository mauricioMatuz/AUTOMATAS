#El siguiente programa necesita un parametro para poder ser ejecutado
#El parametro es la direccion del documento dodne se encuentra el automata
#Ejemplo de ejecucion:
#  python3 afd.py data.txt
 
import sys 

#abrimos el documento dodne se encuentran los datos del automata
#with open('datta.txt') as f:
with open(sys.argv[1]) as f:
    lineas = f.readlines()

i=0
lista = []
#Se limpia el texto donde se encuentran lso datos del automata para crear listas donde podemos manejar los datos 
#esto con la finalidad de poder manejar mas facil la informacion 
while i < len(lineas):
    #se remplazan valores para limpiar el texto
    lin = lineas[i].replace("=","")
    lin = lin.replace("  ","-")
    lin = lin.replace("\n","")
    lin = lin.replace("{","")
    lin = lin.replace("}","")
    lista.append(lin.split("-"))
    i = i + 1

#una vez limpio el texto se crean las variables de tipo lista que usara el sistema
#variable de estados  
q = lista[0][1].split(",")
#variable del alfabeto
s = lista[1][1].split(",")
#variable de estado inicial
q0 = lista[2][1].split(",")
#variable de estados finales 
f = lista[3][1].split(",")
#aplicamos un segundo filtro para obtener los estados de transicion
aux = lista[4][1]
r = aux[1:len(aux)-1].split("),(")
#creamos nuestra lista donde estan los estados de transicion
estados = []
i=0
while i < len(r):
    estados.append(r[i].split(","))
    i = i + 1
#se termina de crear la lista de estados de transicion

print('Documento leido con exito')
print("Ingrese la cadena a evaluar")
#leemos la cadena ingresada
cadena = input()
cadena = list(cadena)

#INICIO DE AFD
#al ser un afd todas las trancisiones deben existir, si una transicion no existe hay un error
#esta variable sera utilizadda para analizar si existen las trancisiones o no 
valor_encontrado = False
#usamos una variable auxiliar dodne guardamos el estado incial
estado_actual = q0[0]
#el bucle sera repetido siempre y cuando existan valores en la cadena de lo contrario se terminara 
while cadena:
    #buscamos en la cadena si los datos ingresados se encuentran en el alfabeto si esto esto no es asi se senala que hay un error en la cadena ingresada
    if(cadena[0] in s):
        #inicializamos un for para la busqueda de lesttado actual en la lista de trancisiones
        for i in range(len(estados)):
            #si el estado en el que estamos parados es igual a un valor en las trancisiones y aparte existe su trancision agregamos el valor resultante como valor actual
            if estados[i][0] == estado_actual and estados[i][1] == cadena[0]:
                #aqui actualizamos nuestro valor actual
                estado_actual = estados[i][2]
                #print(estado_actual)
                valor_encontrado = True
                break
            else:
                #en caso de que no se encuentre nada en la lista de trancisiones significa que la trancision no existe y eso es un error del automata
                valor_encontrado = False
        if valor_encontrado == True:
            #removemos el valor de la cadena ingresada que fue analizado
            cadena.remove(cadena[0])
        else:
            print("cadena invalida")
            break
    else:
        print("Un estado en la cadena no es valido")
        break

#si no se encontro una transicion marcamos como invalida la cadena
if valor_encontrado != False:
    #si el ultimo estado que fue analizado se encuentra en los estados finales maraccamos como cadena valida de lo contrario es invalida
    if estado_actual in f:
        print("cadena valida")
    else:
        print("cadena invalida")
else:
    print("cadena invalida")