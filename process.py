def fifo_from_input():
    # Pedir número de procesos
    n = int(input("¿Cuántos procesos quieres ingresar? "))

    processes = []
    for i in range(n):
        name = input(f"Nombre del proceso {i+1}: ")
        llegada = int(input(f"Tiempo de llegada de {name}: "))
        rafaga = int(input(f"Ráfaga de {name}: "))
        processes.append({"name": name, "llegada": llegada, "rafaga": rafaga})

    #Ordenar por llegada
    processes.sort(key=lambda x: x["llegada"])

    time = 0
    results = []

    # Algoritmo FIFO
    for p in processes:
        #Asigna valores name, llegada y rafaga a las variables de la tupla p
        name, llegada, rafaga = p["name"], p["llegada"], p["rafaga"]
        #Basicamente si el tiempo actual es menor que el tiempo de llegada del proceso, se actualiza
        #el tiempo actual al tiempo de llegada del proceso
        if time < llegada:
            time = llegada  # esperar si aún no llegó
        start = time
        finish = start + rafaga
        tSalida = finish - llegada
        tEspera = tSalida - rafaga

        results.append({
            "name": name,
            "llegada": llegada,
            "rafaga": rafaga,
            "tInicio": start,
            "finish": finish, #Para evitar confusiones, finish es el instante en que el proceso termina
            "tEspera": tEspera,
            "tSalida": tSalida#Es el tiempo en el que el procceso estuvo en el sistema
        })
        #Sobre finish y tSalida, un proceso puede llegar en 2, tener rafaga de 4 por lo tanto termina en 6
        #Pero su tSalida es 6-2=4, es decir, estuvo 4 unidades de tiempo en el sistema
    
        time = finish

    # Mostrar tabla
    print("\nResultados FIFO:")
    print(f"{'Proceso':<8}{'Llegada':<8}{'Ráfaga':<8}{'tInicio':<8}{'Fin':<8}{'tEspera':<8}{'tSalida':<8}")
    for r in results:
        print(f"{r['name']:<8}{r['llegada']:<8}{r['rafaga']:<8}{r['tInicio']:<8}{r['finish']:<8}{r['tEspera']:<8}{r['tSalida']:<8}")


# Ejecutar
fifo_from_input()
