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
"""
"""
#13
Escribe una función que reciba un texto y retorne verdadero o
falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee
de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.
"""
"""
import string

def palíndromo (words):


    letters = ""

    for i in words:
        if i == " " or string.punctuation:
            continue
        else:
            letters += i

    if letters.lower() == (letters.lower()[::-1]): print(True)
    else:
        print(False)
     
palíndromo("Ana lleva al oso la avellana")
"""
"""
#14
Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva.
"""
"""
#   Factorial
def factorial (x):
    if x == 1:
        return 1
    
    return x * factorial(x-1)
    
print(factorial(5))

#  Primero
n=5
n=n*(n-1)*(n-2)*(n-3)*(n-4)
print(n)
n=2
n=n*(n-1)
print(n)
n=10
n=n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)*(n-7)*(n-8)
print(n)

#   Segundo
def factorial(x):

    for i in range(x-1, 0, -1):
        x *= i
    
    return x

print(factorial(5))

#   Otro ejemplo factorial
def total_paginas(libros):
    if len(libros) == 1:
        return libros[0]
    
    return libros[0] + total_paginas(libros[1:])
    
print(total_paginas([50,100, 150]))

#   Otro ejemplo factorial sencillo
def cuenta_atras(numero):
    numero -= 1
    if numero > 0:
        print (numero)
        cuenta_atras (numero)
    else:
        print("Empezamos!")
    
    print(f"Orden de liberación {numero}")

