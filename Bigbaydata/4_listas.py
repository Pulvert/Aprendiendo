"""
#1

import random

ataque_defensa = [[10, 10], [6, 6]]

vida_1 = 200
vida_2 = 220

numero_aleatorio = random.randint(1, 2)

while vida_1 >0 and vida_2 >0:

    if numero_aleatorio == 1:

        vida_1 -= (ataque_defensa[0][1] - ataque_defensa[1][0])
        vida_2 -= (ataque_defensa[0][0] - ataque_defensa[1][1])

        print("La vida del jugador 1 es de " + str(vida_1))
        print("La vida del jugador 2 es de " + str(vida_2))
        
        if vida_1 <= 0:
            print("jugador 1 ha perdido")
        
        elif vida_2 <= 0:
            print("jugador 2 ha perdido")
    
    if numero_aleatorio == 2:

        vida_2 -= (ataque_defensa[0][0] - ataque_defensa[1][1])
        vida_1 -= (ataque_defensa[0][1] - ataque_defensa[1][0])

        print("La vida del jugador 2 es de " + str(vida_2))
        print("La vida del jugador 1 es de " + str(vida_1))

        if vida_1 <= 0:
            print("jugador 1 ha perdido")
        
        elif vida_2 <= 0:
            print("jugador 2 ha perdido")

"""

"""
#2

lista_asignaturas = []

asig = input("Insertar la lista de los nombres de las asignaturas del instituto BigBayData.com: ")

while asig != "fin":
    lista_asignaturas.append(asig)
    asig = input("Introduce otro valor (o 'fin' para terminar): ")


lista_notas = []

puntuaciones = input("Genial. Ahora introduce las puntuaciones uno por uno en Python(o 'fin' para terminar): ")

while puntuaciones != "fin":
    notas = int(puntuaciones)
    lista_notas.append(notas)
    puntuaciones = input("Introduce otro valor (o 'fin' para terminar): ")


alumnos = len(lista_notas)
nota_media= round(sum(lista_notas) / alumnos,1)
suspensos = sum(1 for x in lista_notas if x <5)


print(str("[" + lista_asignaturas[0]) +", " + str(alumnos) + " alumnos, nota media: " + str(nota_media) + ", Suspensos:" + str(suspensos)+"]")

"""
"""
#3a

recount = {}


while True:

    name = input("Introduce nombre(-1 para salir): ")

    if name == "-1":
        break

    if name in recount:
        recount[name] += 1
        
    else:
        recount[name] = 1

print("Recuento de nombres:")
      
for name, recount in recount.items():
    print(f"{name:} {recount}")

"""

"""
#3b
# Pedir al usuario que inserte los nombres
print("Introduce los nombres separados por comas (-1 para terminar):")
nombres_input = input().split(",")

# Inicializar un diccionario para almacenar los recuentos de nombres
recuentos = {}

# Procesar la entrada de nombres
for nombre in nombres_input:
    if nombre == "-1":
        break
    if nombre in recuentos:
        recuentos[nombre] += 1
    else:
        recuentos[nombre] = 1

# Imprimir los recuentos de cada nombre
print("Recuentos de nombres:")
for nombre, recuento in recuentos.items():
    print(f"{nombre}: {recuento}")
"""
"""
#4

names_list = []

while True:

    names = input("Introduce nombre(-1 para salir): ")

    if names == "-1":
        break

    else:
        names_list.append(names)


nombres_sin_repetir = list(set(names_list))

print (nombres_sin_repetir)
"""

"""
#5
list_res = []
num = 6

for x in range (0,20):
    x +=1
    res = num * x

    list_res.append(res)


print (list_res)
"""
"""
#6

print(list_num)

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Inicializar una lista con los primeros 10 números primos
numeros_primos = []
numero = 2
while len(numeros_primos) < 10:
    if es_primo(numero):
        numeros_primos.append(numero)
    numero += 1

# Imprimir la lista de los primeros 10 números primos
print("Los primeros 10 números primos son:", numeros_primos)
"""

