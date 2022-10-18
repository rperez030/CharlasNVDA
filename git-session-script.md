# Control de versiones.

Git y Github desde Visual Studio Code

Ponentes: Dani y Rober

## De qué va el control de versiones

Empezamos con el timeline local en Visual Studio Code para mostrar una idea básica sobre lo que significan varias versiones par aun solo archivo.

Cuando tenemos un único archivo para el cuál necesitamos registrar un control de versiones, Git no es de mucha utilidad. Cuando Git realmente es útil es cuando tenemos varios archivos o carpetas de los que queremos tener un control de versiones.

Git se utiliza en varios sistemas de control de versiones modernos, incluyendo GitHub.

Múltiples formas de interactuar con Git/GitHub: línea de comandos, interfaz web de GitHub, programas de escritorio

## Repaso rápido de un flujo normal con Git y Github en la línea de comandos

No vamos a entrar en detalle sobre cómo configurar el sistema operativo y autenticarse en git con la línea de comandos. Asumiremos que ya estamos autenticados.

- Inicializar el repositorio: (git init)
- Hacer cambios
- Añadir cambios: (git add)
- Git commit
- Crear ramas: (git branch)
- moverse entre ramas: (git checkout)
- Repositorios remotos: (git remote origin [url])
- git pull
- git push

## GitHub en la web

### Visualización de un repositorio

- Código
  - Vista del explorador de archivos
  - Crear un archivo
- Issues (incidencias)
- PRs (solicitudes de cambios)
- Wikis
- Configuración
- Proyectos, milestones, etiquetas ...

### Editando los archivos de un repositorio en la web

- Editor tradicional de GitHub
- versión de VSCode en la web: GitHub.dev

## Control de versiones con Visual Studio Code

### Instalando extensiones de Visual Studio Code útiles para Git/Github

- GitHub Pull Requests and Issues
- Remote Repositories
- GitHub Repositories
- GitHub Lens (Rober)

### Iniciando sesión en GitHub con VSCode

En VSCode nos vamos a administrar, cuentas, y pulsamos donde nos dice no has iniciado sesión con ninguna cuenta. Después seleccionamos iniciar sesión con GitHub y se abre el navegador para que podamos autenticarnos.

### Flujo de trabajo en GitHub con Visual Studio Code

- Inicializar repositorios
- El flujo de cambios+add+commits' en VSCode
- Panel "Source control" y vista de commits

### Crear ramas y moverse entre ellas desde VSCode

- Paleta de comandos
- Barra de estado

### Issues y pull requests

- Extensión GitHub Pull Requests and Issues
- Crear un pull request
- Revisar los cambios de un pull request
