"""
def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.
    return a+b # "return" devuelve el resultado de la función.
print(suma(2, 3)) # Llamada a la función. Hay que pasarle dos parámetros.
# Resultado: 5
"""
"""
def en_pantalla(frase1, frase2):
    print(frase1, frase2) # "return" no es obligatorio

en_pantalla('Me gusta', 'Python')
# Resultado: Me gusta Python

"""

"""
def f1(a): # Función que "encierra" a f2 (enclosing)
    print(a)
    b = 100
    def f2(x): # Función anidada
        print(x) # Llamamos a f2 desde f1
    f2(b)

f1('Python') # Llamamos a f1

"""

"""
def factorial(x):
    if x>1:
        return x*factorial(x-1)

    else:
        return 1
    
print(factorial(10))
"""

"""
def maxmin(lista):
    return max(lista), min(lista) #Devuelve una tupla de 2 elementos
l = [1, 3, 5, 6, 0]
maximo, minimo = maxmin(l) #Desempaqueta la tupla en 2 variables

print(minimo, maximo, sep= ' ')
"""
"""
def descomposicion_en_factores(numero):
    factores = []
    divisor = 2  # Empezamos con el primer número primo

    while numero > 1:
        # Dividimos el número por el divisor hasta que ya no sea divisible
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1

    return factores

# Ejemplo de uso
numero = 1025
print("Los factores primos de", numero, "son:", descomposicion_en_factores(numero))
"""

"""
a = 'Python' #Scope global(al módulo)
print('Valor fuera:', a)

def funcion():
    a=33
    print('Valor dentro', a) #Scope local a la función

funcion()

print('Valor fuera', a)

"""
"""
G = 'Esta variable es de ámbito Global'
def f1():
    E='Esta variable es local a f1. Enclosing a f2'
    def f2():
        L = 'Esta variable es local a f2'
        print(L, E, G, sep = '\n')
        f2()

f1()
"""


def suma(a, b): # Modificamos a y b en el scope de suma()
    a = 3
    b = 4
    return a+b

a, b = 5, 10

print(suma(a, b))
print(a, b) # a y b no han cambiado fuera de la función

