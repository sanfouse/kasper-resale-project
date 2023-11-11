import requests
from data.config import SERVER_URL


async def get_dormitory_by_university(id: int) -> list:
    return requests.get(
        url=f'{SERVER_URL}dormitories/?id={id}'
    ).json()