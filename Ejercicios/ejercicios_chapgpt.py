"""
# Desarrolla un programa en Python que simule un juego de adivinanza de números. El programa debe generar un número aleatorio entre 1 y 100,
#y luego permitir al usuario intentar adivinarlo. Debe proporcionar pistas al usuario indicando si el número ingresado es mayor o menor que el número secreto. 
# El juego debe continuar hasta que el usuario adivine correctamente el número. Al final, el programa debe imprimir cuántos intentos le tomó al usuario adivinar el número."

import random

class Number:
    def __init__(self):
        self.number = int(random.randint(1, 100))
        

    def guess (self):
        count = 0
        while True:

            try:
                n = int(input("Dí un número del 1 al 100: "))
                count += 1            
                if n <0 or n >100:
                    print ("Tiene que ser un número entre 1 y 100!!")
                elif n > self.number:
                    print("El número pensado es menor")
                elif n <0 or n >100:
                    print ("Tiene que ser un número entre 1 y 100!!")
                elif n == self.number:
                    print("Has acertado el número!")
                    print(f"Has necesitado {count} intentos")
                    break
                else:
                    print("El número pensado es mayor")
            except:
                print ("Tiene que ser un número entre 1 y 100!!")

correct_number = Number()

correct_number.guess()
"""
# "Escribe un programa en Python que tome como entrada una lista de números y devuelva dos listas: una con los números pares y otra con los números impares. 
# El programa debe ser capaz de manejar listas de cualquier longitud y debe imprimir las dos listas resultantes al final."


class Lists():

    def __init__(self):

        self.numbers_list = [1,9,5,4,15,64,4,2,324]
        self.pair_list = []
        self.odd_list = []

    def pairs (self):

        for x in self.numbers_list:
            if x % 2 == 0:
                self.pair_list.append(x)
            else:
                self.odd_list.append(x)

    def prints (self):
        print (self.pair_list)
        print (self.odd_list)


l = Lists()
l.pairs()
l.prints()







