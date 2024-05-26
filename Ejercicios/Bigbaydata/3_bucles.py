"""
#1a
num=0
while num <10:
    num += 1
    print (num)
#1b
for i in range(1, 11):
    print(i)
"""
"""
#2

fac=5
resultado=1

for i in range(1,fac+1):
    resultado*= i

print(resultado)
"""
"""
#3
frase = "Esta es una frase de ejemplo"
palabras = frase.split()  # Dividir la frase en palabras utilizando el espacio como delimitador
contador_palabras = 0

for palabra in palabras:
    print(palabra)
    contador_palabras += 1

print("El número total de palabras es:", contador_palabras)
"""
"""
#4

# Definimos los dos primeros números de Fibonacci
fibonacci = [0, 1]

# Generamos la secuencia de Fibonacci hasta el número deseado
n = 10  # Puedes cambiar este valor para generar más números de Fibonacci
while len(fibonacci) < n:
    siguiente_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente_numero)

# Imprimimos la secuencia de Fibonacci
print("Los primeros", n, "números de Fibonacci son:", fibonacci)
"""

"""
#5
def dibujar_arbol(n):
    for i in range(1, n + 1):  # Itera desde 1 hasta n (inclusive)
        print('*' * i)  # Imprime '*' repetido i veces en cada fila

# Ejemplo con n = 3

dibujar_arbol(5)
"""


"""
#6

ntotal = 0

while True:

    n = int(input("Escribe un número para sumar: "))
    if n != -1:   
     ntotal += n
   

    else:
        print("la suma de los números es " + str(ntotal))

"""
"""
#7

pin = str(1234)

for i in range (1, 4):
    xx = 3
    intento= input("introduzca PIN: ")
    
    if intento == pin:
        print("login correcto")
        break

    elif i == 3:
        print("llamando a la policía")

    else:
        print("pin incorrecto, le quedan " + str(3 - i) + " intentos")

"""
"""
#8
a = int(input("valor del cateto a: "))

while a <= 0:
    a= int(input("valor del cateto a (superior a 0): "))

b = int(input("valor del cateto b: "))

while a < 0:
    b= int(input("valor del cateto b (superior a 0): "))

c = (a**2 + b**2)**0.5
print (c)

"""

"""
#9

while True:

    op= (input("marque la operación 1-3: "))
    if op == "SAL":
        break

    if op != '1' and op != '2' and op != '3':   
       continue
    
    a = input("primer valor: ")

    if a == "SAL":
        break

    b = input("segundo valor: ")

    if b == "SAL":
        break
    
    elif op == "1":
        print(int(a)+int(b))
    
    elif op == "2":
        if b == "0":
            print("Error: no se puede dividir entre 0")
        else:
            print(int(a)/int(b))
   
    elif op == "3":
        print((int(a)*int(b)/2.5))

"""

#10

import random

ataque_1 = 10
ataque_2 = 10

defensa_1 = 6
defensa_2 = 6

vida_1 = 200
vida_2 = 200

numero_aleatorio = random.randint(1, 2)

while vida_1 >0 and vida_2 >0:

    if numero_aleatorio == 1:

        vida_1 -= (ataque_2 - defensa_1)
        vida_2 -= (ataque_1 - defensa_2)

        print("La vida del jugador 1 es de " + str(vida_1))
        print("La vida del jugador 2 es de " + str(vida_2))
        
        if vida_1 <= 0:
            print("jugador 1 ha perdido")
        
        elif vida_2 <= 0:
            print("jugador 2 ha perdido")
    
    if numero_aleatorio == 2:

        vida_2 -= (ataque_1 - defensa_2)
        vida_1 -= (ataque_2 - defensa_1)

        print("La vida del jugador 2 es de " + str(vida_2))
        print("La vida del jugador 1 es de " + str(vida_1))

        if vida_1 <= 0:
            print("jugador 1 ha perdido")
        
        elif vida_2 <= 0:
            print("jugador 2 ha perdido")



"""
import random

class Personaje:
    def __init__(self, nombre, ataque, defensa, vida):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida

    def atacar(self, otro_personaje):
        danio = max(0, self.ataque - otro_personaje.defensa)
        otro_personaje.vida -= danio
        print(f"{self.nombre} ataca a {otro_personaje.nombre} y le hace {danio} puntos de daño.")
        print(f"{otro_personaje.nombre} ahora tiene {otro_personaje.vida} puntos de vida.")

# Crear dos personajes
personaje_a = Personaje("A", 20, 10, 100)
personaje_b = Personaje("B", 25, 5, 100)

# Decidir aleatoriamente quién empieza
turno_actual = random.choice([personaje_a, personaje_b])
print(f"¡Comienza el combate! {turno_actual.nombre} empieza.")

# Combate hasta que alguno sea derrotado
while personaje_a.vida > 0 and personaje_b.vida > 0:
    if turno_actual == personaje_a:
        personaje_a.atacar(personaje_b)
        turno_actual = personaje_b
    else:
        personaje_b.atacar(personaje_a)
        turno_actual = personaje_a

# Determinar al ganador
if personaje_a.vida <= 0:
    print("¡El personaje B ha derrotado al personaje A!")
elif personaje_b.vida <= 0:
    print("¡El personaje A ha derrotado al personaje B!")


"""