cuenta_atras (10)
"""
"""
#15
Escribe una función que calcule si un número dado es un número de Armstrong
(o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información
al respecto.
"""
"""
def is_armstrong (number):

    lenght_number = len(str(number))
    list_number = []
    
    for element in str(number):
        list_number.append(element)
    
    print(list_number)

    suma = 0

    for i in list_number:
        i = int(i)
        i = i**lenght_number
        suma += i
    
    if suma == number:
        return True
    else:
        return False

print(is_armstrong(153))

#Versión simplificada:
def es_numero_de_armstrong(numero):
    # Convertir el número a una cadena para poder iterar sobre sus dígitos
    digitos = str(numero)
    # Contar el número de dígitos
    numero_de_digitos = len(digitos)
    # Calcular la suma de los dígitos elevados a la potencia del número de dígitos
    suma = sum(int(digito) ** numero_de_digitos for digito in digitos)
    # Verificar si la suma es igual al número original
    return suma == numero

# Ejemplos de uso:
print(es_numero_de_armstrong(153))  # Salida: True
print(es_numero_de_armstrong(9474)) # Salida: True
print(es_numero_de_armstrong(123))  # Salida: False
"""
"""
#16
Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas.
- Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
- La función recibirá dos String y retornará un Int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se
lanzará una excepción.
"""
"""
from datetime import date
import re

def dates (date1, date2):

    pattern = 
    coincidence = re.match(pattern, date1)

    if coincidence:

        day1, month1, year1 = date1.split("/")

        day1 = int(day1)
        month1 = int(month1)
        year1 = int(year1)

        day2, month2, year2 = date2.split("/")

        day2 = int(day2)
        month2 = int(month2)
        year2 = int(year2)

        
        date1_format = date(year1,month1,day1)
        date2_format = date(year2,month2,day2)

        difference_days = (date2_format-date1_format)

        print(f"La difrencia es de {difference_days.days} días entre ambas fechas")

    else:
        print("La fecha no coincide con el formato dd/mm/yyyy.")
  

dates("11/03/1984", "03/06/2024")

# Solución Chatgpt

from datetime import datetime

def calcular_dias_entre_fechas(fecha1, fecha2):
    formato = "%d/%m/%Y"  # Definimos el formato de la fecha

    try:
        # Convertimos las cadenas de texto a objetos datetime
        fecha1_datetime = datetime.strptime(fecha1, formato)
        fecha2_datetime = datetime.strptime(fecha2, formato)
    except ValueError:
        raise ValueError("Una de las cadenas de texto no representa una fecha correcta")

    # Calculamos la diferencia absoluta en días entre las dos fechas
    diferencia = abs((fecha2_datetime - fecha1_datetime).days)
    
    return diferencia

# Ejemplos de uso:
try:
    print(calcular_dias_entre_fechas("01/06/2023", "01/06/2024"))  # Salida: 366 días (año bisiesto)
    print(calcular_dias_entre_fechas("15/03/2022", "10/03/2022"))  # Salida: 5 días
    print(calcular_dias_entre_fechas("15/03/2022", "32/03/2022"))  # Esto lanzará una excepción
except ValueError as e:
    print(e)
"""
"""
#17
Crea una función que reciba un String de cualquier tipo y se encargue de
poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que
lo resuelvan directamente.
"""
"""
def capital (string):

    list_phrase = []

    for i in string.split():
        list_phrase.append(i.capitalize())
        
    phrase = " ".join(list_phrase)

    print(phrase)
   
capital("La niña no se dejó peinar")
"""
"""
#18
Crea una función que evalúe si un/a atleta ha superado correctamente una
carrera de obstáculos.
- La función recibirá dos parámetros:
- Un array que sólo puede contener String con las palabras
"run" o "jump"
- Un String que represente la pista y sólo puede contener "_" (suelo)
o "|" (valla)
- La función imprimirá cómo ha finalizado la carrera:
- Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
será correcto y no variará el símbolo de esa parte de la pista.
- Si hace "jump" en "_" (suelo), se variará la pista por "x".
- Si hace "run" en "|" (valla), se variará la pista por "/".
- La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""
"""
def is_complete(a, b):

    if a[0] == "run" and b == "_":
        return True
    elif a[0] == "run" and b == "|":
        b = "x"
        print (b)
        return False
    elif a[0] == "jump" and b == "|":
        return True
    elif a[0] == "jump" and b == "_":
        b = "/"
        print (b)
        return False


    else:
        return False
 
print(is_complete(["run"],"_"))
print(is_complete(["run"],"|"))
print(is_complete(["jump"],"_"))
print(is_complete(["jump"],"|"))
"""

"""
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 * y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 *   O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta.
 * Se podría representar con un vacío "", por ejemplo.
"""
"""
def tik_tac_toe ():

    m = [["O", "O", "X"],
        ["O", "X", "X"],
        ["O", "", ""]]

    count_x = 0
    count_o = 0

    for i in range(len(m)): # Iterar sobre las filas
        for j in range(len(m[i])): # Iterar sobre las columnas
            if m[i][j] == "X":
                count_x += 1
            elif m[i][j] == "O":
                count_o += 1

    if count_x > (count_o + 2) or count_o > (count_x + 2) : print("Nulo: Proporción incorrecta")

    else:
        if m[0][0] == m[0][1] ==m[0][2]: print(f"Ganan las {m[0][0]}")
        elif m[0][0] == m[1][0] ==m[2][0]: print(f"Ganan las {m[0][0]}")
        elif m[0][1] == m[1][1] ==m[1][2]: print(f"Ganan las {m[0][1]}")
        elif m[0][2] == m[1][2] ==m[2][2]: print(f"Ganan las {m[0][2]}")
        elif m[0][0] == m[1][1] ==m[2][2]: print(f"Ganan las {m[0][0]}")
        elif m[2][0] == m[2][1] ==m[2][2]: print(f"Ganan las {m[2][0]}")
        elif m[0][2] == m[1][1] ==m[2][0]: print(f"Ganan las {m[2][0]}")
        else: print("Empate")

tik_tac_toe ()

# solucion ChatGPT
def analizar_matriz(matriz):
    # Contar "X" y "O" en la matriz
    contador_X = sum(fila.count('X') for fila in matriz)
    contador_O = sum(fila.count('O') for fila in matriz)
    
    # Validar la proporción de "X" y "O"
    if abs(contador_X - contador_O) > 1:
        return "Nulo"
    
    # Función para verificar si hay un ganador en filas, columnas o diagonales
    def verificar_ganador(simbolo):
        # Verificar filas y columnas
        for i in range(3):
            if all(matriz[i][j] == simbolo for j in range(3)) or all(matriz[j][i] == simbolo for j in range(3)):
                return True
        # Verificar diagonales
        if all(matriz[i][i] == simbolo for i in range(3)) or all(matriz[i][2-i] == simbolo for i in range(3)):
            return True
        return False
    
    # Verificar si hay ganadores
    ganador_X = verificar_ganador('X')
    ganador_O = verificar_ganador('O')
    
    # Determinar el resultado
    if ganador_X and ganador_O:
        return "Nulo"
    elif ganador_X:
        return "X"
    elif ganador_O:
        return "O"
    elif contador_X + contador_O == 9:
        return "Empate"
    else:
        return "Nulo"

# Ejemplo de uso:
matriz = [
    ["X", "O", "X"],
    ["O", "X", ""],
    ["O", "", "X"]
]

resultado = analizar_matriz(matriz)
print("Resultado:", resultado)
"""

"""
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
"""
from datetime import timedelta

def milisec (days, hours, minutes, seconds):

    delta = timedelta(days=days, hours=hours, minutes = minutes, seconds=seconds)

    total_hours = delta.seconds

    comp = days*24 + hours
    comp2 = comp*60 + minutes
    comp3 = comp2*60 + seconds

    print(comp3)



    print(total_hours)
    

    print(delta)



milisec(4, 12, 45, 22)


