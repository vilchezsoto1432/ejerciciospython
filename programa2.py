def mascaracteres(lista):
    pos=0
    for x in range(1, len(lista)):
        if len(lista[x]) > len(lista[pos]):
            pos=x
    return lista[pos]
#bloque principal
palabras=["Silla", "Sillón", "Sofá", "Armario", "Mesa", "Estanteria"]
print(palabras)
print("Palabra con mas caracteres:",mascaracteres(palabras))