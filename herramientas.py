class Validador:
    def __init__(self):
        pass
    def veri_num(self, entrada):
        while True:
            try:
                # Intentamos convertir lo que recibimos del main
                numero = int(entrada)
                return numero
            except ValueError:
                # Si falló, aquí mismo pedimos el nuevo dato
                print("Error: Eso no parece un número entero.")
                entrada = input("Inténtalo de nuevo: ")
    def primo(self, num):
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