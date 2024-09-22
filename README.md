# FastAPI Task API

## Descripción

FastAPI Task Manager es una API RESTful diseñada para facilitar la gestión de tareas. Desarrollada con **FastAPI**, esta aplicación permite a los usuarios crear, leer, actualizar y eliminar tareas de manera eficiente. Además, registra automáticamente información sobre la IP del cliente, su ubicación y las condiciones climáticas, ofreciendo un contexto útil para cada solicitud.

## Tecnologías

Este proyecto utiliza las siguientes tecnologías:

- **FastAPI**: Un framework moderno y rápido para construir APIs con Python, que se basa en estándares como OpenAPI y JSON Schema, lo que permite una documentación automática y una validación de datos robusta.
- **SQLAlchemy**: ORM (Object Relational Mapping) para Python que simplifica la interacción con bases de datos relacionales, permitiendo realizar operaciones de base de datos de manera intuitiva.
- **PostgreSQL**: Un sistema de gestión de bases de datos relacional que se utiliza para almacenar datos de tareas y registros de solicitudes.
- **Pydantic**: Biblioteca para la validación de datos y la creación de modelos de datos mediante el uso de anotaciones de tipo.
- **JSON Web Tokens (JWT)**: Utilizados para la autenticación segura de los usuarios, garantizando que solo aquellos con un token válido puedan acceder a ciertas rutas.
- **Docker**: Herramienta para contenerizar la aplicación, facilitando su despliegue y asegurando que funcione de manera consistente en diferentes entornos.
- **Requests**: Biblioteca para realizar llamadas HTTP a APIs externas, utilizada para obtener la IP del cliente, su ubicación geográfica y el clima actual.

## Funcionalidades

### Gestión de Tareas

- **Crear Tarea**: Permite a los usuarios crear nuevas tareas proporcionando un nombre y una descripción.
- **Leer Tareas**: Los usuarios pueden obtener una lista de todas las tareas o detalles específicos de una tarea por su ID.
- **Actualizar Tarea**: Posibilita la actualización de una tarea existente, incluyendo cambios en el nombre, descripción y estado (pendiente/completada).
- **Eliminar Tarea**: Permite a los usuarios eliminar tareas que ya no sean necesarias.

### Registro de Solicitudes

- La API registra automáticamente información sobre la IP del cliente, el país asociado a esa IP y el clima en el momento de la solicitud. Esta información se almacena en la base de datos, permitiendo el análisis y seguimiento de las interacciones con la API.

### Autenticación

- Todas las rutas de la API que requieren autenticación utilizan JWT. Los usuarios deben iniciar sesión para recibir un token que les permita acceder a las funcionalidades protegidas.

## Estructura del Proyecto

fastapi-tasks-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── crud.py
│   ├── database.py
│   ├── schemas.py
│   ├── auth.py
│   ├── utils.py
├── alembic/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── .env
├── README.md



## Instalación y Uso

1. **Clonar el Repositorio**:
   Clona el repositorio en tu máquina local.
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-repositorio>

2. **Crear un Archivo .env: Crea un archivo .env en la raíz del proyecto y define las siguientes variables**:

SECRET_KEY=<tu_clave_secreta>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=postgresql://postgres:password@db/tasks_db
WEATHER_API_KEY=<tu_api_key>

3. **Construir y Ejecutar el Contenedor: Utiliza Docker Compose para construir y ejecutar el contenedor**:

docker-compose up --build

4. **Acceder a la API: La API estará disponible en http://localhost:9000. Puedes probar las funcionalidades utilizando herramientas como Postman o cURL.**

5. **Documentación Interactiva: FastAPI genera automáticamente documentación interactiva. Puedes acceder a ella en http://localhost:9000/docs.**

## Ejemplo de Uso

1. **Crear una Nueva Tarea**

Para crear una tarea, realiza una solicitud POST a /tasks con el siguiente cuerpo:

{
    "task_name": "My New Task",
    "description": "This is a description of the task."
}


2. **Obtener Todas las Tareas**

Para obtener todas las tareas, realiza una solicitud GET a /tasks.

3. **Actualizar una Tarea**

Para actualizar una tarea, realiza una solicitud PUT a /tasks/{task_id} con el siguiente cuerpo:

{
    "task_name": "Updated Task Name",
    "description": "Updated description.",
    "status": "completed"
}

4. **Eliminar una Tarea**

Para eliminar una tarea, realiza una solicitud DELETE a /tasks/{task_id}.