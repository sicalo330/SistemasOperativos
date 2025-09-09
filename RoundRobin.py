class Proceso:
    def __init__(self, tFase: int, tInicial: int, nombre: str):
        self.tFase: int = tFase # tiempo que toma el proceso en la CPU
        self.tInicial: int = tInicial # Tiempo en que llega el proceso a la CPU
        self.tActivo: int = 0
        self.nombre: str = nombre
    
    def __str__(self):
        s = ""
        if self.nombre != "":
            s += "nombre: " + self.nombre + "\n"
        s += "tiempo restante: " + str(self.tFase) + ", tiempo de llegada: " + str(self.tInicial) + "\n"
        s += "Tiempo activo: " + str(self.tActivo)
        return s

class RoundRobin:
    def __init__(self, Q: int):
        self.Q: int = Q # Q de Quantum. Tiempo máximo por proceso
        self.procesos: list[Proceso] = [] # Procesos que está haciendo el algoritmo
        self.t: int = 0 # Instante de tiempo actual

    def encolarProcesos(self, lProcesos: list[Proceso]): # mete procesos nuevos a la fila de acuerdo a su tiempo inicial y al instante actual de tiempo
        for p in lProcesos:
            if p.tInicial == self.t:
                self.procesos.append(p)
    
    def avanzar(self, lProcesos: list[Proceso]): # avanza un instante de tiempo gestionando acordemente los procesos de la lista
        # chequear encolar
        self.encolarProcesos(lProcesos)

        if len(self.procesos) > 0: # Si la lista no está vacía
            # chequear desencolar
            self.procesos[0].tFase -= 1
            if self.procesos[0].tFase <= 0:
                self.procesos.pop(0)

            # chequear reencolar
            else:
                self.procesos[0].tActivo += 1 # aumenta su tiempo activo
                if self.procesos[0].tActivo == self.Q:
                    self.procesos[0].tActivo = 0
                    self.procesos.append(self.procesos.pop(0))

        # avanzar al siguiente instante
        self.t += 1
    
    def mostarEstatus(self):
        print("Instante de tiempo actual: " + str(self.t) + "\n")
        if len(self.procesos) > 0:
            i: int = 1
            for p in self.procesos:
                print(str(i) + ") " + str(p))
                print("\n")
                i += 1
        else:
            print("Descansando...")

def mainMenu():
    print("Algoritmo Round Robin")
    print("0. Salir")
    print("1. Añadir proceso a la lista")
    print("2. Quitar proceso de la lista")
    print("3. Cambiar proceso de la lista")
    print("4. Ver lista")
    print("5. Borrar lista")
    print("6. Correr algoritmo")
    print("Presione su opción: ", end="")

def RRMenu():
    print("Ejecutando Round Robin")
    print("0. Parar algoritmo")
    print("1. Avanzar un instante")
    print("2. Mostrar cola y estado de procesos")
    print("Presione su opción: ", end="")

def crearProceso() -> Proceso:
    print("Añadiendo proceso")
    proceso = Proceso(0, 0, "")
    proceso.tFase = int(input("Escriba el tiempo de fase: "))
    proceso.tInicial = int(input("Escriba el tiempo de llegada: "))
    proceso.nombre = input("Escriba un nombre para el proceso si desea: ")
    return proceso

def main():
    procs: list[Proceso] = []
    op: int = -1

    while op != 0:
        mainMenu()
        op: str = input()
        print("\n")

        match(op):
            case '0':
                break
            case '1':
                proceso = crearProceso()
                print("Especifique la posición del proceso en la lista si desea.")
                print("Longitud actual de la lista de procesos: " + str(len(procs)))
                pos = input("(Si se sale del rango o si no especifica se pondrá al final): ")
                if pos == "" or int(pos) not in range(0, len(procs)):
                    procs.append(proceso)
                else:
                    procs.insert(int(pos), proceso)
                input("Proceso ingresado :)")
            case '2':
                if len(procs) > 0:
                    print("Especifique la posición del proceso a eliminar en la lista si desea.")
                    print("Longitud actual de la lista de procesos: " + str(len(procs)))
                    pos = input("(Si se sale del rango o si no especifica se eliminará el primero): ")
                    if pos == "" or int(pos) not in range(0, len(procs)):
                        procs.pop(0)
                    else:
                        procs.pop(int(pos))
                    input("Proceso eliminado :)")
                else:
                    input("Nada que eliminar :l")
            case '3':
                if len(procs) > 0:
                    print("Especifique la posición del proceso a modificar en la lista si desea.")
                    print("Longitud actual de la lista de procesos: " + str(len(procs)))
                    pos = input("(Si se sale del rango o si no especifica no se modificará ninguno): ")
                    if pos != "" and int(pos) in range(0, len(procs)):
                        procs[int(pos)].tFase = input("Modifique el tiempo de fase: ")
                        procs[int(pos)].tInicial = input("Modifique el tiempo de llegada: ")
                        procs[int(pos)].nombre = input("Modifique el nombre: ")
                        print("Modifique la posición del proceso en la lista si desea.")
                        print("Longitud actual de la lista de procesos: " + str(len(procs)))
                        pos2 = input("(Si se sale del rango o si no especifica no se reposicionará): ")
                        if pos2 != "" and int(pos2) in range(0, len(procs) - 1):
                            procs.insert(int(pos2), procs.pop(int(pos)))
                        input("Proceso modificado :)")
                    else:
                        input("Nada fue modificado :)")

                else:
                    input("No hay nada para cambiar :l")
            case '4':
                if len(procs) > 0:
                    i = 1 # i de índice
                    for p in procs:
                        print(str(i) + ") ", end="")
                        if p.nombre != "":
                            print("nombre: " + p.nombre + ", ",end="")
                        print("tiempo de fase: " + str(p.tFase) + ", tiempo de llegada: " + str(p.tInicial))
                        i += 1
                else:
                    print("Lista vacía :o")
                input("presione para continuar :)")
            case '5':
                if input("Presione 0 para confirmar: ") == '0':
                    procs.clear()
                    input("Lista vaciada :l")
                else:
                    input("Lista salvada =l")
            case '6':
                op2: int = -1
                rr = RoundRobin(int(input("Ingresa el quantum: ")))
                print("\n")
                while op2 != 0:
                    RRMenu()
                    op2 = int(input())
                    print("\n")

                    match(op2):
                        case 0:
                            input("Algoritmo cancelado :l")
                            break
                        case 1:
                            rr.avanzar(procs)
                            input("instante " + str(int(rr.t - 1)) + " -> " + str(int(rr.t)) + ". Presione para continuar...")
                        case 2:
                            rr.mostarEstatus()
                            input("Presione para continuar...")
                        case _:
                            input("Opción inválida :l")

            case _:
                input("Opción inválida, escoja otra :(")

main()