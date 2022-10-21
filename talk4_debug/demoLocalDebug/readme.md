# Demo de depuración local

El programa `classify.py` lee los ficheros dentro de una carpeta dada (DIRECTORY) y los clasifica según un tamaño límite (SIZE_LIMIT), exportando a continuación dos CSV `small.csv` y `large.csv` con el nombre, tamaño y fecha de cada fichero.

## Contenido de la carpeta

En el directorio `demoLocalDebug` de la demo hay dos subdirectorios:

* `good`: el programa funcionando. Se puede enseñar al principio para que se vea lo que debería hacer.
* `bad`: el mismo programa con distintos estropicios que intentaremos arreglar en la sesión.

En cada uno de esos directorios hay una serie de ficheros python y una carpeta con (falsas) imágenes que el programa deberá clasificar. El programa principal está en el fichero `classify.py` y en el paquete utils hay una serie de módulos necesarios para su funcionamiento.

## Presentación de la demo

Primero enseñaremos el programa funcionando (good) para que se vea cuál es el objetivo a conseguir. Luego enseñaremos el programa "estropeado" y los distintos "fixes" que tendremos que hacer para arreglarlo:

1. Usando la extensión Pylance de Microsoft detectaremos automáticamente errores de sintaxis y de otro tipo que sean detectables antes de ejecutar nada.
2. Ejecutaremos el programa una vez corregidos los errores y veremos cómo tratar con las excepciones que salten (algunas de ellas  podrían haberse detectado también automáticamente).
3. Una vez que el programa "funcione" veremos que no lo está haciendo bien (pondrá casi todos los ficheros en el `large.csv`). Entonces usaremos puntos de interrupción, examinaremos variables, etc.

## Fallos introducidos en el programa con errores

1. classify.py: Cambiado el nombre de la librería `os` por `oos`. El linter dará varios warnings relacionados con esto.
2. classify.py: Cambiada la palabra reservada `def` por `deff`. Esto dará un error en el linter y varios fallos más de sintaxis, indentación o variables no existentes por no haber interpretado bien la línea de definición de la función.
3. utils/constants.py: Cambiado un `=` por `==`. Si abrimos todos los ficheros esto dará varios warnings en el linter por no existir la variable. Podemos esperar a hacerlo cuando salte la primera excepción.
4. utils/output.py: eliminados los dos puntos finales en la definición de la función getTotalSize. Esto no dará error en el linter salvo que se abra explícitamente el fichero en VSCode, pero dará una excepción al arrancar el programa.
5. Eliminada la carpeta "csv" del raíz. Esto dará un error en tiempo de ejecución al no poder guardar los CSV.
6. utils/constants.py: Cambiado el valor de KB introduciendo un punto que hace que su valor sea de 1,024 en lugar de 1024. El lector de pantalla no se entera porque lee igual los dos valores. Esto no se puede detectar de forma automática y tampoco provocará una excepción, sino que deberemos investigarlo usando la depuración.

## Pasos de la demo

### Antes de comenzar

1. Hay que tener instalado Python en el sistema (por ejemplo, Python 3.7.9, que es el que usa NVDA).
2. Instalar también las extensiones de Python y Pylance de Microsoft en VSCode.
3. Para iniciar las demos hay que abrir en VSCode las carpetas `good` o `bad` (no la carpeta de la demo) para que funcionen las rutas relativas que tiene que leer el programa.
4. Si al iniciar la depuración no nos sale el diálogo para elegir el modo de depuración hay que ir a "mostrar todas las configuraciones automáticas de depuración" y elegir la de Python.

### Primeros pasos

1. Abrimos sólo el `classify.py` y pasamos el linter con Control+Shift+M. Corregir los fallos que saldrán por el cambio de nombre en la librería y en la palabra reservada.
2. Arrancamos la depuración. Como no hemos usado el linter en todos los ficheros, saltarán distintas excepciones causadas por los puntos 3 y 4 anteriores. Usamos el linter en todos y corregimos todo lo que salga.
3. Arrancamos de nuevo la depuración. Salta otra excepción porque la carpeta `csv` para exportar los ficheros no existe. La creamos y arrancamos de nuevo.
4. En teoría ahora el programa no da fallos, pero clasifica mal por el punto 6 anterior. Aquí habrá que tracear el programa y ver lo que pasa.

### Trazando el programa

1. Estudiamos lo que hace el programa principal (tras el if __name__) para ver por dónde empezar
2. Como el error es obviamente de de clasificación, empezamos poniendo un breakpoint en la línea donde se llama a la función `classifyBySize()`.
3. Iniciamos la depuración, se parará en el breakpoint y enseñamos el uso de F10 para ir paso a paso. Miramos lo que hay en las variables `small` y `big`
4. Como F10 ejecuta la línea entera en ese punto ya no nos sirve de mucho porque nos hemos saltado la función entera. Reiniciamos y usamos F11 en su lugar y luego F10 por la función..
5. Pasamos varias veces con F10 por el bucle for para ver que se están yendo todos los ficheros al `bigFiles`. Salimos con Shift+F11 para enseñarlo y continuar.
6. Añadimos un breakpoint en el bucle que pare tras 5 impactos. Reiniciamos y examinamos lo que hay en `bifFiles` y `smallFiles`.
7. Añadimos un breakpoint condicional para que pare siempre que el `file.size <= 0.1 * 1024 * 1024*`. Reiniciamos y observamos lo que pasa.
8. Volvemos a empezar. Nos volvemos a meter en la función y la examinamos para ver bien lo que hace. Colocamos un breakpoint dentro del if donde se decide a dónde va el fichero y un watcher con `file.size` y otro con `file.size <= maxSize`.
9. Al ver que está fallando la comparación examinamos `maxSize` (los tamaños están bien). Buscamos su definición con F12, y a su vez la de SIZE_LIMIT y la de KB, donde descubriremos el fallo.

