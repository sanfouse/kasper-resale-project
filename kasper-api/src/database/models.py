import datetime
from typing import List, Optional

import ormar
import sqlalchemy
from src.database.connection import database

metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = ormar.BigInteger(primary_key=True)
    username: str = ormar.String(max_length=255)

    vk_url: str = ormar.String(max_length=255, default=None, nullable=True)


class University(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'universities'

    id: int = ormar.BigInteger(primary_key=True)
    name: str = ormar.String(max_length=255)


class Dormitory(ormar.Model):
    class Meta(BaseMeta):
        tablename = "dormitories"

    id: int = ormar.BigInteger(primary_key=True)
    name: str = ormar.String(max_length=255)

    university: University = ormar.ForeignKey(University)


class Category(ormar.Model):
    class Meta(BaseMeta):
        tablename = "categories"

    id: int = ormar.BigInteger(primary_key=True)
    name: str = ormar.String(max_length=255)

    url: str = ormar.String(max_length=255)


class Advert(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'adverts'

    id: int = ormar.BigInteger(primary_key=True)
    name: str = ormar.String(max_length=255)

    image_path: str = ormar.String(max_length=1000, default=None)
    description: str = ormar.String(max_length=2000, default=None)
    price: str = ormar.Decimal(max_digits=12, decimal_places=2, default=0)
    date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)

    user: User = ormar.ForeignKey(User)
    dormitory: Dormitory = ormar.ForeignKey(Dormitory)
    category: Category = ormar.ForeignKey(Category)