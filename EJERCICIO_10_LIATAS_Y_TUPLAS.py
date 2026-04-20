#EJERCICIO_10_LIATAS_Y_TUPLAS
# Escribir un programa que almacene en una lista los siguientes precios,
#  50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
numeros = []
seguir = True
i = 0
while seguir == True:
    x = int(input("introduzca un precio o precione 0 para salir: "))
    if x != 0:
        numeros.append(x)
        i += 1
    else:
        break 
if len(numeros) >= 1:
    mayor = -999999
    menor = 999999
    for j in numeros:
        if j > mayor:
            mayor = j
        if j < menor:
            menor = j
    print(f"el mayor precio es: {mayor}\nel menor precio es: {menor}")
else:
    input("no has introducido ningun precio")