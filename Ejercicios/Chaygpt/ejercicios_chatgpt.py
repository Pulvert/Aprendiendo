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
        print (self.odd_list)7


l = Lists()
l.pairs()
l.prints()
"""

class Transactions():

    def __init__(self):
        self.list = []

    def read_file(self):

        with open('transacciones.txt', 'r') as file:
            for line in file:
                values = line.split(",")
                dict = {
                    "fecha": values[0],
                    "tipo": values[1],
                    "monto": values[2],
                    "descripción": values[3]
                }
                self.list.append(dict)
            
            print (self.list)

    def total_balance(self):
        total_income = 0
        total_spent = 0
        for value in self.list:        
            if value["tipo"] == "ingreso":
                total_income += float(value["monto"])
            elif value["tipo"] == "gasto":
                 total_spent += float(value["monto"])

        total = total_income - total_spent
        print (f"Balance Total: {total}")



    def month_balance(self):
        jan_income = 0
        jan_spent = 0
        for date in self.list:
            if date["fecha"][5:7] == "01":
                if date["tipo"] == "ingreso":
                    jan_income += float(date["monto"])
                elif date["tipo"] == "gasto":
                    jan_spent += float(date["monto"])
        total_jan = jan_income - jan_spent
        print (f"Enero 2024\n Ingresos: {jan_income}\n Gastos: {jan_spent}\n Balance: {total_jan} ")


    def min_max_trans(self):
        monto_mayor = float('-inf')
        monto_menor = float('inf')
        transaccion_mayor = None
        transaccion_menor = None
        
       
        for x in self.list:
            monto_actual = float(x['monto'])
            if monto_actual > monto_mayor:
                monto_mayor = monto_actual
                transaccion_mayor = x
            if monto_actual < monto_menor:
                monto_menor = monto_actual
                transaccion_menor = x

        print("Transacción Mayor:")
        print("  Fecha:", transaccion_mayor['fecha'])
        print("  Tipo:", transaccion_mayor['tipo'])
        print("  Monto:", transaccion_mayor['monto'])
        print("  Descripción:", transaccion_mayor['descripción'].strip())

        print("Transacción Menor:")
        print("  Fecha:", transaccion_menor['fecha'])
        print("  Tipo:", transaccion_menor['tipo'])
        print("  Monto:", transaccion_menor['monto'])
        print("  Descripción:", transaccion_menor['descripción'].strip())




transaction1 = Transactions()

transaction1.read_file()

transaction1.total_balance()
transaction1.month_balance()
transaction1.min_max_trans()

