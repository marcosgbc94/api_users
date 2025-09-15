# Pasos para probar la API para desarrollo
 - Clonar repositorio: obtener todo el código fuente del proyecto.
 - Copiar archivo .env: incluir todas las variables de entorno necesarias.
 - Elegir base de datos: decidir si usar MySQL o PostgreSQL según `CURRENT_DATA_SOURCE`.
 - Tener Docker instalado: tanto Docker Engine como Docker Compose.
 - Construir contenedores: ejecutar `docker-compose build`.
 - Levantar servicios según base de datos correspondiente `docker-compose -f docker-compose.postgre.yml up -d` para Postgre o `docker-compose -f docker-compose.mysql.yml up -d` para MySQL.
 - Esperar que la DB esté lista: la API incluye un script que espera a que la base de datos responda antes de arrancar.
 - Verificar que el backend corra: asegurarse que FastAPI esté escuchando en el puerto configurado (ej. 8000).
 - Acceder a la API: mediante `localhost:8000` o la IP del host, según corresponda.
 - Usar rutas de prueba: probar endpoints con Postman, curl o navegador para confirmar que funciona.
 - Detener contenedores: al finalizar, usar docker-compose down para limpiar recursos.

# Definiciones de directorios
## Core
Maneja configuraciones del sistema y de seguridad usadas en toda la aplicación, como variables de entorno, claves secretas, y parámetros globales.

## Data
Capa de persistencia del sistema, encargada de almacenar y recuperar información de las fuentes de datos.

### Database
Contiene las fuentes de datos, la configuración y conexión a las bases de datos.

### Models
Definiciones de los modelos del sistema, que representan las tablas o estructuras de la base de datos.

### Mappers
Funciones o clases que transforman datos entre los modelos de la base de datos y los objetos del dominio de la aplicación, y viceversa.

### Repositories
Encapsula la lógica de acceso a datos. Proporciona métodos para consultar, crear, actualizar y eliminar registros sin que el resto de la aplicación conozca los detalles de la base de datos.

## Domain
Representa las entidades y reglas de negocio principales de tu aplicación. Aquí defines tus objetos del dominio y su comportamiento.

## Use Cases
Contiene la lógica de aplicación que coordina los repositorios y el dominio para cumplir casos de uso específicos. Cada use case representa una operación del sistema desde el punto de vista del negocio.

## Presentation
Capa encargada de la interacción con el usuario o cliente (API REST, frontend, etc.). Incluye:

### API / Routers / v1
Define los endpoints de la API, organiza rutas y expone los casos de uso. Aquí también puedes manejar autenticación, validación de datos y control de errores.

### Schemas
Define los esquemas de entrada y salida (por ejemplo, Pydantic en FastAPI) que se usan para validar y serializar datos entre la API y los use cases.