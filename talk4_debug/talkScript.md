# Depurando En Visual Studio Code

## Parte1: depuración local

Ponentes: Juanjo y Ramón

0. Introducción: presentando el programa que queremos depurar
1. Antes de iniciar la depuración...
   * Edición básica. Colapsar y expandir código. Atajos de teclado, paleta de comandos.
   * Breve nota sobre solucionar problemas con los sonidos de accesibilidad (audio cues).
   * Un poco sobre el autocompletado en VSCode...
   * Buscar y reemplazar. Fichero simple o múltiples ficheros. Control+F, Control+Shift+F
   * Reemplazar texto con cursores múltiples. Control+F2 (¡MUCHO CUIDADO!)
   * Renombrar identificadores de manera segura. F2
   *Localizar definiciones y referencias a variables y funciones. F12, Shift+F12. Panel outline
   * Detectar y reparar errores en tiempo de escritura. F8/Shift+F8, Control+Shift+M
2. Primeros pasos: iniciando la ejecución de nuestro programa
   * Iniciar la ejecución: F5, Control+F5, paleta de comandos (Control+Shift+P)
   * Breve explicación de los modos de ejecución: fichero, módulo, remoto, proceso
   * Errores en tiempo de ejecución. Excepciones
3. Controlando la ejecución del programa
   * Añadir y quitar puntos de interrupción (breakpoints). F9 / Shift + F9
   * Iniciando de nuevo la ejecución con puntos de interrupción.
   * Examinar variables simples y complejas. Control+K & Control+I
   * Ejecución paso a paso. F10, F11
   * La terminal y la consola de depuración.
4. Depuración avanzada
   * El panel de depuración. Control+shif+D.
   * Secciones en el panel de depuración: variables, breakpoints, watchers, call stack.
   * Examinar variables desde el panel de depuración.
   * Breakpoints condicionales y por "impactos". Breakpoints de funciones.
   * Monitorizar expresiones (watchers).
   * La pila de llamadas (call stack).
   * El panel de depuración. Creando un fichero `launch.json`.

## Parte 2: depuración de complementos y del código fuente de NVDA

Ponentes: Ramón y **
