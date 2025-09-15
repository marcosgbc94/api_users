from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import OperationalError, IntegrityError
import logging

logger = logging.getLogger(__name__)

async def error_handler(request: Request, call_next):
    try:
        return await call_next(request)

    except HTTPException as exc:
        # Errores controlados desde tus routers (raise HTTPException)
        if exc.status_code == 401:
            return JSONResponse(
                status_code=401,
                content={"detail": "No autorizado. Token inválido o expirado."}
            )
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

    except IntegrityError as exc:
        # Violación de constraints de DB (ej: unique constraint)
        logger.error(f"Error de integridad en DB: {exc}")
        return JSONResponse(
            status_code=409,
            content={"detail": "Conflicto en la base de datos (duplicado o restricción violada)"}
        )

    except OperationalError as exc:
        # Problemas de conexión a la base de datos
        logger.error(f"Error de conexión a DB: {exc}")
        return JSONResponse(
            status_code=503,
            content={"detail": "Servicio de base de datos no disponible"}
        )

    except ValueError as exc:
        # Errores de validación de reglas de negocio
        return JSONResponse(
            status_code=400,
            content={"detail": str(exc)}
        )

    except Exception as exc:
        # Cualquier otro error inesperado
        logger.exception("Error inesperado")
        return JSONResponse(
            status_code=500,
            content={"detail": "Error interno en el servidor"}
        )