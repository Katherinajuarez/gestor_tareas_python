# Gestor de Tareas en Terminal (Python - Versión POO)

## Descripción
Este proyecto es una aplicación interactiva desarrollada en Python para ejecutarse directamente en la terminal. Forma parte del trabajo final para la certificación del curso de Python Inicial.

El objetivo principal es planificar e implementar un proyecto utilizando el modelo **Entrada–Proceso–Salida (EPS)**, incorporando los conceptos fundamentales del lenguaje junto con una introducción a la **Programación Orientada a Objetos (POO)** para lograr una arquitectura modular, escalable y mantenible.

---

## Características
* **Modelo Orientado a Objetos:** Separación clara de responsabilidades entre el modelo de datos (`Tarea`) y la lógica de administración (`GestorTareas`).
* **Menú interactivo:** Navegación en consola para la gestión fluida de tareas.
* **Persistencia de datos:** Lectura y escritura en un archivo `.txt` local con un formato descriptivo e identificadores explícitos.
* **Validación de entradas:** Control de errores de formato (restricción de dígitos numéricos en la categoría) y manejo seguro de datos numéricos.
* **Manejo de excepciones:** Prevención de caídas del programa ante la ausencia del archivo de datos o entradas inválidas del usuario.

---

## Modelo EPS (Entrada–Proceso–Salida)

### 1. Entrada
* **Interfaz de usuario (`input()`):**
  * Opción seleccionada del menú principal (1 al 5).
  * Título de la tarea y categoría/prioridad (validada solo para letras).
  * Índice entero de la tarea a completar.
* **Almacenamiento externo:**
  * Lectura del archivo `tareas.txt` con formato: `titulo: <texto>, categoria: <texto>, completada: <True/False>`.

### 2. Proceso
* **Modelado con POO:**
  * **Clase `Tarea`:** Encapsula el título, la categoría y el estado de la tarea. Incluye métodos para cambiar estado (`marcar_completada()`), consultar estado formateado (`obtener_estado_texto()`) y convertir el objeto a texto para archivo (`a_linea_archivo()`).
  * **Clase `GestorTareas`:** Administra la lista de objetos `Tarea` (`self.lista_tareas`), controlando la carga, guardado, alta y actualización de tareas.
* **Procesamiento de archivos:**
  * Parseo de cadenas mediante `.split(",")`, `.split(":")` y `.strip()` para reconstruir e instanciar cada objeto `Tarea`.
* **Validaciones y Control de flujo:**
  * Función auxiliar `tiene_numeros()` con recorrido `for` para validar cadenas.
  * Ciclo `while` en `main()` para el menú interactivo y condicionales `if-elif-else` para invocar métodos del gestor.
* **Excepciones:**
  * Bloques `try/except` para manejar la falta del archivo de datos o errores al ingresar números enteros.

### 3. Salida
* **Consola (`print()`):**
  * Menú principal y listado numerado de tareas con estado (`[Pendiente]` o `[Completada]`).
  * Mensajes de confirmación y de error detallados.
* **Almacenamiento externo:**
  * Escritura/actualización del archivo `tareas.txt` guardando cada tarea en una línea estructurada.

---

## Arquitectura de Clases

* `Tarea`: Representa una entidad de tarea individual.
  * Atributos: `titulo`, `categoria`, `completada`.
  * Métodos: `marcar_completada()`, `obtener_estado_texto()`, `a_linea_archivo()`.
* `GestorTareas`: Administra la colección de tareas y la persistencia.
  * Atributos: `nombre_archivo`, `lista_tareas`.
  * Métodos: `cargar_tareas()`, `guardar_tareas()`, `mostrar_tareas()`, `agregar_tarea()`, `marcar_completada()`.
