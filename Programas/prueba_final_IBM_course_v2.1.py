from colorama import Fore, Style # Importamos biblioteca para poner colorcitos
import json # Importamos biblioteca para poder guardar las tareas una vez cerrado el programa


class Task: # Creamos atributos de clase "task"
    def __init__(self): # Creamos atributos de clase "task"
        self.dic_task = {} # Creamos diccionario de tareas
        self.load_tasks() # Nos permite importar tareas antes cargadas

    def load_tasks(self): # Método para importar tareas antes cargadas
        try:
            with open("tasks.json", "r") as file:
                self.dic_task = json.load(file) # Busca el archivo y carga el diccionario
        except FileNotFoundError:
            pass  # Si el archivo no existe, no hay tareas que cargar

    def save_tasks(self): # Método para guardar tareas
        with open("tasks.json", "w") as file:
            json.dump(self.dic_task, file)

    def add_task(self): # Método que añade tarea no completada
        task = input("\nInserte tarea: ")
        self.dic_task[task] = "No completado"

    def print_tasks(self): # Método que imprime las tareas
        print(f"\nTAREAS\n-------")
        for index, (key, value) in enumerate(self.dic_task.items(), start=1):  # Iteramos sobre la lista para mostrar todos los elementos enumerados
            if value == ("No completado"): # Hacemos un 'if' para poner de color rojo el 'no completado'
                print(f"{Fore.WHITE}{index}. {Fore.BLUE}{key}{Fore.WHITE} -> {Fore.RED}{value}{Style.RESET_ALL}")
            else: # Hacemos un 'else' para poner de color verde el 'completado'
                print(f"{Fore.WHITE}{index}. {Fore.BLUE}{key}{Fore.WHITE} -> {Fore.GREEN}{value}{Style.RESET_ALL}")

    def task_manage (self): # Método que pasa tareas a "completadas"
        task_number = int(input("\nQué tarea ha completado?: \n"))
        try:
            items_list = list(self.dic_task.items()) # Convertimos diccionario a lista para poder identificar el valor por nº posición
            new_value = "Completado" # Queremos cambiar a 'Completado'
            items_list[task_number-1] = (items_list[task_number-1][0],new_value) # Cambiamos a 'Completado'
            self.dic_task = dict(items_list) # Volvemos a convertir a diccionario
        except:
            print(f"\n{Fore.RED}Error: No existe esa tarea{Style.RESET_ALL}") # Generamos excepción por si el usuario teclea tarea no existente

    def del_task (self): # Método que elimina tarea
        task_position = int(input("\nQué tarea quiere eliminar?: \n"))
        try:
            items_list = list(self.dic_task.items()) # Convertimos diccionario a lista para poder identificar el valor por nº posición
            items_list.pop(task_position-1) # Eliminamos elelemento según posición
            self.dic_task = dict(items_list) # Volvemos a convertir a diccionario
        except:
            print(f"\n{Fore.RED}Error: No existe esa tarea{Style.RESET_ALL}") # Generamos excepción por si el usuario teclea tarea no existente

task_instance = Task() # Creamos instancia de la clase "task"

options = print(f"\n MENU PRINCIPAL\n ------------\n1- {Fore.BLUE}Mostrar tareas{Style.RESET_ALL}\n2- {Fore.BLUE}Agregar tarea{Style.RESET_ALL}\n3- {Fore.BLUE}Marcar tarea como completada{Style.RESET_ALL}\n4- {Fore.BLUE}Eliminar tarea{Style.RESET_ALL}\n5- {Fore.BLUE}Fin{Style.RESET_ALL}") # Opciones que se muestran al usuario

while True:

    action = input("\n1 Elige opción ('help' para recordar opciones): ")
    
    if action == "1": 
        task_instance.print_tasks() # Ejecuta método imprime las tareas
        
    elif action == "2": 
        task_instance.add_task() # Ejecuta método que añade las tareas

    elif action == "3":
        task_instance.task_manage() # Ejecuta método que pasa tareas a "completadas"

    elif action == "4":
        task_instance.del_task() # Ejecuta método que elimina tarea

    elif action == "5":
        task_instance.save_tasks()  # Guardar las tareas antes de salir
        break # Salir del bucle

    elif action == "help":
        print(f"\n MENU PRINCIPAL\n ------------\n1- {Fore.BLUE}Mostrar tareas{Style.RESET_ALL}\n2- {Fore.BLUE}Agregar tarea{Style.RESET_ALL}\n3- {Fore.BLUE}Marcar tarea como completada{Style.RESET_ALL}\n4- {Fore.BLUE}Eliminar tarea{Style.RESET_ALL}\n5- {Fore.BLUE}Fin{Style.RESET_ALL}") # Opciones que se muestran al usuario

    else:
        print((f"\n{Fore.RED}Error: Opción incorrecta{Style.RESET_ALL}")) # Error si no se marca opción correcta
