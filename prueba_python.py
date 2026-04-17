def primo(num):
    if num == 2:
        return True
    elif num%2==0:
        return False
    else:
        cont = 0
        a = int(num**0.5)
        for aux in range(1,a+1):
            if num%aux==0:
                cont += 1
        if cont > 1:
            return False
        else:
            return True
print ("esta funcion toma un rango de numeros y muestra todos los \n numeros primos contenidos en ese rango")
a = int(input("introduce el inicio del rango: "))
b = int(input("introduce el final del rango: "))
condicion = False
while condicion == False:
    if a < b:
        condicion = True
        print (f"los numeros primos que hay entre {a} y {b} son: ")
        for i in range(a, b):
            if primo(i + 1):
                    print(i + 1, end=", ")
    else:
        print(f"\n---------------------------\nel numero final debe ser mayor que el inicial\n-----------------------------")
        a = int(input("introduce el inicio del rango: "))
        b = int(input("introduce el final del rango: "))



