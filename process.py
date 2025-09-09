def fifo_from_input():
    # Pedir número de procesos
    n = int(input("¿Cuántos procesos quieres ingresar? "))

    processes = []
    for i in range(n):
        name = input(f"Nombre del proceso {i+1}: ")
        arrival = int(input(f"Tiempo de llegada de {name}: "))
        burst = int(input(f"Ráfaga de {name}: "))
        processes.append({"name": name, "arrival": arrival, "burst": burst})

    # Ordenar por llegada
    processes.sort(key=lambda x: x["arrival"])

    time = 0
    results = []

    # Algoritmo FIFO
    for p in processes:
        name, arrival, burst = p["name"], p["arrival"], p["burst"]
        if time < arrival:
            time = arrival  # esperar si aún no llegó
        start = time
        finish = start + burst
        turnaround = finish - arrival
        waiting = turnaround - burst

        results.append({
            "name": name,
            "arrival": arrival,
            "burst": burst,
            "tInicio": start,
            "finish": finish,
            "tEspera": waiting,
            "tSalida": turnaround
        })

        time = finish

    # Mostrar tabla
    print("\nResultados FIFO:")
    print(f"{'Proceso':<8}{'Llegada':<8}{'Ráfaga':<8}{'tInicio':<8}{'Fin':<8}{'tEspera':<8}{'tSalida':<8}")
    for r in results:
        print(f"{r['name']:<8}{r['arrival']:<8}{r['burst']:<8}{r['tInicio']:<8}{r['finish']:<8}{r['tEspera']:<8}{r['tSalida']:<8}")


# Ejecutar
fifo_from_input()
