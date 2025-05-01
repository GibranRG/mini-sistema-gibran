from gestor import GestorTareas

gestor = GestorTareas()

while True:
    print("\nGestor de Tareas")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        gestor.agregar_tarea(nombre, descripcion)
    elif opcion == "2":
        gestor.mostrar_tareas()
    elif opcion == "3":
        indice = int(input("Índice de tarea a completar: "))
        gestor.completar_tarea(indice)
    elif opcion == "4":
        indice = int(input("Índice de tarea a eliminar: "))
        gestor.eliminar_tarea(indice)
    elif opcion == "5":
        break
    else:
        print("Opción inválida")
