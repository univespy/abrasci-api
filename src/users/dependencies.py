from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase

from src.database import Session
from src.users.models import User
from src.users.services import UserManager


async def get_user_db(session: Session):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
