"""
#1
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 

def fizzbuzz ():

    my_list = [i for i in range (1, 101)]

    for i in my_list:
        if i % 3 == 0 and i % 5 == 0:
            print ("fizzbuzz")
        elif i % 3 == 0:
            print ("fizz")
        elif i % 5 == 0:
            print ("fizz")
        else:
            print(i)

fizzbuzz()
"""

"""
#2
  Escribe una función que reciba dos palabras (String) y retorne
  verdadero o falso (Bool) según sean o no anagramas.
  - Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.

def is_anagram (word, word2):
    
    if int(len(word.lower())) != int(len(word2.lower())):
        return False
    
    elif word.lower() == word2.lower():
        return False

    else:
        return sorted(word.lower()) == sorted(word2.lower())
                                         
print(is_anagram ("amor", "RomA"))      
"""
"""
#3
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
 la que el siguiente siempre es la suma de los dos anteriores.
 0, 1, 1, 2, 3, 5, 8, 13...


def fibonacci():
    list = [0,1]

    num_fib = 50

    for i in range (1, num_fib):
        last_num = list[-1] + list[-2]
        list.append(last_num)

    print(list)

fibonacci()
"""
"""
#4
 Escribe un programa que se encargue de comprobar si un número es o no primo.
 Hecho esto, imprime los números primos entre 1 y 100.
"""

#a
def primos():

    for n in range (2, 102):
        es_primo = True
        for h in range (n-1,1,-1):
            if n % h == 0: # Si no hay resto es divisible, con lo cual no es primo
                es_primo = False
                
                break
                

        if es_primo:
            print (f"{n} es primo") # Primero se comprueba todas las itinerancias del for, si
                     # no se cumplen, ya tiene que ser primo


primos()


"""
#b

def is_prime():

    for number in range(1,101):
        if number >= 2:

            is_divisible = False

            for i in range (2, number):
                if number % i == 0:
                    is_divisible = True
                    break
            
            if not is_divisible:
                print(number)


print(is_prime())

"""



    









