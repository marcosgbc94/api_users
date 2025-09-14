from fastapi import FastAPI
from src.presentation.api.routers.v1 import user_router

app = FastAPI()

#app.include_router(json_auth_router.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(user_router.router, prefix="/api/v1", tags=["users"])
