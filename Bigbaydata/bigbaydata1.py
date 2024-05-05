"""
#1
print("Hola Mundo!")
"""
"""
#2
mitexto = "Hola Mundo!"
print(type(mitexto))
"""
"""
#3
num=int(2)
resultado= int(num*2/1.5)

print(type(resultado))
"""
"""
#4
edad=input("Qué edad tienes: ")
print(type(int(edad)))
"""
"""
#5
capital_inicial=int(100000)
tasa_interes=float(0.02)
periodo=int(10)

total=int(capital_inicial*(1+tasa_interes)**10)
total_interes=total-capital_inicial
print(total_interes)

"""
"""
#6
intensidad= int(3)
resistencia= int(4)

voltaje=intensidad*resistencia

print(voltaje)
"""
"""
#7

r= 2
c=2*3.1416*r

print(c)
print(2*r)
"""
"""
#8

import time

peso1= int(input("Introducir valor del peso del primer átomo: "))
atomo1= int(input("Introducir el número de átomos del primer átomo: "))
peso2= int(input("Introducir valor del peso del segundo átomo: "))
atomo2= int(input("Introducir el número de átomos del segundo átomo: "))

pesoMolecuar = (int(peso1*atomo1*peso2*atomo2))

print("calculando el Peso Molecular...")
time.sleep(3)
print(pesoMolecuar)
"""

"""
#9
n=5
n=n*(n-1)*(n-2)*(n-3)*(n-4)
print(n)
n=2
n=n*(n-1)
print(n)
n=10
n=n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)*(n-7)*(n-8)
print(n)
"""
"""
#10

impresiones= 1000
clicks= 5000
tiempoPorSession= 450
cpc= 5

ctr = clicks/impresiones
print("El número como porcentaje es: {:.0f}%".format(ctr))

"""
