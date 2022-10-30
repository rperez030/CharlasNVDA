# Pasos para depurar NVDA

## Paso 1. Clonar el repositorio de NVDA

1. Abre tu navegador favorito e inicia sesión en la [web de GitHub](https://www.github.com).
2. Navega al [repo de NVDA](https://github.com/nvaccess/nvda.git).
3. Crea un fork del repo de NVDA en tu propia cuenta de GitHub. Puedes dejar el nombre y descripción por defecto. Si quieres también puedes dejar marcada la casilla para clonar sólo la rama "master". Si dejas los datos por defecto, la URL de tu fork será de la forma `https://github.com/tu_usuario/nvda.git`.
4. Clona el fork que acabas de crear en tu disco duro.
5. Inicializa y actualiza los submódulos de NVDA (si no sabes cómo hacerlo, puedes leer la [Guía de introducción a Git y GitHub](https://nvda.es/documentacion/desarrollo/documentacion-de-la-comunidad-hispanohablante/guia-de-introduccion-a-git-y-github/) de la página de [NVDA en español](https://nvda.es/).

## Paso 2. Hacer un *build* del código fuente

1. Asegúrate de tener instalado Visual Studio Community 2019 o superior para poder compilar las DLLs que necesitará NVDA para funcionar.
2. Lee el README que hay en la carpeta principal del repo e instala todas las librerías que se indican para poder construir una copia funcional de NVDA.
3. Usa el comando ``scons source`` para crear el entorno virtual, compilar las DLLs y construir un NVDA que se pueda ejecutar correctamente.
