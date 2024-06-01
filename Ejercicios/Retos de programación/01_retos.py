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
"""
#a
def primos():

    for n in range (2, 102):
        es_primo = True
        for h in range (n-1,1,-1):
            if n % h == 0: # Si no hay resto es divisible, con lo cual no es primo
                es_primo = False
                print (f"{n} no es primo")
                break
                

        if es_primo:
            print (f"{n} es primo") # Primero se comprueba todas las itinerancias del for, si
                     # no se cumplen, ya tiene que ser primo


primos()

"""
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
"""
#7
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
"""
list_string = []
string = "Hola mundo"

for i in string[::-1]:
    list_string.append(i)

new_string = "".join(list_string)
print(new_string)
"""


from posixpath import split
"""
#5
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""
"""
def area (type):

  base = 5
  altura = 6

  if type == "triangle":
    return base * altura / 2
  elif type == "square":
    return base * base
  elif type == "rectangle":
    return base * altura


print (area("triangle"))
"""
"""
#8
Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que
 lo resuelvan automáticamente.
"""
"""
phrase = "La gente de la playa, estaba con otra gente"
# Convertir a minúsculas y eliminar la coma
phrase_lower = phrase.lower().replace(",", "")
# Dividir la frase en palabras
words = phrase_lower.split(" ")

# Crear un diccionario para contar las palabras
word_count = {}

# Iterar sobre las palabras y contar las frecuencias
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


# Imprimir las palabras repetidas y sus frecuencias
repeated_words = {word: count for word, count in word_count.items() if count > 1}

print("Palabras repetidas y sus frecuencias:")
for word, count in repeated_words.items():
    print(f"{word}: {count}")
"""
"""
#9
Crea un programa se encargue de transformar un número
decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""
"""
def binary (num):

  bin_list = []
  num = int(num)

  while num > 0:

    if num % 2 == 0:
      bin_list.append("0")
    else:
      bin_list.append("1")
    num = int(num/2)

  bin_list.reverse()

  bin_nums = "".join(bin_list)

  print(bin_nums)

binary(458)
"""
"""
#10
Crea un programa que sea capaz de transformar texto natural a código
morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar
la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras
o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en
 https://es.wikipedia.org/wiki/Código_morse.

"""
"""
import string

def morse ():

  morse = ".- -... -.-. -.. .-.-."
  palabras = morse.split()
  list_morse = []
  abecedario = string.ascii_lowercase

  dic_morse = {" ":" ","a":".-","b":"-...","c":"-.-.","d":"-.."}

  if morse[0] in abecedario:

    for i in morse:
      if i in dic_morse:
        for key, value in dic_morse.items():
          if i == key:
            print (value)
  else:

    for i in palabras:
        for key, value in dic_morse.items():
          if i == value:
            list_morse.append(key)
    string_morse = "".join(list_morse)
    print (string_morse)

morse ()
"""
"""
#11
Crea un programa que comprueba si los paréntesis, llaves y corchetes
de una expresión están equilibrados.
- Equilibrado significa que estos delimitadores se abren y cieran
en orden y de forma correcta.
- Paréntesis, llaves y corchetes son igual de prioritarios.
No hay uno más importante que otro.
- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
- Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""
"""
def estan_equilibrados(expresion):
    # Crear un diccionario de pares de delimitadores
    pares = {')': '(', ']': '[', '}': '{'}
    # Crear una pila para rastrear los delimitadores abiertos
    pila = []

    # Recorrer cada carácter en la expresión
    for char in expresion:
        # Si el carácter es un delimitador de apertura, agregarlo a la pila
        if char in pares.values():
            pila.append(char)
        # Si el carácter es un delimitador de cierre
        elif char in pares.keys():
            # Comprobar si la pila está vacía o si el delimitador superior de la pila no coincide
            if not pila or pila[-1] != pares[char]:
                return False
            # Si coincide, eliminar el delimitador superior de la pila
            pila.pop()

    # Si la pila está vacía al final, los delimitadores están equilibrados
    return not pila

# Ejemplos de uso
expresion1 = "{ [ a * ( c + d ) ] - 5 }"
expresion2 = "{ a * ( c + d ) ] - 5 }"

print(estan_equilibrados(expresion1))  # Debería devolver True
print(estan_equilibrados(expresion2))  # Debería devolver False
"""
"""
#12

Crea una función que reciba dos cadenas como parámetro (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO
estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO
estén presentes en str1.
"""

def twelve (str1, str2):

    out1 = []
    out2 = []

    dict1 = {}
    dict2 = {}

    for i in str1:   
        for j in str2:
            if i == j:                      
                dict1[i] = 1
                break               
            else:                      
                dict1[i] = 0

    for k, v in dict1.items():
        if v == 0:
            out1.append(k)

    for i in str2:   
        for j in str1:
            if i == j:                      
                dict2[i] = 1
                break               
            else:                      
                dict2[i] = 0

    for k, v in dict2.items():
        if v == 0:
            out2.append(k)

    print(out1)       
    print(out2)  

twelve("jueves", "miercoles")













