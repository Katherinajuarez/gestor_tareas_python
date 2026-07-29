# Gestor de tareas (Python)

## Descripción
Este proyecto es una aplicación interactiva desarrollada en Python para ejecutarse directamente en la terminal. Forma parte del trabajo final para la certificación del curso de Python Inicial.

El objetivo principal es aplicar los conceptos fundamentales de programación mediante la planificación e implementación del modelo **Entrada–Proceso–Salida (EPS)**, logrando un sistema modular que permite administrar tareas pendientes y persistir la información en un archivo de texto local.

---

## Características
* **Menú interactivo:** Navegación sencilla basada en consola para seleccionar acciones.
* **Gestión de tareas:** Permite agregar tareas con título y categoría/prioridad, así como listarlas y marcarlas como completadas.
* **Validación de datos:** Control de errores mediante bloques `try/except` y validación de texto para asegurar que la categoría no contenga dígitos numéricos.
* **Persistencia de datos:** Lectura y escritura automática en un archivo `.txt` con formato descriptivo (`titulo: ..., categoria: ..., completada: ...`).

---

## Modelo EPS (Entrada–Proceso–Salida)

### 1. Entrada
* Opciones del menú interactivo elegidas por el usuario.
* Título de la tarea y categoría (restringida a texto sin números).
* Número entero correspondiente al índice de la tarea para actualizar su estado.
* Datos cargados desde el archivo local `tareas.txt`.

### 2. Proceso
* Manejo de la navegación del sistema mediante un bucle `while`.
* Lectura y procesamiento de texto (`.split()` y `.strip()`) para reconstruir los datos desde el archivo.
* Almacenamiento de cada tarea en un diccionario (`"titulo"`, `"categoria"`, `"completada"`) agrupados dentro de una lista general.
* Recorrido de listas mediante ciclos `for` por índice (`range(len(...))`).
* Validación mediante la función auxiliar `tiene_numeros()` para verificar el formato de la categoría.
* Control de excepciones mediante `try/except` ante errores de entrada o la falta del archivo inicial.

### 3. Salida
* Visualización en pantalla del menú y del listado numerado de tareas con su estado (`[Pendiente]` o `[Completada]`).
* Mensajes informativos de confirmación o advertencia de errores.
* Actualización y guardado automático en el archivo de texto `tareas.txt`.

---

## Estructura del código
El programa está estructurado en funciones modulares para garantizar la claridad y orden:

* `mostrar_menu()`: Muestra las opciones principales.
* `cargar_tareas(nombre_archivo)`: Carga los datos del archivo local al iniciar.
* `guardar_tareas(nombre_archivo, lista_tareas)`: Escribe el estado actual de las tareas en el archivo.
* `mostrar_tareas(lista_tareas)`: Imprime en consola la lista numerada.
* `tiene_numeros(texto)`: Función de validación de caracteres.
* `agregar_tarea(lista_tareas)`: Solicita, valida e inserta una nueva tarea.
* `marcar_completada(lista_tareas)`: Cambia el estado de una tarea a completada.
* `main()`: Controla el flujo general de la aplicación.
