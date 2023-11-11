import requests
from data.config import SERVER_URL

async def get_universities():
    return requests.get(
        url=f'{SERVER_URL}universities/'
    ).json()