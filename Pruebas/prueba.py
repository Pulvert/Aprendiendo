
"""
my_list = [3, 7, 8, 9]
print(my_list)
my_list = "Diego"

print(my_list)
"""
"""
ataque_defensa = [[8, 6], [4, 10]]

print(ataque_defensa[1][1])


ataque,defensa = [8,6], [4,10]


print(defensa[1])

"""

lista_asignaturas = []

asig = input("Insertar la lista de los nombres de las asignaturas del instituto BigBayData.com: ")

while asig != "fin":
    lista_asignaturas.append(asig)
    asig = input("Introduce otro valor (o 'fin' para terminar): ")


print(lista_asignaturas)