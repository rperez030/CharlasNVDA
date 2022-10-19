# Control de versiones.

Git y Github desde Visual Studio Code

Ponentes: Dani y Rober

## Rober: De qué va el control de versiones

Empezamos con el timeline local en Visual Studio Code para mostrar una idea básica sobre lo que significan varias versiones para un solo archivo.

Cuando tenemos un único archivo para el cuál necesitamos registrar un control de versiones, Git no es de mucha utilidad. Cuando Git realmente es útil es cuando tenemos varios archivos o carpetas de los que queremos tener un control de versiones.

Git se utiliza en varios sistemas de control de versiones modernos, incluyendo GitHub.

Múltiples formas de interactuar con Git/GitHub: línea de comandos, interfaz web de GitHub, programas de escritorio

## Dani: Repaso rápido de un flujo normal con Git y Github en la línea de comandos

Repaso verbal de un flujo de trabajo de git en la línea de comandos. Mención a la guía de Jose sobre el tema.

- Inicializar el repositorio: (git init)
- Hacer cambios
- Añadir cambios: (git add)
- Git commit
- Crear ramas: (git branch)
- moverse entre ramas: (git checkout)
- Repositorios remotos: (git remote origin [url])
- git pull
- git push

## Rober: GitHub en la web

### Visualización de un repositorio

- Código
  - Vista del explorador de archivos
  - Crear un archivo
- Issues (incidencias)
- PRs (solicitudes de cambios)
- Configuración
- Dani: Wikis
- Proyectos, milestones, etiquetas ...

### Editando los archivos de un repositorio en la web

- Rober: Editor tradicional de GitHub
- Dani: versión de VSCode en la web: GitHub.dev

## Control de versiones con Visual Studio Code

### Instalando extensiones de Visual Studio Code útiles para Git/Github

Las extensiones las traemos ya instaladas y únicamente se mencionan y se demuestran.

- GitHub Pull Requests and Issues
- Remote Repositories
- GitHub Repositories
- GitHub Lens (como sugerencia)

### Iniciando sesión en GitHub con VSCode

TBD. Cada extensión reqerirá autorización. VSCode notificará en cada momento. Se abrirá la página de GitHub y se autorizar´ra la extensión.

### Flujo de trabajo en GitHub con Visual Studio Code

- Clonar repositorio.
Dani:  Git init, clonado interactivo desde la papleta de comandos Rober clonado local
- El flujo de cambios+add+commits' en VSCode
- Panel "Source control" y vista de commits

### Crear ramas y moverse entre ellas desde VSCode

- Paleta de comandos
- Barra de estado

### Issues y pull requests

- Extensión GitHub Pull Requests and Issues
- Crear un pull request
- Revisar los cambios de un pull request
