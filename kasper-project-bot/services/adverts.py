import requests
from data.config import SERVER_URL


async def get_adverts(category: int, dormitory: int) -> list:
    return requests.get(
        url=f"{SERVER_URL}adverts/?category={category}&dormitory={dormitory}"
    ).json()