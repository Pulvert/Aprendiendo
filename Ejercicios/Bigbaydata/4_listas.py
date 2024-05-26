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
"""
#7
lista_compra = ["manzanas", "papel", "yogurt", "chocolate" , "leche"]

lista_compra.pop()

lista_compra.reverse()

print(lista_compra)
"""
"""
#8 Añade las estadísticas de los primeros 10 pokemon en nuestra pokedex. Fíjate qué estadísticas quieres
#  para todos los pokemon. Aquí algunas sugerencias: nombre, ataque, hp, defensa, velocidad, at_Esp, def_Esp. Después, utiliza la lista como una pokedex para consultarlo.

stats = ["Nombre", "Ataque", "Hp", "Defensa", "Velocidad", "At_Esp", "Def_Esp"]

bulbasur = ["Bulbasur", 50, 500, 35, 10, 40, 45]
pikachu = ["Pikachu", 40, 300, 50, 20, 60, 45]

def print_stats(a):

    print(f"{stats[0]}: {a[0]}\n{stats[1]}: {a[1]}\n{stats[2]}: {a[2]}\n{stats[3]}: {a[3]}\n{stats[4]}: {a[4]}\n{stats[5]}: {a[5]}\n{stats[6]}: {a[6]}\n  ")


pokemon = input("Qué Pokemon quieres consultar?: ")


if pokemon == "bulbasur":
    a = bulbasur
    print_stats(a)

if pokemon == "pikachu":
    a = pikachu
    print_stats(a)
"""
"""
#9 Imagina construir un sistema de planning de vuelos de un aeropuerto cercano. Crea una planificación donde dentro contiene, por día de la semana, horario, compañia, duracion_estimada, tipo_avion. Utiliza una lista dentro de otra lista.
# PD: Después de llenar los datos necesitarás ofrecer al usuario ver la información.

list = ["día de la semana", "horario", "compañia", "duracion_estimada", "tipo_avion", []]

print (list)

a = input("introduzca día de la semana: ")
b = input("introduzca horario: ")
c = input("introduzca compañía: ")
d = input("introduzca duración: ")
e = input("introduzca tipo de avión: ")


list[-1].append(a)
list[-1].append(b)
list[-1].append(c)
list[-1].append(d)
list[-1].append(e)

print (f"{list[0]}: {list[-1][0]} \n {list[1]}: {list[-1][1]} \n {list[2]}: {list[-1][2]} \n {list[3]}: {list[-1][3]} \n {list[4]}: {list[-1][4]} ")
"""

#10 Haz un sistema de ordenamiento de ayudas para tu comunidad. La idea es que insertes todos los emails que quieras para, aleatoriamente, ofrecer N ayudas. 
# El objetivo es tener un sistema justo de ayudas para repartir entre la ciudadanía que se postula. Una vez lo tengas, desarrolla un sistema de envío automático por correo. ¿Serás capaz?

import random

email_list = []

while True:

    emails = input("inserte correo electrónico 'fin' para terminar: ")

    if emails == "fin":
        break
    
    else:
        email_list.append (emails)

ayudas = 2

seleccionados = random.sample(email_list, ayudas)

print (seleccionados)


for seleccionado in seleccionados:

    print("felcididades", seleccionado)








