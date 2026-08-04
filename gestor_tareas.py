# Proyecto: Gestor de tareas

class Tarea:
    def __init__(self, titulo, categoria, completada=False):
        self.titulo = titulo
        self.categoria = categoria
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

    def obtener_estado_texto(self):
        if self.completada:
            return "Completada"
        return "Pendiente"

    def a_linea_archivo(self):
        # Convierte el objeto a formato de texto para guardar en tareas.txt
        return "titulo: " + self.titulo + ", categoria: " + self.categoria + ", completada: " + str(self.completada) + "\n"


class GestorTareas:
    def __init__(self, nombre_archivo="tareas.txt"):
        self.nombre_archivo = nombre_archivo
        self.lista_tareas = []
        self.cargar_tareas()

    def cargar_tareas(self):
        try:
            archivo = open(self.nombre_archivo, "r")
            lineas = archivo.readlines()
            archivo.close()

            for linea in lineas:
                linea = linea.strip()
                if linea != "":
                    partes = linea.split(",")
                    
                    titulo = partes[0].split(":")[1].strip()
                    categoria = partes[1].split(":")[1].strip()
                    valor_completada = partes[2].split(":")[1].strip()

                    completada = True if valor_completada == "True" else False
                    
                    # Crear un objeto de tipo Tarea y agregarlo a la lista
                    nueva_tarea = Tarea(titulo, categoria, completada)
                    self.lista_tareas.append(nueva_tarea)

            print("Tareas cargadas correctamente desde el archivo.")
        except:
            print("No se encontro un archivo previo o esta vacio. Se creara una lista nueva.")

    def guardar_tareas(self):
        try:
            archivo = open(self.nombre_archivo, "w")
            for i in range(len(self.lista_tareas)):
                tarea = self.lista_tareas[i]
                archivo.write(tarea.a_linea_archivo())
            archivo.close()
            print("Tareas guardadas exitosamente en", self.nombre_archivo)
        except:
            print("Ocurrio un error al intentar guardar el archivo.")

    def mostrar_tareas(self):
        if len(self.lista_tareas) == 0:
            print("\nNo hay tareas registradas.")
        else:
            print("\n--- LISTA DE TAREAS ---")
            for i in range(len(self.lista_tareas)):
                tarea = self.lista_tareas[i]
                numero = i + 1
                print(str(numero) + ". [" + tarea.obtener_estado_texto() + "] " + tarea.titulo + " (Categoria: " + tarea.categoria + ")")

    def agregar_tarea(self, titulo, categoria):
        nueva_tarea = Tarea(titulo, categoria)
        self.lista_tareas.append(nueva_tarea)
        print("Tarea agregada correctamente.")

    def marcar_completada(self, indice):
        if indice >= 0 and indice < len(self.lista_tareas):
            self.lista_tareas[indice].marcar_completada()
            print("Tarea marcada como completada.")
            return True
        else:
            print("Error: El numero ingresado no corresponde a ninguna tarea.")
            return False


# Menu de opciones para el usuario
def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Guardar tareas en archivo")
    print("5. Salir")


def tiene_numeros(texto):
    numeros = "0123456789"
    for caracter in texto:
        if caracter in numeros:
            return True
    return False


def main():
    # Iniciamos el objeto gestor que administra las tareas
    gestor = GestorTareas("tareas.txt")
    
    ejecutando = True
    while ejecutando:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-5): ").strip()

        if opcion == "1":
            gestor.mostrar_tareas()

        elif opcion == "2":
            print("\n--- AGREGAR NUEVA TAREA ---")
            titulo = input("Ingrese el titulo de la tarea: ").strip()
            categoria = input("Ingrese la categoria o prioridad: ").strip()

            if titulo == "" or categoria == "":
                print("Error: El titulo y la categoria no pueden estar vacios.")
            elif tiene_numeros(categoria):
                print("Error: La categoria no puede contener numeros, solo texto.")
            else:
                gestor.agregar_tarea(titulo, categoria)

        elif opcion == "3":
            gestor.mostrar_tareas()
            if len(gestor.lista_tareas) > 0:
                try:
                    num = input("\nIngrese el numero de la tarea a marcar como completada: ")
                    indice = int(num) - 1
                    gestor.marcar_completada(indice)
                except:
                    print("Error: Debe ingresar un numero entero valido.")

        elif opcion == "4":
            gestor.guardar_tareas()

        elif opcion == "5":
            gestor.guardar_tareas()
            print("Saliendo del programa. Hasta luego!")
            ejecutando = False

        else:
            print("Opcion invalida. Por favor, seleccione un numero del 1 al 5.")


main()
