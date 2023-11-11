import requests
from data.config import SERVER_URL


async def get_all_categories() -> list:
    return requests.get(
        url=f'{SERVER_URL}categories/'
    ).json()