from fastapi import APIRouter
from fastapi.responses import Response
from src.database import models
from src import schemas
from typing import List

router = APIRouter(prefix='/api/v1/adverts', tags=['Товары'])

@router.get('/all')
async def get_adverts() -> List[models.Advert]:
    return await models.Advert.objects.select_related(['user', 'category', 'dormitory']).all()


@router.get('/advert/{id}')
async def get_advert(id: int) -> models.Advert:
    return await models.Advert.objects.filter(id=id).select_related(['user', 'category', 'dormitory']).first()


@router.post('/create')
async def create_advert(advert: schemas.Advert) -> models.Advert:
   	return await models.Advert.objects.create(
        name=advert.name,
        image_path=advert.image_path,
        description=advert.description,
        price=advert.price,
        user=advert.user,
        dormitory=advert.dormitory,
        category=advert.category
    )


@router.get('/')
async def get_adverts_by_category_by_dormitory(category: int, dormitory: int) -> List[models.Advert]:
    return await models.Advert.objects.filter(category=category, dormitory=dormitory).all()
     