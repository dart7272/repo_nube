def primo(num):
    if num%2==0:
        return False
    else:
        cont=0
        for aux in range(1,9):
            if num%aux==0:
                cont +1
        if cont >=3:
            return False
        else:
            return True
print ("esta funcion toma un rango de numeros y muestra todos los \n numeros primos contenidos en ese rango")
a = int(input("introduce el inicio del rango: "))
b = int(input("introduce el final del rango: "))
print (f"los numeros primos que hay entre {a} y {b} son: ")
for i in range(a, b):
	if primo(i + 1):
			print(i + 1, end=", ")
print()


