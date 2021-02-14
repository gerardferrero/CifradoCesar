#Ave César

def cifrar(mensaje,clave):
    resultado = ""
    for letra in mensaje:
        if letra == " ":
            resultado = resultado + " "
        else:
            resultado = resultado + abecedario[(abecedario.find(letra)+clave)%len(abecedario)]
    
    return resultado



def descifrar(mensaje,clave):
    resultado = ""
    for letra in mensaje:
        if letra == " ":
            resultado = resultado + " " 
        else:
            resultado = resultado + abecedario[(abecedario.find(letra)-clave)%len(abecedario)]

    return resultado



abecedario = "abcçdefghijklmnñopqrstuvwxyzABCÇDEFGHIJKLMNÑOPQRSTUVWXYZ*/&%$()=+-_.,:;?¿¡!@#"

print ("1. Cifrar/descifrar con clave")
print ("2. Descifrar mensaje sin clave")

opcion = input("Elija opción: ")

if opcion == "1":
    opcion = input("Elija cifrar o descifrar[C/D]: ")
    mensaje = input("Introduzca el mensaje: ")
    clave = int(input("Introduzca la clave: "))



    if opcion == "C":
        print(cifrar(mensaje,clave))
    elif opcion == "D":
        print(descifrar(mensaje,clave))

elif opcion == "2":
    fichero = open("palabras_español.txt","r")
    diccionario = []
    for linea in fichero:
        diccionario.append(linea.strip('\n'))

    mensaje_cifrado = input("Introduzca el mensaje a descifrar: ")

    lista_palabras = mensaje_cifrado.split(" ")
    clave_obtenida = 0
    contador_maximo = 0
    for clave in range(1,len(abecedario)):
        contador = 0
        print (f"Probando clave {clave}...  ",end="")
        for palabra in lista_palabras:
            if descifrar(palabra,clave) in diccionario:
                contador = contador + 1
        if contador > contador_maximo:
            contador_maximo = contador
            clave_obtenida = clave
        print (f"Contador de palabras descifradas = {contador}")


    print (f"La clave obtenida es: {clave_obtenida}")
    print (f"El mensaje descifrado es: {descifrar(mensaje_cifrado,clave_obtenida)}")