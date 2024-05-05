print("ola k ase")

# Soy un comentario

"""
# Variable
nombre="diego"
altura="175cm"
year= int("2020")
print(nombre + " " + altura)
"""
"""
pregunta1= input("cómo te llamas?: ")

if pregunta1== "Diego":
    print(pregunta1 + " que nombre más bonito...")

elif pregunta1== "Dani":
    print(pregunta1 + " que nombre más feo...")
"""
"""
num1 = int(input("ingresa un número: "))
num2 = int(input("ingresa otro número: "))

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
"""
"""
from datetime import datetime

nombre = input("Cómo te llamas?: ")
edad = int(input("qué edad tienes: "))

año_actual = datetime.now().year

edad100 = año_actual + (100 - edad)
print (nombre+ " " +str(edad)+ " " +str(edad100))
"""

# funciones
"""
def calcular_area_triangulo (base, altura):

    area= (base*altura)/2
    return area

    
base=int(input("base: "))
altura=int(input("altura: "))

area_triangulo = calcular_area_triangulo(base, altura)

print("El área del triángulo con base", base, "y altura", altura, "es:", area_triangulo)


print (calcular_area_triangulo (base, altura))
"""

var_altura= int(input("Altura?: "))

def mostrarAltura(altura):
    
    if altura >= 180:
        print("eres alto")

    else:
        print("eres bajo")

mostrarAltura(var_altura)


def mostrarNombre():
    nombre = input("Cómo te llamas?: ")
    if nombre == "Diego":
        print("Qué nombre más bonito")
    else:
        print("Qué nombre más feo")

mostrarNombre()


