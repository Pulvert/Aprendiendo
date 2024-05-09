
#1 Imprime «Hola Mundo» si a es mayor a b. 
a=int(input("valor: "))
b=int(input("valor: "))

if:
    a > b
    print("hello world")

"""
#2 Determinar si alguien es menor de edad o no. Pide al usuario la edad por pantalla e imprime por pantalla si puede acceder a nuestra fiesta nocturna de BigBayData.com.
edad=int(input("edad: "))

if edad >= int(18):
    print("puedes pasar a nuestra fiestuki")
else:
    print("sorry")
"""
"""
#3
b=int(input("valor cateto1: "))
c=int(input("valor cateto2: "))

if b <= int(0):
    print("error")
elif c <= int(0):
    print("error")
else:
    a=((b**2)+(c**2))**0.5
    print(float(a))
"""

"""
#4
a=int(input("valora: "))
b=int(input("valorb: "))


op=int(input("elija numero de operacion: "))
if op == 1:
    print(a+b)
elif op == 2:
    print(a*b)
elif op == 3:
    print(a-b)
elif op == 4:
    print(a/b)
"""
"""
#5
puntos=int(input("Cuantos puntos tienes?"))

if puntos <100:
    print("10% descuento")
elif puntos in range (100,149):
    print("12% descuento")
elif puntos ==150:
    print("15% descuento")
elif puntos >150:
    print("20% descuento")
"""
"""
#6
imp_fra=int(input("importe factura: "))
tip_fra=input("tipo general o tipo alimetos?: ")

if tip_fra == "general":
    print("total: "+str(imp_fra+(imp_fra*0.21)))

elif tip_fra == "alimentos":
    print("total: "+str(imp_fra+(imp_fra*0.10)))
"""
"""
#7
password="diego"

password=input("introduzca contraseña: ")

if password=="diego":
    print("Bienvenid@...")

else:
    print("ordenador bloqueado. contraseña incorrecta")
"""
"""
#8
año=int(input("Año: "))

if (año%4==0) and (año%100!=0) or (año%400==0):
    print("El año es un año bisiesto (tiene 366 días).")

else:
    print("El año no es un año bisiesto (tiene 365 días).")
"""
"""
#9
tarifa_anual=int(120)
edad=19
tiene_trabajo=("no")

if edad >= 18 and tiene_trabajo == "si":
    print("la tarifa anual es de " + str(tarifa_anual))

elif edad <= 18 and tiene_trabajo == "si":
    print("la tarifa anual es de " + str(tarifa_anual*0.95))

elif edad >= 18 and tiene_trabajo == "no":
    print("la tarifa anual es de " + str(tarifa_anual*0.75))

elif edad <= 18 and tiene_trabajo == "no":
    print("la tarifa anual es de " + str(tarifa_anual*0.5))
"""
"""
#10

ing_veg = ("pimiento y tofu")
ing_noveg = ("peperoni, jamón y salmón")
ing_comunes = ("mozarella, tomate y ")

pizza=input("Quiere una pizza vegetariana:? ")
if pizza.lower() == ("si"):
    ing1=input("elija un ingrediente entre "+ing_veg+ ":")
    print("su pizza está compuesta de "+ ing_comunes + ing1)

else:
    ing2=input("entonces quiere una pizza no vegetariana, elija un ingrediente entre "+ing_noveg+ ":")
    print("su pizza está compuesta de "+ ing_comunes + ing2)
"""