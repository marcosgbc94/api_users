from fastapi import FastAPI
from src.presentation.errors import error_handler
from src.presentation.api.routers.v1 import user_router, auth_router

app = FastAPI()

#  Middleware global
app.middleware("http")(error_handler)

app.include_router(auth_router.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(user_router.router, prefix="/api/v1", tags=["users"])
