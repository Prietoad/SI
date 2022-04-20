#Datos
alf = "aábcdeéfghiíjklmnñoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ0123456789 ,.:-()"
cifrado = "ÁeóÍ ebá 5b-CeóÍósUÍCs sÍ2UeÍÚLVVpt)utÍoáÍez2ehÍÍíN1mX-ñjA1E-OmimjX-wOyimj3wPFé13iAimÚj-mj31-OXwÚjF-OwjjbmYf2áUspY7ÍíPomY íYy3KYí ÚoPbbmEYÓ YP:3mbYyÁLÁYY4v6z6(znmsnzh(v:6zW6fW6zvoz(vóp-z6(6MpWÉzxpOFpzzÍ.íÍa3ñcahuiÍa.Í3uV Ía,ua úc.uVáúua3ñca5y(Zj9aa)r7NOFyWOwóyOÁNuukYóRYOKyRYKdRkÁy(OOIiPúGTókCF5yaó95FCyCsaTó)aQAQóiZGZ("
a = 64
b = 5
aAux = a
bAux = b
#Decodificacion
#Conseguimos la clave de descifrado inicial
modulo = len(alf)
aInverso = pow(aAux,-1,modulo)
fila = 1
mensaje = ""
#Decodificamos los mensajes
for letter in cifrado:
    #Valor de n cifrado
    nPrima = alf.index(letter)
    #Clave descifrado
    aInverso = pow(aAux,-1,modulo)
    aDesc = (aInverso)%modulo
    bDesc = (-bAux*aInverso)%modulo
    n = (aDesc * nPrima  + bDesc) % modulo
    mensaje = mensaje + alf[n]
    #Comprobamos si hay que cambiar de fila
    if len(mensaje) > 2 and mensaje[-1] == " " and mensaje [-2] == " ":
        fila += 1
        mensaje = mensaje[:len(mensaje)-2]
        mensaje = mensaje + "\n"
    #Clave cifrado
    aAux = (a ** fila) % modulo
    bAux = (b * fila) % modulo

#Imprimimos el mensaje descifrado 
print(mensaje)
