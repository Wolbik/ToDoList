# To-Do List

**Descripción**  
_To-Do List_ es una aplicación de gestión de tareas sencilla que permite a los usuarios crear, editar y eliminar tareas. El proyecto está desarrollado en Python y utiliza una interfaz de línea de comandos para interactuar con el usuario.

## Tecnologías:

- **Lenguaje de Programación**: Python 3.x
- **Framework**: No se utiliza un framework específico
- **Dependencias**: Las bibliotecas necesarias están incluidas en el archivo `requirements.txt`.

## Esquema de almacenamiento:

No se utiliza una base de datos. Los datos se almacenan en archivos locales en formato JSON.

## Cómo ejecutar el proyecto:

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/tu-usuario/ToDolist.git
   cd ToDolist
   ```

2. **Instalar las dependencias**:
   Asegúrate de tener Python 3.x y `pip` instalados, luego ejecuta:

   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**:
   Para iniciar la aplicación, simplemente ejecuta el siguiente comando:
   ```bash
   python main.py
   ```

## Cómo ejecutar las pruebas:

1. **Instalar `pytest`**:  
   Si no tienes `pytest` instalado, ejecuta el siguiente comando:

   ```bash
   pip install pytest
   ```

2. **Ejecutar las pruebas**:
   Para correr todas las pruebas unitarias, usa:
   ```bash
   pytest
   ```

## CI/CD con GitHub Actions

Este proyecto utiliza **GitHub Actions** para automatizar la ejecución de las pruebas cada vez que se abre un _pull request_ hacia la rama `QA`.

### Flujo de Trabajo (Workflow):

El archivo de configuración del workflow se encuentra en `.github/workflows/python-tests.yml`. El workflow sigue los siguientes pasos:

1. **Clona el repositorio** en el entorno del runner.
2. **Configura Python** en la versión especificada (actualmente Python 3.x).
3. **Instala las dependencias** listadas en el archivo `requirements.txt`.
4. **Ejecuta las pruebas** utilizando `pytest`.

### Trigger de Ejecución

El workflow se ejecuta automáticamente cuando:

- Se crea o actualiza un _pull request_ apuntando a la rama `QA`.

### Manejo de Fallos

Si alguna prueba falla, el workflow falla y los cambios no pueden ser fusionados hasta que todas las pruebas pasen correctamente.

## Contribuidores:

- **Rosanna Bautista** - 1105980 | GitHub: [rosannabautista](https://github.com/rosannabautista)
- **Jean Azar** - 1104992 | GitHub: [Jcazt21](https://github.com/Jcazt21)
- **Samir Moammer** - 1106232 | GitHub: [SamirMoammer](https://github.com/SamirMoammer)
- **Mercedes Pérez** - 1054334 | GitHub: [Mercedesperezy](https://github.com/Mercedesperezy)
- **Rolbik Urbáez** - 1105721 | GitHub: [Wolbik](https://github.com/Wolbik)
- **Francisco Paulino** -  1106084 | GitHub: [Crosslands](https://github.com/Crosslands)
