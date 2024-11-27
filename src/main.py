from fastapi import FastAPI

from src.users.router import fastapi_users
from src.users.schemas import UserCreate, UserRead

app = FastAPI()
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)


@app.get('/')
def read_root():
    return {'message': 'Hello, world!'}
