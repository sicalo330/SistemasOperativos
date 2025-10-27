print("Ingrese la secuencia de referencias de páginas: ", end=" ")
memoria = input()
tamanoMarco = 3
marcos = []
orden = []  # Lleva el orden de llegada para FIFO

print(f"Secuencia: {memoria}\n{'-'*60}")

for paso, digito in enumerate(memoria, start=1):
    print("Paso " + str(paso) + ": Procesando dígito " + str(digito))
    print("------------------------------------------------------------------------------------------------------------------------")
    #Entra el if si el digito a reemplazar ya está en los marcos, simplemente no pasa nada
    if digito in marcos:
        print("HIT: el dígito " + str(digito) + " ya está en memoria.")
        print("Marcos: " + str(marcos) + " | Orden: " + str(orden) + "\n")
        continue
    #Entra al if desde el inicio, cuando la lista está vacía o si aún no se llena
    if len(marcos) < tamanoMarco:
        marcos.append(digito)
        orden.append(digito)
        print("ADD: se agrega " + str(digito) + ".")
        print("Marcos: " + str(marcos) + " | Orden: " + str(orden) + "\n")
        continue
    #Aquí va a entrar después de los primero 3 pasos, cuando ya se llenaron los marcos y el digito a reemplazar no está en los marcos
    eliminado = marcos.pop(0)  # se elimina el más antiguo (el primero que entró)
    orden.pop(0)#Se usa pop(0) para eliminar el primer elemento de la lista orden
    #Se añaden los nuevos valores en la lista marcos y orden
    marcos.append(digito)
    orden.append(digito)
    print("REPLACE: se reemplaza " + str(eliminado) + " por " + str(digito) + ".")
    print("Marcos: " + str(marcos) + " | Orden: " + str(orden) + "\n")

print("------------------------------------------------------------------------------------------------------------------------")
print("Final:")
print("Marcos: " + str(marcos) + " | Orden: " + str(orden))
