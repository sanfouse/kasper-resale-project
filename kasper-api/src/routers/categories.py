from fastapi import APIRouter
from fastapi.responses import Response
from src.database import models
from src import schemas

router = APIRouter(prefix='/api/v1/categories', tags=['Категории'])

@router.get('/')
async def get_categories():
    return await models.Category.objects.select_related('adverts').all()


@router.post('/create')
async def create_category(category: schemas.Category) -> models.Category:
   	return await models.Category.objects.create(
        name=category.name,
        url=category.url
    )