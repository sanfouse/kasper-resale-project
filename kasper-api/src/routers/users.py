from fastapi import APIRouter
from fastapi.responses import Response
from src.database import models
from src import schemas
from asyncpg.exceptions import UniqueViolationError


router = APIRouter(prefix='/api/v1/users', tags=['Пользователи'])

@router.get('/')
async def get_users():
    return await models.User.objects.all()


@router.post('/create')
async def create_user(user: schemas.User) -> models.User:
    return await models.User.objects.get_or_create(
            id=user.id, 
            username=user.username, 
            vk_url=user.vk_url
        )