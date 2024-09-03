class Tarea:
    def __init__(self, titulo):
        self.titulo = titulo
        self.completado = False
        
    def marcar_completada(self):
        self.completado= True
    
    def __str__(self):
        if self.completado:
            estado = 'Completado'
        else:
            estado = 'Pendiente'
        return (f"{self.titulo} - {estado}")

class ListaTareas:
    
    def __init__(self):
        self.tareas = []
    
    def agregar_tareas(self, titulo):
        tarea = Tarea(titulo)
        self.tareas.append(tarea)
        print(f"Tarea {titulo} agregada")

    def marcar_completado (self,indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
            print(f"Tarea {self.tareas[indice].titulo} marcada como  completada")
        else:
            print("indice de la tarea no valido")
    
    def mostrar_tareas (self):
        if self.tareas:
            print(f"Lista de Tareas")
            for i, tarea in enumerate(self.tareas):
                print(f"{i}.{tarea}")
        else:
            print("No existe elementos en la lista")

    
def mostrar_menu():
    print("\nGestor Lista de Tareas")
    print("1. Agregar Tarea")
    print("2. Marcar Tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Salir")

def main():
    lista_tareas= ListaTareas()
    while True:
        mostrar_menu()
        opcion = input("Seleccion una opcion: ")
        if opcion=="1":
            titulo = input("Ingrese el titulo de la tarea")
            lista_tareas.agregar_tareas(titulo)
        elif opcion =="2":
            lista_tareas.mostrar_tareas()
            indice = int(input("Seleccione el numero de la tarea a marcar como completada"))
            lista_tareas.marcar_completado(indice)
        elif opcion=="3":
            lista_tareas.mostrar_tareas()
        elif opcion=="4":
            print("Saliendo del gestor de Tareas...")
            break
        else:
            print("Opcion no validad")
main()