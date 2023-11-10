from fastapi import APIRouter
from fastapi.responses import Response
from src.database import models
from src import schemas

router = APIRouter(prefix='/api/v1/dormitories', tags=['Общежития'])

@router.get('/')
async def get_dormitories():
    return await models.Dormitory.objects.prefetch_related(['adverts', 'university']).all()


@router.post('/create')
async def create_dormitories(dormitories: schemas.Dormitory) -> models.Dormitory:
   	return await models.Dormitory.objects.create(
        name=dormitories.name,
        university=await models.University.objects.get(id=dormitories.university)
    )