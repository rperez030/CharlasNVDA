# Control de versiones. Git y Github desde Visual Studio Code

Ponentes: Dani y Rober

## De qué va el control de versiones.

Empezamos conEl timeline local en Visual Studio Code.

Cuando tenemos un único archivo para el cuál necesitamos registrar un control de versiones, Git no es de mucha utilidad. Cuando Git realmente es útil es cuando tenemos varios archivos o carpetas de los que queremos tener un control de versiones.

Git se utiliza en varios sistemas de control de versiones modernos, incluyendo GitHub.

Múltiples formas de interactuar con Git/GitHubb: línea de comandos, interfaz web de GitHub, programas de escritorio

## Repaso rápido de un flujo normal con Git y Github en la línea de comandos:

No vamos a entrar en detalle sobre cómo configurar el sistema operativo y autenticarse en git con la línea de comandos. Asumiremos que ya estamos autenticados.

- Inicializar el repositorio (git init)
- Hacer cambios 
- Git add 
- Git commit
- Crear ramas git tbranch 
- moverse entre ramas: git checkout
- Repositorios remotos: git remote origin [url]
- pull 
- push

## GitHub en la web

### Visualización de un repositorio

- Código
  - Vista del explorador de archivos
  - Crear un archivo
- Issues
- PRs
- Wikis
- Configuración
- Proyectos, milestones, etiquetas ...

### Editando los archivos de un repositorio en la web

- Editor tradicional de GitHub
- versión de VSCode en la web: GitHub.dev 

## Control de versiones con Visual Studio Code

### Instalando extensiones de Visual Studio Code útiles para Git/Github

- GitHub Pull Requests and Issues
- GitHub Remote
- GitHub Repositories
- GitHub Lens???

### Iniciando sesión en GitHub con VSCode

En VSCode nos vamos a administrar, cuentas, y pulsamos donde nos dice no has iniciado sesión con ninguna cuenta. Después seleccionamos iniciar sesión con GitHub y se abreel navegador para que podamos autenticarnos.

### Flujo de trabajo en GitHub con Visual Studio Code

- Inicializar repositorios
- El flujo de cambios+add+commmit en VSCode
- Panel "Source control" y vista de commits

### Crear ramas y moverse entre ellas desde VSCode

- Paleta de comandos
- Barra de estado

### Issues y pull requests

- Extensión GitHub Pull Requests and Issues
