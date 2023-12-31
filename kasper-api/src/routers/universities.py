from fastapi import APIRouter
from fastapi.responses import Response
from src.database import models
from src import schemas

router = APIRouter(prefix='/api/v1/universities', tags=['ВУЗы'])

@router.get('/')
async def get_universities():
  return await models.University.objects.all()


@router.post('/create')
async def create_university(university: schemas.University) -> models.University:
    return await models.University.objects.create(
            name=university.name
        )