import requests
from data.config import SERVER_URL


async def get_adverts(page: int, category: int, dormitory: int) -> tuple:
    responce = requests.get(
        url=f"{SERVER_URL}adverts/paginate?category={category}&dormitory={dormitory}&page={page}&page_size=1"
    ).json()
    return responce['adverts'], responce['total_adverts']