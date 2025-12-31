# API de Tareas (Prueba Técnica)

Hola, este es mi proyecto para la prueba de Backend. Es una API REST simple para manejar tareas, hecha con **FastAPI** y **PostgreSQL**.

## Cómo correrlo

Lo hice con Docker. Solo necesitas tener Docker instalado y correr este comando en la carpeta:

```bash
docker-compose up --build
```

Espera a que descargue todo.

## Cómo usarlo

Cuando termine de cargar, entra aquí para probar la API:
- **Link**: `http://localhost:8000/docs`

Ya creé un usuario para que puedas probar:
- **Usuario**: `admin`
- **Contraseña**: `secret`

Primero tienes que loguearte en el botón "Authorize" o en el endpoint `/auth/login` para que te deje usar las otras funciones de tareas.

## Qué tecnologías usé

- **FastAPI**: Es moderno y rápido para hacer APIs con Python.
- **PostgreSQL**: Es una base de datos relacional.
- **Docker**: Para no tener problemas de ejecución.
- **JWT**: Para la autenticación segura.
- **SQLAlchemy**: Para manejar la base de datos con código Python.

## Cosas que me faltaron (To Do)

No alcancé a hacer todo perfecto, pero esto es lo que mejoraría si tuviera más tiempo:

- [ ] Agregar Tests (apenas estoy aprendiendo Pytest).
- [ ] Mejorar la seguridad de las claves (ahora están en el archivo docker-compose).
- [ ] Hacer que se puedan crear más usuarios.

¡Gracias por la oportunidad!
