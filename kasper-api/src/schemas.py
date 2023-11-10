import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel
from .database import models
from decimal import Decimal


class User(BaseModel):
    id: int
    username: str


class Advert(BaseModel):
    name: str

    image_path: str
    description: str
    price: Decimal

    user: int
    dormitory: int
    category: int


class Dormitory(BaseModel):
    name: str
    university: int


class Category(BaseModel):
    name: str
    url: str


class University(BaseModel):
    name: str
    