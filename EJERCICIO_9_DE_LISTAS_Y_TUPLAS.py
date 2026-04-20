#EJERCICIO 9 DE LISTAS Y TUPLAS
palabra = input(f"introduzca la palabra: ")
pal = palabra.upper()
a =0
e =0
i =0
o =0
u =0
for x in range(0,len(pal)):
    if pal[x] == "A":
        a += 1
    elif pal[x] == "E":
        e += 1
    elif pal[x] == "I":
        i += 1
    elif pal[x] == "O":
        o += 1
    elif pal[x] == "U":
        u += 1
    else:
        continue
print(f"-----------------------------------\ncantidad de A: {a}\ncantidad de E: {e}\ncantidad de I: {i}\ncantidad de O: {o}\ncantidad de U: {u}")
