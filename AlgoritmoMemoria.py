def mainMenu():
    print("0. Salir")
    print("1. Añadir proceso a la lista")
    print("2. Quitar proceso de la lista")
    print("3. Cambiar proceso de la lista")
    print("Presione su opción: ", end="")

def bitReferencia():
    print("Ingrese la secuencia de referencias de páginas: ", end=" ")
    memoria = input()
    tamanoMarco = 3
    marcos = []
    bitsRef = []
    orden = []

    print(f"Secuencia: {memoria}\n{'-'*60}")

    for paso, digito in enumerate(memoria, start=1):
        print(f"Paso {paso}: Procesando dígito {digito}")
        print("----------------------------------------------------------------------------------------------------------")

        #Pasa a este if si el dígito ya está en los marcos
        if digito in marcos:
            #Se recorre todos los bits de referencia
            for i in range(len(bitsRef)):
                if marcos[i] == digito:
                    #En el caso de que el digito esté en los marcos, se agrega un 1 en la posición de la lista bitsRef
                    bitsRef[i] = 1
                else:
                    #Los demás quedan en 0, ya que no fueron referenciados
                    #Esto también evita que no haya más de un bit de referencia en 1
                    bitsRef[i] = 0

            # Mostramos el estado actual
            print("Hit: el dígito " + digito + " ya está en la memoria.")
            print("Marcos: " + str(marcos) + " | Bits: " + str(bitsRef) + " | Orden: " + str(orden) + "\n")
            #Al parecer lo que hace continue es pasar al siguiente digito de la lista marcos
            continue

        #Pasa a este if desde el inicio, cuando la lista está vacía o si aún no se llena
        if len(marcos) < tamanoMarco:
            marcos.append(digito)
            bitsRef.append(0)
            orden.append(digito)
            print(f"ADD: se agrega {digito}.")
            print(f"Marcos: {marcos} | Bits: {bitsRef} | Orden: {orden}\n")
            continue

        #Aquí va a entrar después de los primero 3 pasos, cuando ya se llenaron los marcos

        #Entra al if si el digito no tiene referencia
        #Si el primero no tiene la referencia signigica que no es el primero en la cola, por lo que se debe dejar como primero y eliminar a otro
        if bitsRef[0] == 0:
            eliminado = marcos.pop(0)
            bitsRef.pop(0)
            orden.pop(0)
            marcos.append(digito)
            bitsRef.append(0)
            orden.append(digito)
            print(f"REPLACE pop(0): reemplazando {eliminado} por {digito}.")
        else:#Si entra al else significa que el primero tiene referencia
            bitsRef[0] = 0 #Se resetea el bit de referencia del primero
            #El if else ocurre si la lista tiene más de un elemento
            if len(marcos) > 1:
                #Se elimina el segundo elemento de la lista marcos, bitsRef y orden
                eliminado = marcos.pop(1)
                bitsRef.pop(1)
                orden.pop(1)
                marcos.append(digito)#Se agrega el digito nuevo en la ultima posición de la lista marcos
                bitsRef.append(0)
                orden.append(digito)
                print(f"El primer digito tenía un bit de referencia, se reemplaza {eliminado} por {digito}")
            else:
                #Por seguridad este else permite eliminar el digito con el bit de referencia si solo hay un elemento en la lista marcos
                eliminado = marcos.pop(0)
                bitsRef.pop(0)
                orden.pop(0)
                marcos.append(digito)
                bitsRef.append(0)
                orden.append(digito)
                print(f"REPLACE borde: reemplazando {eliminado} por {digito}.")

        print("Marcos:" + str(marcos) + " | Bits: " + str(bitsRef) + " | Orden: " + str(orden) + "\n")

    print("----------------------------------------------------------------------------------------------------------")
    print("Final")
    print("Marcos:" + str(marcos) + " | Bits: " + str(bitsRef) + " | Orden: " + str(orden))

def main():
    op: int = -1
    while op != 0:
        mainMenu()
        op: str = input()
        print("\n")

        match(op):
            case '0':
                break
            case '1':
                bitReferencia()
            case '2':
                print("Caso 2:ALgoritmo de Juan")
                print("a")

            case '3':
                print("Caso 3: Algoritmo de Juan también :)")
            case _:
                input("Opción inválida, escoja otra :(")

main()

print("done")