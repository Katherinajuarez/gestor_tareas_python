# Proyecto: Gestor de tareas

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Guardar tareas en archivo")
    print("5. Salir")


def cargar_tareas(nombre_archivo):
    lista_tareas = []
    try:
        archivo = open(nombre_archivo, "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            linea = linea.strip()
            if linea != "":
                # Separamos por coma los tres campos
                partes = linea.split(",")
                
                # Extraer el valor omitiendo el encabezado
                titulo_con_clave = partes[0].split(":")
                titulo = titulo_con_clave[1].strip()

                categoria_con_clave = partes[1].split(":")
                categoria = categoria_con_clave[1].strip()

                completada_con_clave = partes[2].split(":")
                valor_completada = completada_con_clave[1].strip()

                if valor_completada == "True":
                    completada = True
                else:
                    completada = False

                tarea = {
                    "titulo": titulo,
                    "categoria": categoria,
                    "completada": completada
                }
                lista_tareas.append(tarea)
        print("Tareas cargadas correctamente desde el archivo.")
    except:
        print("No se encontro un archivo previo o esta vacio. Se creara una lista nueva.")

    return lista_tareas


def guardar_tareas(nombre_archivo, lista_tareas):
    try:
        archivo = open(nombre_archivo, "w")
        for i in range(len(lista_tareas)):
            tarea = lista_tareas[i]
            # Formato de guardado: titulo: ?, categoria: ?, completada: ?
            linea = "titulo: " + tarea["titulo"] + ", categoria: " + tarea["categoria"] + ", completada: " + str(tarea["completada"]) + "\n"
            archivo.write(linea)
        archivo.close()
        print("Tareas guardadas exitosamente en", nombre_archivo)
    except:
        print("Ocurrio un error al intentar guardar el archivo.")


def mostrar_tareas(lista_tareas):
    if len(lista_tareas) == 0:
        print("\nNo hay tareas registradas.")
    else:
        print("\n--- LISTA DE TAREAS ---")
        for i in range(len(lista_tareas)):
            tarea = lista_tareas[i]
            if tarea["completada"]:
                estado = "Completada"
            else:
                estado = "Pendiente"
            
            numero = i + 1
            print(str(numero) + ". [" + estado + "] " + tarea["titulo"] + " (Categoria: " + tarea["categoria"] + ")")


def tiene_numeros(texto):
    # Funcion auxilar que valida que la categoria no contenga numeros, solo texto
    numeros = "0123456789"
    for caracter in texto:
        if caracter in numeros:
            return True
    return False


def agregar_tarea(lista_tareas):
    print("\n--- AGREGAR NUEVA TAREA ---")
    titulo = input("Ingrese el titulo de la tarea: ").strip()
    categoria = input("Ingrese la categoria o prioridad: ").strip()

    if titulo == "" or categoria == "":
        print("Error: El titulo y la categoria no pueden estar vacios.")
    elif tiene_numeros(categoria):
        print("Error: La categoria no puede contener numeros, solo texto.")
    else:
        nueva_tarea = {
            "titulo": titulo,
            "categoria": categoria,
            "completada": False
        }
        lista_tareas.append(nueva_tarea)
        print("Tarea agregada correctamente.")


def marcar_completada(lista_tareas):
    mostrar_tareas(lista_tareas)
    if len(lista_tareas) > 0:
        try:
            opcion = input("\nIngrese el numero de la tarea a marcar como completada: ")
            indice = int(opcion) - 1

            if indice >= 0 and indice < len(lista_tareas):
                lista_tareas[indice]["completada"] = True
                print("Tarea marcada como completada.")
            else:
                print("Error: El numero ingresado no corresponde a ninguna tarea.")
        except:
            print("Error: Debe ingresar un numero entero valido.")


def main():
    archivo_datos = "tareas.txt"
    tareas = cargar_tareas(archivo_datos)
    
    ejecutando = True
    while ejecutando:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-5): ").strip()

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            guardar_tareas(archivo_datos, tareas)
        elif opcion == "5":
            guardar_tareas(archivo_datos, tareas)
            print("Saliendo del programa. Hasta luego!")
            ejecutando = False
        else:
            print("Opcion invalida. Por favor, seleccione un numero del 1 al 5.")


main()