class Task:
    def __init__(self): # Creamos atributos de clase "task"
        self.list_task_complete = [] # Creamos lista de tareas completas
        self.list_task_nocomplete = [] # Creamos lista de tareas no completas

    def add_task(self): # Método que añade tarea a lista de tareas no completas
        task = input("Inserte tarea: ")
        self.list_task_nocomplete.append(task)

    def print_tasks(self): # Método que imprime las tareas
        print("\nTareas no completadas:\n")
        for index, element in enumerate(self.list_task_nocomplete, start=1): # Iteramos sobre la lista para mostrar todos los elementos enumerados
          print(f"{index}. {element}") # Damos formato enumerado a las tareas no completadas
        print("\nTareas completadas:\n")
        for index, element in enumerate(self.list_task_complete, start=1): # Iteramos sobre la lista para mostrar todos los elementos enumerados
          print(f"{index}. {element}") # Damos formato enumerado a las tareas completadas

    def task_manage (self): # Método que pasa tareas a "completadas"
        task_number = int(input("\nQué tarea ha completado?: \n")) 
        try:
            task_pop = self.list_task_nocomplete.pop(task_number-1) # Eliminamos la tarea y la guardamos
            self.list_task_complete.append(task_pop) # La metemos en la lista de tareas completadas
        except:
            print("\nError: No existe esa tarea") # Generamos excepción por si el usuario teclea tarea no existente

    def del_task (self): # Método que elimina tarea
        task_type = input("\n'1' para eliminar tareas no completadas, '2' para tareas completadas:\n")
        try:
          if task_type == "1":
            task_position = int(input("\nQué tarea quiere eliminar?: \n"))
            self.list_task_nocomplete.pop(task_position-1) # Eliminamos de la lista "no completadas" según su posición (-1 porque se empieza a contar desde 0 y nuestro primer número de la lista es 1)
          if task_type == "2":
            task_position = int(input("\nQué tarea quiere eliminar?: \n"))
            self.list_task_complete.pop(task_position-1) # Eliminamos de la lista "no completadas" según su posición (-1 porque se empieza a contar desde 0 y nuestro primer número de la lista es 1)
        except:
            print("\nError: Opción incorrecta") # Generamos excepción por si el usuario teclea tarea no existente


task_instance = Task() # Creamos instancia de la clase "task"

while True:
    
    action = input("\n1- Mostrar tareas\n2- Agregar tarea\n3- Marcar tarea completada\n4- Eliminar tarea\n5- Fin\n\nIntroduzca opción: ") # Opciones que se muestran al usuario

    if action == "1": 
        task_instance.print_tasks() # Ejecuta método imprime las tareas
        
    elif action == "2": 
        task_instance.add_task() # Ejecuta método que añade las tareas

    elif action == "3":
        task_instance.task_manage() # Ejecuta método que pasa tareas a "completadas"

    elif action == "4":
        task_instance.del_task() # Ejecuta método que elimina tarea

    elif action == "5":
        break # Salir del bucle

    else:
        print("\nError: Opción incorrecta") # Error si no se marca opción correcta