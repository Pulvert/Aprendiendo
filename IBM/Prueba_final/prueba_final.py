""" Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione
una6 lista de tareas pendientes. El programa deberá permitir al usuario realizar las siguientes
operaciones:
• Agregar una nueva tarea: El programa deberá permitir al usuario agregar una nueva tarea a
la lista de tareas pendientes.
• Marcar una tarea como completada: El programa deberá permitir al usuario marcar una
tarea como completada, dada su posición en la lista.
• Mostrar todas las tareas: El programa deberá imprimir en pantalla todas las tareas
pendientes, numeradas y mostrando su estado (completada o pendiente).
• Eliminar una tarea: El programa deberá permitir al usuario eliminar una tarea de la lista,
dada su posición.

El programa deberá incluir las siguientes características:
• Manejo de excepciones: El programa deberá manejar excepciones en caso de que el
usuario ingrese una opción no válida o una posición que no exista en la lista.
• Comentarios explicativos: El código deberá estar comentado para explicar su
funcionamiento en cada parte relevante.
"""

no_completadas = [] # Lista de las tareas no completadas.
completadas = [] # Lista a la que van las tareas que se marcan como completadas

def tareas (): # Definimos función para reutilizar código si fuera necesario
    
    while True: # Bucle, sól ose sale de él tecleando el número 5

        action = input("\n1- Mostrar tareas\n2- Agregar tarea\n3- Marcar tarea completada\n4- Eliminar tarea\n5- Fin\nIntroduzca opción: ") # Opciones que se muestran al usuario

        if action == "1":
            if not no_completadas and not completadas: # En el caso de que no se hayam introducido tareas
                print("\nTodavía no existen tareas")
            else:
                print("\nTareas no completadas:") 
                for indice, tarea in enumerate(no_completadas, start=1):
                    print(f"{indice}. {tarea}") # Muestra tareas no completadas iterando sobre la lista. Le damos formato para enumerar los elementos (índice - tarea)
                print("\nTareas completadas:")
                for indice, tarea in enumerate(completadas, start=1):
                    print(f"{indice}. {tarea}") # Muestra tareas completadas iterando sobre la lista. Le damos formato para enumerar los elementos (índice - tarea)

        elif action == "2":
            agregar_tarea = input("Inserte tarea: ") # Solicitamos al usuario que inserte tarea (todas van a "tareas no completadas")
            no_completadas.append(agregar_tarea) # Añadimos el elemento "tarea" a la lista

        elif action == "3":
            if not no_completadas:
                print("\nNo exixten tareas no completadas")
            else:
                completada = int(input("Qué tarea ha completado?: ")) # Preguntamos al usuario el número de tarea de la lista de "no completadas" ha completado
                tarea_completada=no_completadas.pop(completada-1) # La quitamos de la lista "no completadas" y la guardamos en una variable
                completadas.append(tarea_completada) # La añadimos en la lista de "completadas"

        elif action == "4":
            if not no_completadas and not completadas: # En el caso de que no se hayan introducido tareas
                print("\nNo existen tareas")
            else:
                bb = input("\nQuiere eliminar una tarea completada o no completada?: ") # Distinguimos de qué lista quiere eliminar la tarea
                if bb == "no completada":
                    if not no_completadas:
                       print("\nNo existen tareas no completadas")
                    else:
                        elim = int(input("\nQué tarea no completada quiere eliminar?: "))
                        no_completadas.pop(elim-1) # Eliminamos de la lista "no completadas" según su posición (-1 porque se empieza a contar desde 0 y nuestro primer número de la lista es 1)
                elif bb == "completada":
                    if not completadas:
                        print("\nNo existen tareas completadas")
                    else:
                        elim = int(input("\nQué tarea completada quiere eliminar?: "))
                        completadas.pop(elim-1) # Eliminamos de la lista "completadas" según su posición (-1 porque se empieza a contar desde 0 y nuestro primer número de la lista es 1)

        elif action == "5": # La única forma de salir
            break

        else: # Si apretamos otra tecla fuera de las opciones, vuelve a las opciones que pide al usuario
            False


tareas()