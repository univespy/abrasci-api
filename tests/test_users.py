from http import HTTPStatus

import pytest
from httpx import AsyncClient

from src.users.schemas import UserCreate


@pytest.mark.asyncio
async def test_user_register(client: AsyncClient):
    user = UserCreate(
        full_name='String String', email='user@example.com', password='string'
    )

    response = await client.post('/auth/register', json=user.model_dump())

    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['email'] == 'user@example.com'
