# Máquinas virtuales con VMware Workstation

## Índice de contenidos

0. Introducción. ¿Qué es una máquina virtual? Diferencias entre VMware Workstation Player y Pro
1. Descargar una imagen ISO de Windows.
2. Descargar e instalar VMware Player.
3. Crear una máquina virtual. Disco duro, memoria, red.
4. Instalar Windows en la máquina virtual usando el Narrador.
5. Instalar VMware Tools.
6. Configurar carpetas compartidas entre el anfitrión y el huésped.
7. Instalar NVDA en el huésped (mediante USB o usando carpetas compartidas).
8. Comprobar la configuración de red. Otras configuraciones de red.
9. Otras opciones disponibles en VMware Workstation Pro.

## Introducción. ¿Qué es una máquina virtual?

TBD. Work in progress.

## Antes de empezar: descargar imagen ISO de Windows 10

Al igual que un ordenador físico, una máquina virtual no sirve para nada si no instalamos un sistema operativo. Por este motivo, antes de crear siquiera la máquina virtual vamos a descargar una imagen ISO de instalación de Windows 10, que será el sistema que instalaremos. Para ello seguimos los siguientes pasos:

1. Descarga la herramienta de creación de medios de Windows:
   - Abre un navegador y busca "descargar imagen iso windows 10". Normalmente el primero de los resultados será el que buscamos: "Descargar imagen de disco de Windows 10 (archivo ISO)", en el sitio web de Microsoft.
   - Entra en ese enlace y navega al encabezado de nivel 2 llamado "¿Estás deseando instalar Windows 10 en tu PC?", y luego pulsa el botón que hay justo a continuación, llamado "Descargar ahora la herramienta".
   - Guarda el fichero "MediaCreationTool21H2.exe" en tu disco duro.
2. Crea una imagen ISO del disco de instalación de Windows:
   - Ejecuta el fichero recién descargado para iniciar la herramienta de creación de medios de Windows.
   - Deberás aceptar la licencia para poder continuar con el proceso de creación de medios.
   - Elige "Crear medios de instalación (unidad flash USB, DVD o archivo ISO) para otro PC" y pulsa "Siguiente".
   - Elige el idioma de instalación y la arquitectura del procesador. Por defecto está marcada la opción "usa las opciones recomendadas para este equipo", pero podemos elegir otras, por ejemplo: español, windows 10, 64 bit.
   - Elige "archivo ISO" para descargar una imagen ISO del disco de instalación; más adelante mmontaremos esta imagen como una unidad extraíble desde VMware.
   - Guarda la imagen ISO en tu ordenador. Es recomendable darle un nombre identificativo con la versión y el idioma, por ejemplo: "windows10_64bit_es.iso". Ten en cuenta que el archivo descargado ocupará algo más de 4 GB, y por lo tanto el sistema de archivos de la unidad donde lo vayas a guardar deberá ser NTFS o extFAT (FAT32 no admite ficheros de más de 4 GB).
   - Pulsa "Finalizar" en la última pantalla para cerrar la herramienta de creación de medios.

## Descargar e instalar VMware Workstation Player

- En un navegador, buscar "descargar vmware player". Dos encabezados y "descargar ahora"
- Instalación:
  - Moverse con tabulador o con revisión de objetos para leer los mensajes
  - Dejar la carpeta por defecto (o elegir si quieres)
  - Preferible marcar "Enhanced keyboard driver" y "add vmware console tools into system path"
  - Marcar : "check for updates at startup" y desmarcar "join the vmware customer experience improvement program"
  - Shortcuts: indiferente la de "desktop", preferible marcar la del "start menu" para poder buscarlo con cortana
  - Finish, y Cuando termine otra vez "finish" (salvo que tengamos una licencia, aunque también se puede meter luego).
  - Pedirá reiniciar el equipo, lo ideal es hacerlo ya mismo
- Para iniciar VMware player buscarlo en Cortana. Estará marcada la opción "use vmware player for free", nos da la opción para comprar una licencia. Pulsar en "continue" y a continuación "finish".

## Crear una máquina virtual

- Para crear una máquina virtual necesitaremos una imagen del sistema operativo que queramos instalar, para lo cual nos sirve la del paso anterior...
- Create new virtual machine
- Select ISO -> Browse. Nos dirá que ha autodetectado la versión de windows... Next
- Nombre de la máquina: para identificarla en el panel de VMware. Por ejemplo: "Windows 10 64bit - English"
- Location: donde queramos guardarla, puede ser una unidad externa, pero ojo con el rendimiento. También puede ser otra partición.
- Maximum size: el tamaño que se "verá" desde dentro de la máquina, el disco es virtual y el fichero irá creciendo si se necesita. Se puede dejar por defecto (60 GB), depende de lo que vayamos a hacer con esa máquina.
- Split disk / single file: da un poco igual en cuanto a rendimiento, puede ser útil partirlo si queremos mover la máquina a FAT32 (limitada a < 4GB).>)
- Nos mostrará una lista con las características de la máquina. Aquí podemos cambiar por ejemplo la memoria asignada o el tipo de red, entre otras cosas. Por ejemplo, asignarle 4096 MB de memoria y la red en "bridge". Conviene por lo menos echarle un vistazo a la lista.
- Podemos marcar la opción de "power on after creation" para que la arranque al terminar.Finish

## Instalar Windows

- La máquina virtual se arranca, pero todavía no podemos oírla porque no se ha iniciado el sistema. Con NVDA+R podemos hacer OCR y vemos que estamos en el arranque WEFI.
- Para poder enviar teclas a la máquina virtual necesitamos que capture el teclado, Podemos hacerlo con el menú (Alt y luego buscar "full screen"), o también hay una tecla rápida que por defecto es Control+Alt+Enter. Oiremos "panel, bloqueo numérico desactivado". Sobre todo lo podemos comprobar pulsando Alt+Tab, y si no cambia al resto de ventanas es que estamos dentro de la máquina. Pulsamos Enter (arrancar) y luego una tecla.
- Para dejar de enviar teclas a la máquina (volver al host) pulsamos Control+Alt, podemos hacer OCR hasta comprobar que se arranca el programa de instalación.
- En cuanto esté sobre el programa de instalación, volvemos a controlar la máquina con Control+Alt+Enter y ahí ya podemos iniciar Narrator con Control+Windows+Enter. A partir de ahí seguimos la instalación como si fuera un ordenador de verdad. Narrator nos irá hablando, pero también podemos ir haciendo OCR de vez en cuando desde el host.

## VMware tools

- Pulsar ControlAlt para controlar el host. Pulsar Alt para ir al menú, y buscar "manage", abrir el submenú y pulsar "install VMware tools".
- Si no arranca directamente, abrir el explorador y desde ahí ir a "este equipo" y buscar el DVD, pedirá elevar privilegios y se iniciará la instalación. Siguiente, siguiente, siguiente...

## Carpetas compartidas entre la máquina y el sistema anfitrión

- Control+Alt para controlar el host.
- Alt para abrir el menú. Buscar "manage" y "settings".
- Buscar las pestañas e ir a "options". En el listado bajar hasta "shared folders".
- Activar "always enabled" y "map as a network drive".
- En el listado no tendremos ninguna de momento. Seguir tabulando hasta "add" y ajustar la carpeta del host y el nombre que tendrá en el guest. También si es "read only" o para lectura y escritura.
- Tabular hasta "ok" y listo.

## Verificar la configuración de la red

- Podemos hacerlo con la terminal o desde las opciones de red...

## Otras posibilidades

[Tutorial: instalación de Arch Linux de forma accesible](https://qcsalon.net/es/forum1000000/topic101902)
