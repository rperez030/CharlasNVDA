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
   * Juanjo: Examinando variables desde el panel de depuración. Cambiar valores en tiempo de ejecución.
   * Juanjo: Monitorizando variables y expresiones mediante watchers.
   * Ramón: Siguiendo el rastro de las variables definidas y llegando al meollo del problema.

## Parte 2: depuración de complementos y del código fuente de NVDA

Ponentes: Ramón, Gustavo y Rober

### Intro: advertencias generales

1. Charla muuuuy técnica, no intentéis esto en casa
2. lo que vamos a hacer
3. recordatorio depuración local: explicación del demoGame
   * ejecutarlo desde la terminal interna
   * crear un launch.json
   * configurar terminal externa
4. depuración remota
   * intro a la depuración remota
   * librería necesaria
   * creación del entorno virtual
   * verificar que podemos importar debugpy
   * debugpy y .listen()
   * jugando remotamente
   * wait_for_client()
   * jugando de nuevo
   * comprobando dónde están los el resultados
5. Aplicando la depuración remota para depurar addons
   * insertando el debugger en el código del addon
   * ¿por qué NVDA se reinicia contínuamente?
   * debugpy.log_to()
   * debugpy.configure(python)
   * path mappings 1
6. Depurando NVDA
   * Insertando el depurador en el inicio de NVDA
   * launch.json con dos perfiles para el inicio y para el NVDA ya ejecutándose
   * Jugando a depurar NVDA




### Depuración avanzada

1. La terminal integrada y la consola de depuración.
2. Perfiles de depuración
   * Creando un fichero `launch.json`.
   * Cambiar la terminal por defecto a la terminal externa.
3. La pila de llamadas (call stack).
autocompletado y revisión de funciones como si fueran variables
la terminal externa
logpoints
depuración remota
entorno virtual con debugpy
abriendo puerto e interfaz de conexión con 0.0.0.0
log de depuración por si acaso
esperando conexiones

### Depurando complementos

máquinas virtuales para depurar
Depurando complementos. Debugpy dentro de un complemento. WaitForClient
el puerto sólo se levanta una vez
Configurar el python que lanzará el servidor de depuración
path mappings 1
justMyCode

### Depurando NVDA

NVDA ejecutándose desde los fuentes
interceptar el propio inicio de NVDA
Engancharse a la depuración antes y después de iniciado NVDA


### Frikadas varias

remote python console
Live share & live audio
función print modificada para hablar
NVDA remote iOS y depuración con Mac
launch con configuración múltiple para lanzar y depurar en remoto a la vez

## Pasos para depurar NVDA

1. Crear una máquina virtual con el sistema que queramos depurar.
2. Instalar máquina virtual
   * NVDA instalado con el acceso directo y atajo de teclado que permita arrancarlo en caso de necesidad.
   * NVDA que se depurará, en principio el del source, pero también se puede hacer con el instalado o con un portable, aunque hay que cambiar cosas.
   * Python 3.7.9. Para crear el entorno virtual en el source y también para lanzar el subproceso de debugpy, aunque para esto último serviría una versión más reciente también.
   * Git (opcional). Es útil para clonar y mantener actualizado el repo de NVDA. Esto conviene hacerlo desde un fork, también se puede acceder a través de una carpeta compartida con el host.
   * VSCode (opcional). Aunque no es imprescindible puede ser útil para determinadas tareas en la máquina virtual.
   * TeleNVDA (opcional). Puede servir para acceder más rápidamente al guest sin necesidad de cambiar a VMware y activar la máquina con Control+G.


   conectar dos clientes por dos puertos distintos?
justMyCode
timeout en el launch
ejecutar comandos en el remoto, borrar ficheros, play de un audio...
SSH para conectar al servidor de depuración
remote python console
con la consola ejecutar un subprocess con un servidor web
