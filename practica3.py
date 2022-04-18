from decimal import *
import numpy as np

getcontext().prec = 500

#Funcion que calcula las frecuencias de una fuente
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

#Funcion que calcula las probabilidades de una fuente
def calcularProbabilidades(freq, source):
    total = 0
    prob = {}
    for i in source:
        if( i =="\n"):
            total = total + 2
        else: 
            total= total + 1

    for symbol in freq:
        prob[symbol] =freq[symbol]/total
    return prob

#Funcion que devuelve un diccionario con los intervalos de una fuente
def calcularIntervalos(dicProbabilidades, symbols):
    dicIntervalos={}
    L = 0
    H = dicProbabilidades[symbols[0]]
    for i in range(0,len(symbols)):
        intervalo = [L,H]
        dicIntervalos[symbols[i]] = intervalo
        L = H
        if(i+1 < len(symbols)):
            H = L + dicProbabilidades[symbols[i+1]]
    return  dicIntervalos

#Algoritmo que decodifica y crea el mensaje
def decodificar(dicIntervalos, num, longitudMsj):
    mensaje = ""
    for i in range(0,longitudMsj):
    #Intervalo en el que se encuenta el num
        for symbol in dicIntervalos:
            intervalo = dicIntervalos[symbol]
            if(num >= intervalo[0] and num <= intervalo[1]):
                mensaje = mensaje + symbol
                L = intervalo[0]
                H = intervalo[1]
                #Convertimos num al intervalo [0,1]
                numerador = Decimal(num - Decimal(L))
                denominador = Decimal(H - L)
                
                num = Decimal(numerador/denominador)
                #print(Decimal(num.numerator)/Decimal(num.denominator))
                break
    return mensaje

#Funcion que calcula la entropia de una fuente
def entropia(freq,source):
    total = 0
    for i in source:
        if( i =="\n"):
            total = total + 2
        else: 
            total= total + 1
    sumatorio = 0
    for symbol in freq:
        paso = freq[symbol]*np.log(freq[symbol])
        sumatorio += paso
    entropia = round(1/np.log(2)*(np.log(total)-1/total*sumatorio),9)
    return entropia

#Ejercicio 1
#Datos iniciales
fuente = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ."
dicProbabilidades = {}
dicIntervalos = {}
num = Decimal('0.1613657607216723798346110583')
longitudMsj = 19
mensaje = ""

#Diccionario de probabilidades
for symbol in fuente:
    lon = len(fuente)
    dicProbabilidades[symbol] = Decimal(1)/Decimal(len(fuente))

#Diccionario de intervalos
dicIntervalos = calcularIntervalos(dicProbabilidades,fuente)

#Algoritmo de decodificacion      
#print(decodificar(dicIntervalos,num,longitudMsj) + "\n")

#Ejercicio 2
#Datos iniciales
num = Decimal('0.247276109705412160222')
longitudMsj = 17
mensaje = ""
dicFrecuencias = {}
dicProbabilidades = {}
dicIntervalos = {}

#Leemos la fuente
fuenteTexto = '''La canica gira entre mis dedos en el fondo del bol-
sillo. Es mi preferida, nunca me separo de ella. Y
lo bueno es que es la más fea de todas, no se pa-
rece en nada a las de ágata, o a las grandes canicas metá-
licas que suelo mirar en el escaparate de la tienda del tío
Ruben, en la esquina de la calle Ramey.'''
symbols = []

#Calculamos probabilidades
dicFrecuencias = calcularFrecuencias(fuenteTexto)
dicProbabilidades = calcularProbabilidades(dicFrecuencias,fuenteTexto)

#Lista de simbolos unicos
for i in dicProbabilidades:
    symbols.append(i)

print(symbols)
#Diccionario de intervalos
#dicIntervalos = calcularIntervalos(dicProbabilidades,symbols)

#Entropia
print(entropia(dicFrecuencias,fuenteTexto))

#Algoritmo de decodificacion      
#print(decodificar(dicIntervalos,num,longitudMsj) + "\n")

