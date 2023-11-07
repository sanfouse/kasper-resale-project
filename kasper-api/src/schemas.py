import datetime
from decimal import Decimal

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    vk_url: str

