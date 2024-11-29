import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from testcontainers.postgres import PostgresContainer

from src.database import Base, get_session
from src.main import app


@pytest_asyncio.fixture
async def client(session):
    async def get_session_override():
        yield session

    async with AsyncClient(app=app, base_url='http://0.0.0.0:8000') as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client


@pytest_asyncio.fixture(scope='session')
async def engine():
    with PostgresContainer(
        'postgis/postgis:latest', driver='psycopg'
    ) as postgres:
        _engine = create_async_engine(postgres.get_connection_url())

        async with _engine.begin():
            yield _engine


@pytest_asyncio.fixture
async def session(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSession(engine) as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
