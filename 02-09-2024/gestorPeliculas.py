class Peliculas:
    
    def __init__(self, titulo):
        self.titulo = titulo
        self.completado = False
        
    def marcar_vista(self):
        self.completado = True
        
    def __str__(self):
        
        if self.completado:
            estado = 'Vista'
        else:
            estado = 'No vista'
            
        return f"{self.titulo} - {estado}"
    
class Listapelicula:
    
    def __init__(self):
        self.pelicula = []
        
    def agregar_Peliculas(self,titulo):
        peliculas = Peliculas(titulo)
        self.pelicula.append(peliculas)
        print(f"Peliculas {titulo} agregada")
        
    def marcar_vista(self, indice):
        
        if 0<= indice < len(self.pelicula):
            
            self.pelicula[indice].marcar_vista()
            
            print(f"Pelicula {self.pelicula[indice].titulo} marcada como vista")
        else:
            print("Indice de la Pelicula no valido")
            
    def mostrar_pelicula(self):
        
        if self.pelicula:
            print("Lista de Peliculas")
            for i, Peliculas in enumerate(self.pelicula):
                print(f"{i}. {Peliculas}")
        else:
            print("No hay Peliculas en la lista.") 
            
    
    
def mostrar_menu():
    print("\nGestor de lista de Peliculas")
    print("1. Agregar Peliculas")
    print("2. Marcar Peliculas como Vista")
    print("3. Mostrar todas las pelicula")
    print("4. Salir")
    
    
def main():
    
    lista_pelicula = Listapelicula()
    
    while True:
        mostrar_menu() 
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            titulo = input("Ingrese el titulo de la Pelicula: ")
            lista_pelicula.agregar_Peliculas(titulo)
        elif  opcion == "2":
            lista_pelicula.mostrar_pelicula()
            indice = int(input("Seleccione el numero de la Pelicula a marcar como vista: "))
            lista_pelicula.marcar_vista(indice)  
        elif  opcion == "3":
            lista_pelicula.mostrar_pelicula()
        elif  opcion == "4":
            print("Saliendo del gestor de pelicula...")
            break
        else:
            print("Opcion no valida. Intenta de nuevo")
            
main()                    