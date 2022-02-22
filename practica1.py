#imports
import itertools
import math as ma
import numpy as np
from numpy import true_divide

#Lee el archivo de texto
f = open("datos_1.txt")

#Listas
listAll= []
listSymbols = []
listNumber = []
listProbabilidades = []

#Llenamos la lista con todos los simbolos y la lista con los simbolos unicos
for symbol in itertools.chain.from_iterable(f):
    if(symbol not in listSymbols and symbol != "\n"):
        listSymbols.append(symbol)
    if(symbol =="\n"):
        listAll.append(" ")
        listAll.append(" ")
    listAll.append(symbol)

#Contamos las apariciones de cada simbolo
for symbol in listSymbols:
    num = listAll.count(symbol)
    listNumber.append(num)

#Contamos el numero total de apariciones
count = 0
for num in listNumber:
    count = count + num

#Llenamos la lista con las probabilidades de cada simbolo
for num in listNumber:
    listProbabilidades.append(num/count)

#Imprimimos la probabilidad y frecuencia de la d
for i in range(len(listSymbols)):
    if(listSymbols[i] == 'd'):
        print("d: Frecuencia = " + str(listNumber[i]) + " Probabilidad = " + str(round(listProbabilidades[i],4)))
#Calculamos la entropia
i=0
sumatorio = 0
for symbol in listSymbols:
    paso = listNumber[i]*np.log(listNumber[i])
    sumatorio = sumatorio + paso
    i+=1
entropia = round(1/np.log(2)*(np.log(count)-1/count*sumatorio),4)

print("Entropia: " + str(entropia))

#Ordenamos todas las listas
for j in range (len(listProbabilidades)):
    swapped = False
    i = 0
    while i<len(listProbabilidades)-1:
        if listProbabilidades[i] < listProbabilidades[i+1]:
            listProbabilidades[i],listProbabilidades[i+1] = listProbabilidades[i+1],listProbabilidades[i]
            listSymbols[i],listSymbols[i+1] = listSymbols[i+1],listSymbols[i]
            listNumber[i],listNumber[i+1] = listNumber[i+1],listNumber[i]
            swapped = True
        i=i+1
    if swapped ==False:
        break

#Imprimimos los cuatro primeros simbolos con sus frecuencias absolutas y probabilidades
for i in range(0,4):
    roundValue = round(listProbabilidades[i],4)
    print(str(listSymbols[i]) + " " + str(listNumber[i]) + " " + str(roundValue))

#Cierra el archivo
f.close()
