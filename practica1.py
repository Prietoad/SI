#imports
import itertools
import math as ma
import numpy as np
from numpy import true_divide

#Funcion que cuenta el numero de apariciones de cada simbolo de la fuente y lo guarda en una lista
def countAppereances(fuente,listNum,listSymbols):
    for symbol in listSymbols:
        num = fuente.count(symbol)
        listNum.append(num)

#Lee el archivo de texto
f = open("datos_1.txt")
fuente = f.read()

#Listas
listAll= []
listSymbols = []
listNumber = []
listProbabilidades = []

#Llenamos la lista con todos los simbolos y la lista con los simbolos unicos
for symbol in fuente:
    if(symbol not in listSymbols and symbol != "\n"):
        listSymbols.append(symbol)
    if(symbol =="\n"):
        listAll.append(" ")
        listAll.append(" ")
    else:
        listAll.append(symbol)

#Contamos las apariciones de cada simbolo
countAppereances(listAll,listNumber,listSymbols)

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

#Extra
listAll2 = []
listSymbols2 = []
listNumber2 = []
listProbabilidades2 = []

#Llenamos la lista con todos los simbolos de dos en dos y la lista con los simbolos unicos de dos en dos
f = open("datos_1.txt")
fuente2 = f.read()

for i in range(0,len(fuente2)+2,2):
    symbol = listAll[i]+listAll[i+1]
    listAll2.append(symbol)

for i in range(0,len(listAll2)):
    symbol = listAll2[i]
    if(symbol not in listSymbols2):
        listSymbols2.append(symbol)
    
#Contamos las apariciones de cada simbolo
countAppereances(listAll2,listNumber2,listSymbols2)

#Aparaciones totales
count = count/2

#Llenamos la lista con las probabilidades de cada simbolo
for num in listNumber2:
    listProbabilidades2.append(num/count)

#Calculamos la entropia
i=0
sumatorio = 0
for symbol in listSymbols2:
    paso = listNumber2[i]*np.log(listNumber2[i])
    sumatorio = sumatorio + paso
    i+=1
entropia = round(1/np.log(2)*(np.log(count)-1/count*sumatorio),4)

#Ordenamos todas las listas
for j in range (len(listProbabilidades2)):
    swapped = False
    i = 0
    while i<len(listProbabilidades2)-1:
        if listProbabilidades2[i] < listProbabilidades2[i+1]:
            listProbabilidades2[i],listProbabilidades2[i+1] = listProbabilidades2[i+1],listProbabilidades2[i]
            listSymbols2[i],listSymbols2[i+1] = listSymbols2[i+1],listSymbols2[i]
            listNumber2[i],listNumber2[i+1] = listNumber2[i+1],listNumber2[i]
            swapped = True
        i=i+1
    if swapped ==False:
        break

#Imprimimos las cuatro primeras  
print("\nExtra: \nEntropia: " + str(entropia))
for i in range(0,4):
    roundValue = round(listProbabilidades2[i],5)
    print(str(listSymbols2[i]) + " " + str(listNumber2[i]) + " " + str(roundValue))


