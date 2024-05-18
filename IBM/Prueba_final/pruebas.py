while action != "5":

    

    if action == "2":
        agregar_tarea = input("Inserte tarea, 'fin' para terminar': ")
    if agregar_tarea == "fin":
        break
    else:      
        list.append(agregar_tarea)

action = input("1- Mostrar tareas\n2- Agregar tarea\n3- Marcar tarea completada\n4- Eliminar tarea\n5-fin\n")

print (list)




def tareas ():

    action = input("1- Mostrar tareas\n2- Agregar tarea\n3- Marcar tarea completada\n4- Eliminar tarea\n5- Fin\n")
    
    while action !="5":

        
        if action == "2":
            agregar_tarea = input("Inserte tarea, 'fin' para terminar': ")
            if agregar_tarea == "fin":
                break
            else:      
                list.append(agregar_tarea)


    print (list)



    def tareas ():
   
    
    action = input("1- Mostrar tareas\n2- Agregar tarea\n3- Marcar tarea completada\n4- Eliminar tarea\n5- Fin\n")
    
    while action !="5":
       
        if action == "2":
            agregar_tarea = input("Inserte tarea, 'fin' para terminar': ")

            if agregar_tarea == "fin":
                action = input("1- Mostrar tareas\n2- Agregar tarea\n3- Marcar tarea completada\n4- Eliminar tarea\n5- Fin\n")
                break
            else:      
                list.append(agregar_tarea)


    print (list)




list = []


def tareas ():
   
    
    action = input("1- Mostrar tareas\n2- Agregar tarea\n3- Marcar tarea completada\n4- Eliminar tarea\n5- Fin\n")
    
    while action !="5":
       
        if action == "2":
            agregar_tarea = input("Inserte tarea, 'fin' para terminar': ")

            if agregar_tarea == "fin":
                action = input("1- Mostrar tareas\n2- Agregar tarea\n3- Marcar tarea completada\n4- Eliminar tarea\n5- Fin\n")
                break
            else:      
                list.append(agregar_tarea)


    print (list)




list = []


def tareas ():
   
    
    action = input("1- Mostrar tareas\n2- Agregar tarea\n3- Marcar tarea completada\n4- Eliminar tarea\n5- Fin\n")
    
    while action !="5":
       
        if action == "2":
            agregar_tarea = input("Inserte tarea, 'fin' para terminar': ")

            if agregar_tarea == "fin":
                action = input("1- Mostrar tareas\n2- Agregar tarea\n3- Marcar tarea completada\n4- Eliminar tarea\n5- Fin\n")
                break
            else:      
                list.append(agregar_tarea)


    print (list)




tareas()

no_completadas = []
completadas = []

def tareas ():
    
    while True:

        action = input("\n1- Mostrar tareas\n2- Agregar tarea\n3- Marcar tarea completada\n4- Eliminar tarea\n5- Fin\n")

        if action == "1":
            print("Tareas no completadas:")
            for indice, tarea in enumerate(no_completadas, start=1):
                print(f"{indice}. {tarea}")
        elif action == "2":
            agregar_tarea = input("Inserte tarea: ")   
            no_completadas.append(agregar_tarea)
        elif action == "4":
            elim = int(input("Qué tarea quiere eliminar?: "))
            no_completadas.pop(elim-1)
        elif action == "5":
            break

        else:
            break

