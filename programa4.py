def carga_sueldo():
    sueldos=[]
    for x in range(5):
        s=int(input("ingrese el sueldo del empleados: "))
        sueldos.append(s)
    return sueldos


def imprimir(base):
    for x in range(len(base)):
        print(base[x])

def rango_mayor(base):
    tasa=0
    for x in range(len(base)):
        if base[x]>=100:
            tasa=tasa+1
    print("el numero de personas con sueldos mayor a 100 son:",tasa)

def promedio(base):
    cc=0
    for x in range(len(base)):
        cc=cc+base[x]
    pt=cc/int(len(base))
    print("el promedio de los sueldos es: ",pt)
    for z in range(len(base)):
        if base[z]<pt:
            print(base[z])

base=carga_sueldo()
imprimir(base)
rango_mayor(base)
promedio(base)