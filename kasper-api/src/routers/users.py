from fastapi import APIRouter
from fastapi.responses import Response
from src.database import models
from src import schemas
from typing import List

router = APIRouter(prefix='/api/v1/users', tags=['Пользователи'])

@router.get('/')
async def get_users() -> List[models.User]:
    return await models.User.objects.all()


@router.get('/user/{id}')
async def get_user(id: int) -> models.User:
    return await models.User.objects.prefetch_related('adverts').get(id=id)


@router.post('/create')
async def create_user(user: schemas.User) -> models.User:
    return await models.User.objects.get_or_create(
        id=user.id,
        username=user.username, 
    )