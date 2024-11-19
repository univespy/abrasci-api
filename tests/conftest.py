import pytest_asyncio
from httpx import AsyncClient

from src.main import app


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(app=app, base_url='http://0.0.0.0:8000') as client:
        yield client
