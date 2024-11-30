import uuid

from fastapi_users import schemas
from pydantic import BaseModel


class BaseUser(BaseModel):
    full_name: str


class UserRead(schemas.BaseUser[uuid.UUID], BaseUser):
    pass


class UserCreate(schemas.BaseUserCreate, BaseUser):
    pass


class UserUpdate(schemas.BaseUserUpdate, BaseUser):
    pass
