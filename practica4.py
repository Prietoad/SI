import math as ma
import numpy as np
import textwrap

#Ejercicio de decodificacion lineal y decodificacion fuente
#Ejercicio 1
#Fuente
fuente='''La canica gira entre mis dedos en el fondo del bol-
sillo. Es mi preferida, nunca me separo de ella. Y
lo bueno es que es la más fea de todas, no se pa-
rece en nada a las de ágata, o a las grandes canicas metá-
licas que suelo mirar en el escaparate de la tienda del tío
Ruben, en la esquina de la calle Ramey.'''
def calcularFrecuencias(source):
    freq = {}
    for symbol in source:
        if(symbol == "\n"):
            if " " in freq:
                freq[" "] += 2
            else:
                freq[" "] = 2
        else:
            if symbol in freq:
                freq[symbol] += 1
            else:
                freq[symbol] = 1
    return freq

dicFreq = calcularFrecuencias(fuente)
symbols=[]
for i in dicFreq:
    symbols.append(i)

A= [[1,0,1,0,1,1,1,1],
[0,1,1,1,0,1,1,1],
[1,1,0,1,1,1,1,1],
[0,1,1,0,1,1,1,0]]

L=[1,0,0,1,1,1,0,0,0,0,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,1,0,0,1,0,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,1,0,0,1,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0]

#Decodificacion lineal
#Cogemos los valores sobrantes
filas = len(A)
columnas = len(A[1])

resto =  len(L)%12
print(resto)
lastArray = []
lastArray.append(L[-1])
L.pop(-1) 


#Numero de divisiones de seis digitos
divisionesNum = len(L)/12
#Dividimos el mensaje codificado en el numero de divisiones de 6
divisiones= []
divisiones = np.array_split(L,divisionesNum)
#Cogemos los tres primeros valores de cada division de 6
codificacion = ""
for array in divisiones:
    division3 = ""
    for i in range(0,filas):
        division3 = division3 + str(array[i])
    codificacion = codificacion + division3
#Añadimos los valores sobrantes al conjunto
for i in lastArray:
    codificacion = codificacion + str(i)
#Dividimos el conjunto anterior en la longitud minima de cada palabra
#Longitud minima para esta fuente (se redondea al entero superior mas cercano)
minLong = ma.ceil(ma.log(len(symbols),2))
divisiones7 = textwrap.wrap(codificacion,minLong)
#Convertimos cada division a base 10 y utilizamos ese numero como posicion en el alfabeto para conseguir el simbolo decodificado
frase = ""
for division in divisiones7:
    #Decodificacion fuente
    numero = int(division,2)
    frase = frase + symbols[numero]

#Mensaje decodificado
print(frase)

#Ejercicio 2




