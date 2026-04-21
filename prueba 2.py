#DICCIONARIO
import os

def limpiar_pantalla():
    # 'nt' es para Windows, 'posix' para Linux/macOS
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Llamada a la función
limpiar_pantalla()
#   EJERCICIO 1:
# monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# m=input ("intruduzca divisa: ")
# if m.title() in monedas:
#     print( monedas[m.title()])
# else:
#     print ("moneda no reistrada")

#   EJERCICIO 2:
# n = int (input("digite un numero: "))
# if n % 2 == 0:
#     print ("el numero no es primo")
# else:
#     x = n ** 0.5
#     i=1
#     cont=0
#     while i <= x:
#         if (n%i == 0):
#             cont+=1
#         i+=1
#     if cont > 1:
#         print("el numero no es primo")
#     else:
#         print("el numero es primo")
#EJERCICIO 3:
# cad = input ("escriba una palabra: ")
# print(cad[::-1])
#EJERCICIO 4:
# tup = (1,2,3,4,5,6,7,8,9,10)
# print (tup[::-1])
#EJERCICIO 5:
# materias = ["matematicas", "fisica", "quimica", "historia", "lengua"]
# reprovadas = []
# for materias in materias:
#     nota = float(input(f"nota de {materias}: "))
#     if nota < 10:
#         reprovadas.append(materias)
# for reprovada in reprovadas:
#     print (f"debes repetir: {reprovada}")
# EJERCICIO 6:
# cesta = {}
# fin = False
# while fin == False:
#     articulo = input ("Articulo: ")
#     precio = float(input(f"precio de {articulo}: "))
#     cesta [articulo] = precio
#     op = input ("quieres seguir anadiendo articulos? (s/n): ")
#     if op == "n" or op == "N":
#         fin = True
#     elif op == "s" or op == "S":
#         fin = False
# print ("lista de compras: \n")        
# for articulo, precio in cesta.items():
#     print (f{articulo}---------{precio}$\n")
# def registrar_cli (dic_clientes, dic_preferentes):
#     limpiar_pantalla()
#     cedula = input("cedula de cliente: ")
#     nombre = input("nombre del cliente: ")
#     direccion = input("direccion del cliente: ")
#     telefono = input("telefono del cliente: ")
#     correo = input("correo del cliente: ")
#     p = input("el cliente es preferente? (s/n): ")
#     if p == "s" or p == "S":
#         preferente = True
#     elif p == "n" or p == "N": 
#         preferente = False
#     datos = {
#         "nombre" : nombre,
#         "direccion" : direccion,
#         "telefono" : telefono,
#         "correo" : correo,
#         "preferente" : preferente
#     }
#     dic_clientes[cedula] = datos
#     if preferente :
#         dic_preferentes[cedula] = datos
#     input ("cliente registrado con exito!")
# def eliminar_cli(dic_clientes, dic_preferentes):
#     limpiar_pantalla()
#     c = input("cedula del cliente a eliminar: ")
#     limpiar_pantalla()
#     if c in dic_clientes:
#                 del dic_clientes[c]
#                 del dic_preferentes[c]
#                 print("el cliente fue eliminado con exito!")
# def mostrar_cli(dic_clientes):
#     limpiar_pantalla()
#     cedula = input("Digite la cedula del cliente que desea buscar: ")
#     if cedula in dic_clientes:
#         datos = dic_clientes[cedula]
#         print("=== DATOS DEL CLIENTE ===")
#         print(f"Cédula:    {cedula}")
#         print(f"Nombre:    {datos['nombre']}")
#         print(f"Dirección: {datos['direccion']}")
#         print(f"Teléfono:  {datos['telefono']}")
#         print(f"Correo:    {datos['correo']}")
#         print(f"Preferente: {'Sí' if datos['preferente'] else 'No'}")
#     else:
#         print(f"Error: El cliente con cédula {cedula} no está registrado.")
    
#     input("\nPresione Enter para continuar...")

