# Depurando En Visual Studio Code

## Parte1: depuración local

Ponentes: Juanjo y Ramón

### Introducción a la demo

0. Ramón: Aclaraciones previas
   * Es una charla hipertécnica, se asume conocimientos de Python, programación, uso de la terminal, etc.
   * La demo estará alojada en GitHub por si alguien quiere intentar seguirla, aunque eso será mejor offline y parando el audio.
1. Presentando los objetivos
   * Juanjo: Abrir la carpeta y enseñar un poco su estructura y explicar lo que se persigue.
   * Juanjo: Abrir una terminal en la carpeta del programa y ejecutarlo con `py classify.py`.
   * Juanjo: Leer la salida del programa y examinar el resultado en la carpeta "csv".
   * Juanjo: Abrir la carpeta en VSCode como espacio de trabajo con `code .`.
   * Ramón: abrir el mismo workspace desde el menú contextual del explorador de archivos de Windows.
   * Ramón: recordatorio del explorador de archivos de VSCode y cómo moverse entre archivos. Control+Shift+E. Alt+números. Control+números. Control+M.
   * Ramón: Repaso rápido del código y navegación básica. Colapsar y expandir código. Atajos de teclado, paleta de comandos. Panel de outline.
   * Ramón: Breve nota sobre solucionar problemas con los sonidos de accesibilidad (audio cues).
2. Antes de empezar: un poco de edición básica y manejo de la interfaz
   * Juanjo: Buscar y reemplazar. Fichero simple o múltiples ficheros. Control+F, Control+Shift+F Opciones en este panel de búsqueda.
   *Juanjo: Localizar definiciones y referencias a variables y funciones. F12, Shift+F12. Recordar de nuevo el panel outline.
   * Ramón: Reemplazar texto con cursores múltiples. Control+F2 (¡MUCHO CUIDADO!)
   * Ramón: Renombrar identificadores de manera segura. F2
   * Ramón: Un poco sobre el autocompletado en VSCode. Ventajas e inconvenientes. Posibles settings.

### Comienzo de la demo

0. Juanjo: Recordatorio de lo que hay que tener instalado: Python 3.x y extensiones de Python y Pylance.
1. Corrección de errores de sintaxis (en tiempo de escritura)
   * Juanjo: Detectar y reparar errores con el linter de Pylance: item de la barra de estado, Control+Shift+M, F8/Shift+F8.
   * Ramón: primer intento de ejecución: Paleta de comandos/F5/Control+F5 y los modos de depuración (fichero, módulo, remoto, proceso, otros).
   * Ramón: primeras escepciones. Vuelta a pasar el linter.
   * Juanjo: Falta la carpeta "csv". Errores en tiempo de ejecución no causados directamente por el código
   * Juanjo: el programa ya se ejecuta, ¿y ahora qué? Análisis del resultado fallido.

### Trazando el programa

1. Ejecución paso a paso. Conceptos básicos
   * Ramón: Añadir y quitar puntos de interrupción (breakpoints). F9 / Shift + F9. Parar y reiniciar: F5/Shift+F5.
   * Ramón: Examinar variables simples y complejas. Control+K & Control+I. El árbol de una variable.
   * Juanjo: Ejecución paso a paso. F10 (ejecuta la línea), F11 (se mete en la función).
   * Juanjo: paso a paso dentro de la función. Iterando el bucle y examinando `file.size`. Salir con Shift+F11.
2. El panel de depuración
   * Ramón: Abrir el panel de depuración. Control+Shift+D. Posibles problemas con el depurador de Python.
   * Ramón: Resumen de las secciones del panel de depuración.
   * Ramón: Breakpoints condicionales por expresiones y por número de hits. Seguimos examinando variables.
   * Juanjo: Examinando variables desde el panel de depuración.
   * Juanjo: Monitorizando variables y expresiones mediante watchers.
   * Ramón: Siguiendo el rastro de las variables definidas y llegando al meollo del problema.

### Depuración avanzada

1. Ramón: La terminal integrada y la consola de depuración.
2. Juanjo: La pila de llamadas (call stack).

## Parte 2: depuración de complementos y del código fuente de NVDA

Ponentes: Ramón y **

1. El panel de depuración. Creando un fichero `launch.json`.
