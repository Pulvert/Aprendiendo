# Lista original
lista_original = [1, 2, 3, 4, 5]

# Índice del elemento que deseas seleccionar
indice_elemento = 2  # Por ejemplo, seleccionamos el tercer elemento (índice 2)

# Verificar si el índice está dentro del rango válido
if 0 <= indice_elemento < len(lista_original):
    # Eliminar el elemento seleccionado de la lista original y agregarlo a la nueva lista
    elemento_seleccionado = lista_original.pop(indice_elemento)
    nueva_lista = [elemento_seleccionado]
    print("Elemento seleccionado:", elemento_seleccionado)
    print("Lista original actualizada:", lista_original)
    print("Nueva lista:", nueva_lista)
else:
    print("El índice está fuera de rango.")