# def listar_cli(dic_clientes):
#     limpiar_pantalla()
#     if not dic_clientes:
#         print("No hay clientes registrados actualmente.")
#     else:
#         print("=== LISTADO DE CLIENTES ===")
#         for cedula, datos in dic_clientes.items():
#             pref = "Sí" if datos["preferente"] else "No"
#             print(f"C.I: {cedula} | Nombre: {datos['nombre']} | Telefono: {datos['telefono']}| Preferente: {pref}")
#     input("\nPresione Enter para continuar...")
# def listar_cli_pref(dic_preferentes):
#     limpiar_pantalla()
#     if not dic_preferentes:
#         print("No hay clientes preferentes registrados actualmente.")
#     else:
#         print("=== LISTADO DE CLIENTES PREFERENTES ===")
#         for cedula, datos in dic_preferentes.items():
#             print(f"C.I: {cedula} | Nombre: {datos['nombre']} | Telefono: {datos['telefono']}")
#     input("\nPresione Enter para continuar...")
# def menu(fin):
#     while fin != True:
#         limpiar_pantalla()
#         op = int(input("opcion 1-------Registrar un cliente\nopcion 2-------Eliminar un cliente\nopcion 3-------Mostrar datos de un cliente\nopcion 4-------Listar todos los clientes\nopcion 5-------Listar clientes preferentes\nopcion 0-------Salir\nseleccione una opcion: "))
#         if op == 0:
#             x = input ("seguro que desea salir? (s/n): ")
#             if x == "s" or x == "S":
#                 fin = True
#             elif x == "n" or x == "N":
#                 fin = False
#                 return fin
#         elif op == 1:
#             registrar_cli(dic_clientes, dic_preferentes)
#         elif op == 2:
#             eliminar_cli(dic_clientes, dic_preferentes)
#         elif op == 3:
#             mostrar_cli(dic_clientes)
#         elif op == 4:
#             listar_cli(dic_clientes)
#         elif op == 5:
#             listar_cli_pref(dic_preferentes)
# dic_clientes = {} 
# dic_preferentes = {}
# fin = False
# while fin == False:
#     fin = menu(fin)
# EJERCICIO 12 DE BUCLES
# def contar(frase, letra, contador):
#     for i in range(0, len(frase)):
#         if letra in frase[i]:
#             contador += 1
#         else:
#             continue
#     return contador
# limpiar_pantalla()
# frase = input ("introduzca frase: ")
# letra = input ("introduzca letra: ")
# contador = 0
# print (f"la letra '{letra}' aparece {contar(frase, letra, contador)} veces en la frase '{frase}'")
# EJERCICIO DE SUCESION FIBONACCI
# def definir_limite(lim):
#     definido = False
#     while not definido:
#         lim = int(input("introduzca cuantos numeros de fibonacci desea ver?: "))
#         if lim <= 0:
#             print("el numero debe ser positivo")
#         else:
#             definido = True
#     return lim 
# def fibo(num, lim, numant):
#     lim = definir_limite(lim)
#     for i in range (0, lim):
#         print (f"numeros fibonacci {num}")
#         aux = num
#         num = aux + numant
#         numant = aux
        
        
# limpiar_pantalla()
# num = 1
# numant = 1
# lim = 1
# fibo(num,lim,numant)
# EJERCICIO 7 DE PROGRAMACION FUNCIONAL
def llenar(asig, aprob):
            for i in range (5):
                materia = input("nombre de materia: ")
                materia = materia.upper()
                nota = int(input(f"nota de {materia}: "))
                asig[materia] = nota
                if nota > 9:
                    aprob[materia] = nota
def mostrar(asig):
    input (asig)
def mostrar_aprob(aprob):
    input (aprob)
asig = {}
aprob = {}
x = False
while x == False:
    limpiar_pantalla()
    op = int(input("1 para asignar notas a una materia\n2 para mostrar las notas\n3 mostrar materias aprobadas\n0 para salir\nseleccione una opcion: "))
    if op == 0:
        x = True
    elif op == 1:
        llenar(asig, aprob)
    elif op == 2:
        mostrar(asig)
    elif op == 3:
        mostrar_aprob(aprob)




    