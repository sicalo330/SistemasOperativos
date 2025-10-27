print("Ingrese la secuencia de referencias de páginas: ", end=" ")
memoria = input()
tamanoMarco = 3
marcos = []
usoReciente = []#Mantiene el orden de uso (de menos a más reciente)

print("Secuencia: " + str(memoria) + "\n")
print("----------------------------------------------------------------------------------------------------------")

for i in range(len(memoria)):
    digito = memoria[i]
    paso = i + 1
    print("Paso " + str(paso) + ": Procesando dígito " + str(digito))
    print("----------------------------------------------------------------------------------------------------------")

    #Caso en el que el digito está en memoria
    if digito in marcos:
        #Actualizamos el orden de uso, se quita de la lista usoReciente y lo ponemos al final
        usoReciente.remove(digito)
        usoReciente.append(digito)
        print("El dígito " + str(digito) + " ya está en memoria.")
        print("Marcos: " + str(marcos) + " | Uso reciente: " + str(usoReciente) + "\n")
        continue

    #Entra al if desde el inicio, cuando la lista está vacía o si aún no se llena
    if len(marcos) < tamanoMarco:
        marcos.append(digito)
        usoReciente.append(digito)
        print("Se agrega " + str(digito) + ".")
        print("Marcos: " + str(marcos) + " | Uso reciente: " + str(usoReciente) + "\n")
        continue

    #Aquí se hace el intercambio del digito
    menosUsado = usoReciente.pop(0) #el que menos se ha usado (primer elemento)
    index = marcos.index(menosUsado)#Se toma el primer digito de la lista marcos, y se busca el índice en marcos
    marcos[index] = digito#Se reemplaza tomando el índice de la lista 
    usoReciente.append(digito)#El nuevo se considera el más reciente
    print("Se reemplaza " + str(menosUsado) + " por " + str(digito) + ".")
    print("Marcos: " + str(marcos) + " | Uso reciente: " + str(usoReciente) + "\n")

print("----------------------------------------------------------------------------------------------------------")
print("Final:")
print("Marcos: " + str(marcos) + " | Uso reciente: " + str(usoReciente))
