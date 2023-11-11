import requests
from data.config import SERVER_URL
from aiogram import types

async def get_or_create_user(message: types.Message):
    return requests.post(
            f'{SERVER_URL}users/create',
            json={
                'id': message.from_user.id,
                'username': message.from_user.username
            }
        )