import math
from functools import reduce


#Datos
alf="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ0123456789 ,.:!-¿?()"
longAlf = len(alf)
#Codificamos numericamente
dicNumerico = dict()
index = 0
for symbol in alf:
    dicNumerico[symbol] = index 
    index+=1

dicNumericoInverso = dict()
index = 0
for symbol in alf:
    dicNumericoInverso[index] = symbol
    index+=1

#Funciones
def claveExtendidaVigenere(keyNumeric,s,longMax,modulo):
    for i in range(s,longMax):
        newK = 0
        index = 1
        for j in range(0,s):
            newK += (keyNumeric[j]*keyNumeric[i-index])
            index+=1 
        newK = newK % modulo
        keyNumeric.append(newK)

    return keyNumeric
    
def extended_gcd(a,b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def calcularClavePrivada(e,modulo):
    gdc,clavePrivada,y = extended_gcd(e,modulo)
    if(clavePrivada < 0):
        clavePrivada = clavePrivada + modulo
    return clavePrivada

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


#Ejercicio 1 / Vigenere
key = "IMMANUEL KANT"
mensaje_cifrado="9MúqR2SXkÑRN2G?E Éfáv.úc7ú:(ÁÉ,ñ:c1ñKtÓjW2-vgrJQKMX!ÑíCIVa?!wiuf6wÓézuPC:í7kNfQLÉóI.é2Nb?réd?dGJkíSÚMñsózWMí,:-ñ82Q8IFíiKcCwKnúJ7bspvSn5YqñXomÓWbñe4ÍAfad3iám3a¿rLáG7)ÑGBXF:mbsTuÑ0)vWL ÁlgBmXRú4Jgó.G:hoéZ8SÁ?ñ5qTW8óh¿ÁILEAN,ÓZE7P(CH)2oZemVGiTQUABuBUñK6"
longCifrado=len(mensaje_cifrado)

#Extendemos la clave
keyNumeric = []
for symbol in key:
    keyNumeric.append(dicNumerico[symbol])

#Calculamos la clave extendida
claveExtendidaVigenere(keyNumeric,len(key),len(mensaje_cifrado),longAlf)

#Calculamos el mensaje
mensaje = ""
for i in range(len(mensaje_cifrado)):
    valorDescifrado = (dicNumerico[mensaje_cifrado[i]] - keyNumeric[i]) % longAlf
    index = 0
    for symbol in alf:
        if index == valorDescifrado:
            letraDescifrada = symbol
            break
        index+=1
    mensaje = mensaje + letraDescifrada
    if(len(mensaje) >= 2):
        if mensaje[-1] == " " and mensaje[-2] == " ":
            mensaje = mensaje[:-1]
            mensaje = mensaje[:-1]
            mensaje = mensaje + "\n"
    index+=1
#print(mensaje)

#Ejercicio 2 / RSA en bloque
#Pepa    
nPepa=62439738695706104201747 
ePepa=356812573 

#Benito
nBenito=743330222539755158153
eBenito=80263681
p = 27264083009
q = 27264083017

mensaje_cifrado="ñj64Íy l2ÁHxQt0 9 mLP)apHDq,Bc,PÚñl9CíwÍ-WqKzcP éAó2?LuhcaeE2ÉTyúbñ.p:ÑRRGu5hAG:ñÉu8QÚpFfo.F éñBPí5GqW:upAÁZ39víGÓíyCH3.ÉB1XIv1qcMD)Lvr-Rw1L7!-vatA0EQUzr¿o56MfC ()ÉvFrQtbTvdúóÓd)JQjÁi54aáHú1t8ÉGéQÁSLÉ:IGC797:(jÓS8lkYiGQ4ibu¿S6cPjñsñah!kú0EdoYHr8G,í!EÑ?.JH7.EwgñGfuwEJHgFít?AioXÍ!Jq.Xo7SGÓNr.9z4XhJvH1IKxCPlPFsguBRG).YUzM37Un2K2vV?Ir)ñd6UyqóYx3CmDDiDmf:iats)uPÚl1sGñúG0gdGUskajRuJ38:lÓXopipg1GAAwVlékFu:AUqáByFhBLiTkc9!MDuN2YKvIW0A9Í IU7T.QSAjQ?ÑrkáOá6N9(A,Fdñ.RyvrO-wÚ QgíZxp4L-?hJ52Yrvh4a3rB0AéH:é5qwjbYGíHc FTtqúYqR"
N = longAlf

#Clave privada del receptor
modulo= (p-1)*(q-1)
if(eBenito > modulo):
    eBenito = eBenito%modulo
clavePrivada = calcularClavePrivada(eBenito,modulo)
#Longitud de bloque
k = math.floor(math.log(nBenito,N))

#Longitud de bloque a descifrar
kDescifrar = k+1

#Descifrado
mensaje = ""
for i in range(0,len(mensaje_cifrado),kDescifrar):
    bloque = mensaje_cifrado[i:i+kDescifrar]
    enteroDescifrado = 0
    for j in range(0,len(bloque)):
        enteroDescifrado += dicNumerico[bloque[j]] * (N**(kDescifrar-j-1))

    listaCifras = []
    potenciacionModular = pow(enteroDescifrado,clavePrivada,nBenito)
    aux = 0
    for i in range(0,k):
        aux = potenciacionModular % N
        listaCifras.insert(0,aux)
        potenciacionModular = potenciacionModular // N
    for i in range(0,k):
        mensaje = mensaje + dicNumericoInverso[listaCifras[i]]
        if(len(mensaje) >= 2):
            if mensaje[-1] == " " and mensaje[-2] == " ":
                mensaje = mensaje[:-1]
                mensaje = mensaje[:-1]
                mensaje = mensaje + "\n"
   
#print(mensaje)
    
#Ejercicio 3
n_B=9641865053
e_B=70241161

nAlicia = 21962054407
eAlicia = 80263681

#factorice nAlicia
factores = factors(nAlicia)
index = 0
for x in factores:
    if index == 1:
        p = x
    if index == 2:
        q = x
    index+=1
    
Kcifrada="dÑ(.ZQe qCurdEÑKÍHfk!QEedoÓM1F"
C="yáxFMm dTlqGM!Emi9Q)7h¿iÚYymrvLúfYLÉvxnf68U0WWfÓ)p)wzRqGLú)UtÚcoQdgL l fi?(FFxEHLUz:jx7scoFÑD::mOZK?3Mf.THFUOat3ogaÉI?U0ÁPA6tyg7girF,FDÉíYkLzRú4:PPw),E!WBQT:SWí:,túVÍ:JM7ÓQn:XúLíÍ,uS1gXmNao0eKzÓjÁ:x3OmóI09AnkA:?ÑIDg17(AXoXFGHc6(q75rWO!"

#Desciframos la clave
#Clave privada del receptor
modulo= (p-1)*(q-1)
if(eAlicia > modulo):
    eAlicia = eAlicia%modulo

clavePrivada = calcularClavePrivada(eAlicia,modulo)
#Longitud de bloque
k = math.floor(math.log(nAlicia,N))

#Longitud de bloque a descifrar
kDescifrar = k+1

#Descifrado de K*
mensaje = ""
for i in range(0,len(Kcifrada),kDescifrar):
    bloque = Kcifrada[i:i+kDescifrar]
    enteroDescifrado = 0
    for j in range(0,len(bloque)):
        enteroDescifrado += dicNumerico[bloque[j]] * (N**(kDescifrar-j-1))

    listaCifras = []
    potenciacionModular = pow(enteroDescifrado,clavePrivada,nAlicia)
    aux = 0
    for i in range(0,k):
        aux = potenciacionModular % N
        listaCifras.insert(0,aux)
        potenciacionModular = potenciacionModular // N
    for i in range(0,k):
        mensaje = mensaje + dicNumericoInverso[listaCifras[i]]
        if(len(mensaje) >= 2):
            if mensaje[-1] == " " and mensaje[-2] == " ":
                mensaje = mensaje[:-1]
                mensaje = mensaje[:-1]
                mensaje = mensaje + "\n"
print(mensaje)

#Descifrado de C con Vigenere
key = mensaje
longCifrado=len(C)
#Extendemos la clave
keyNumeric = []
for symbol in key:
    keyNumeric.append(dicNumerico[symbol])
#Calculamos la clave extendida
claveExtendidaVigenere(keyNumeric,len(key),len(C),longAlf)
#Calculamos el mensaje
mensaje = ""
for i in range(len(C)):
    valorDescifrado = (dicNumerico[C[i]] - keyNumeric[i]) % longAlf
    index = 0
    for symbol in alf:
        if index == valorDescifrado:
            letraDescifrada = symbol
            break
        index+=1
    mensaje = mensaje + letraDescifrada
    if(len(mensaje) >= 2):
        if mensaje[-1] == " " and mensaje[-2] == " ":
            mensaje = mensaje[:-1]
            mensaje = mensaje[:-1]
            mensaje = mensaje + "\n"
    index+=1
print(mensaje)

#Cifrar
mensaje_cifrado = "GACELA DE LA TERRIBLE PRESENCIA (Federico García Lorca, 1898-1936)"
key = "MARTE"
longCifrado=len(mensaje_cifrado)
#Extendemos la clave
keyNumeric = []
for symbol in key:
    keyNumeric.append(dicNumerico[symbol])
#Calculamos la clave extendida
claveExtendidaVigenere(keyNumeric,len(key),len(C),longAlf)
#Calculamos el mensaje
mensaje = ""
for i in range(len(mensaje_cifrado)):
    valorDescifrado = (dicNumerico[C[i]] + keyNumeric[i]) % longAlf
    index = 0
    for symbol in alf:
        if index == valorDescifrado:
            letraDescifrada = symbol
            break
        index+=1
    mensaje = mensaje + letraDescifrada
    if(len(mensaje) >= 2):
        if mensaje[-1] == " " and mensaje[-2] == " ":
            mensaje = mensaje[:-1]
            mensaje = mensaje[:-1]
            mensaje = mensaje + "\n"
    index+=1
print(mensaje)
