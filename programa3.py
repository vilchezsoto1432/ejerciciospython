def cargar_lista():
    lista = []
    for x in range(10):
        valor = int(input("Ingrese el valor: "))
        lista.append(valor)
    return lista


def generar_listas(lista):
    positivos = []
    negativos = []
    for x in range(len(lista)):
        if lista[x] > 0:
            positivos.append(lista[x])
        else:
            if lista[x] < 0:
                negativos.append(lista[x])
    print("Lista de valores positivos")
    print(positivos)
    print("Lista de valores negativos")
    print(negativos)

lista = cargar_lista()
generar_listas(lista)



