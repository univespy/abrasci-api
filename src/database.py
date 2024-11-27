from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .settings import settings

engine = create_async_engine(settings.DATABASE_URL)


class Base(DeclarativeBase):
    pass


async def get_session():
    async with AsyncSession(engine) as session:
        yield session


Session = Annotated[AsyncSession, Depends(get_session)]
