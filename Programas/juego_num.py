while True:
    num_pen = int(input("Escribe un número del 1 al 100: "))

    if num_pen <=0 or num_pen >100:
        print("no has escrito un número correcto")

    else:
        break
    

while True:
    num1 = int(input("Di un número jugador 1: "))

    if num1 == num_pen:
        print("Has perdido!! era justo el número que había pensado")
        break  # Salir del bucle si se adivina el número
    elif num1 == (num_pen + 1) or num1 == (num_pen - 1):
        print("He perdido!! el número que había pensado era el " + str(num_pen))
        break
    elif num_pen > num1:
        print(num1 + 1)

    elif num_pen < num1:
        print(num1 - 1)

    num2 = int(input("Di un número jugador 2: "))

    if num2 == num_pen:
        print("Has perdido!! era justo el número que había pensado")
        break  # Salir del bucle si se adivina el número
    elif num2 == (num_pen + 1) or num2 == (num_pen - 1):
        print("He perdido!! el número que había pensado era el " + str(num_pen))
        break
    elif num_pen > num1:
        print(num2 + 1)

    elif num_pen < num1:
        print(num2 - 1)
  

