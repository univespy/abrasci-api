from fastapi import FastAPI

from src.auth.router import fastapi_users
from src.users.schemas import UserCreate, UserRead, UserUpdate

from .security import auth_backend

app = FastAPI()
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix='/auth',
    tags=['auth'],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users'],
)


@app.get('/')
def read_root():
    return {'message': 'Hello, world!'}
