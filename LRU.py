print("Ingrese la secuencia de referencias de páginas: ", end=" ")
memoria = input()
tamanoMarco = 3
marcos = []
uso_reciente = []  # Mantiene el orden de uso (de menos a más reciente)

print(f"Secuencia: {memoria}\n{'-'*60}")

for i in range(len(memoria)):
    digito = memoria[i]
    paso = i + 1
    print(f"Paso {paso}: Procesando dígito {digito}")
    print("-" * 100)

    # Caso 1: HIT (ya está en memoria)
    if digito in marcos:
        # Actualizamos el orden de uso: lo quitamos y lo ponemos al final
        uso_reciente.remove(digito)
        uso_reciente.append(digito)
        print(f"HIT: el dígito {digito} ya está en memoria.")
        print(f"Marcos: {marcos} | Uso reciente: {uso_reciente}\n")
        continue

    # Caso 2: Aún hay espacio en los marcos
    if len(marcos) < tamanoMarco:
        marcos.append(digito)
        uso_reciente.append(digito)
        print(f"ADD: se agrega {digito}.")
        print(f"Marcos: {marcos} | Uso reciente: {uso_reciente}\n")
        continue

    # Caso 3: Reemplazo LRU
    menos_usado = uso_reciente.pop(0)  # el que menos se ha usado (primer elemento)
    index = marcos.index(menos_usado)
    marcos[index] = digito  # reemplazamos esa página
    uso_reciente.append(digito)  # el nuevo se considera el más reciente
    print(f"REPLACE: se reemplaza {menos_usado} por {digito}.")
    print(f"Marcos: {marcos} | Uso reciente: {uso_reciente}\n")

print("-" * 100)
print("Final:")
print(f"Marcos: {marcos} | Uso reciente: {uso_reciente}")
