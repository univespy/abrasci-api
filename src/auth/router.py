import uuid

from fastapi_users import FastAPIUsers

from src.security import auth_backend
from src.users.dependencies import get_user_manager
from src.users.models import User

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
