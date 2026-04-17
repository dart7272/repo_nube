from herramientas import Validador
lector = Validador()
print ("esta funcion toma un rango de numeros y muestra todos los \n numeros primos contenidos en ese rango")
a = lector.veri_num(input("Introduce el inicio del rango: "))
b = lector.veri_num(input("Introduce el final del rango: "))
condicion = False
while condicion == False:
    if a < b:
        condicion = True
        print (f"los numeros primos que hay entre {a} y {b} son: ")
        for i in range(a, b):
            if lector.primo(i + 1):
                    print(i + 1, end=", ")
    else:
        print(f"\n---------------------------\nel numero final debe ser mayor que el inicial\n-----------------------------")
        ia = int(input("introduce el inicio del rango: "))
        ib = int(input("introduce el final del rango: "))



