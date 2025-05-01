from tareas import Tarea

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre, descripcion):
        self.tareas.append(Tarea(nombre, descripcion))

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]

    def mostrar_tareas(self):
        for i, tarea in enumerate(self.tareas):
            print(f"{i}. {tarea}")

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
