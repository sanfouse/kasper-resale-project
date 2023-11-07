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

    vk_url: str = ormar.String(max_length=255, default=None)


class Advert(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'adverts'

    id: int = ormar.BigInteger(primary_key=True)
    name: str = ormar.String(max_length=255)

    image_path: str = ormar.String(max_length=1000, default=None)
    description: str = ormar.String(max_length=2000, default=None)
    price: str = ormar.Decimal(max_digits=12, decimal_places=2, default=0)
    date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)

    user: Optional[List[User]] = ormar.ManyToMany(User)


class Dormitory(ormar.Model):
    class Meta(BaseMeta):
        tablename = "dormitories"

    id: int = ormar.BigInteger(primary_key=True)
    name: str = ormar.String(max_length=255)

    adverts: Optional[List[Advert]] = ormar.ManyToMany(Advert)


class University(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'universities'

    id: int = ormar.BigInteger(primary_key=True)
    name: str = ormar.String(max_length=255)

    dormitories: Optional[List[Dormitory]] = ormar.ManyToMany(Dormitory)