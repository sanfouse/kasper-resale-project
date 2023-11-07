from fastapi import APIRouter
from fastapi.responses import Response
from src.database import models
from src import schemas

router = APIRouter(prefix='/api/v1/adverts', tags=['Товары'])

@router.get('/')
async def get_adverts():
  return await models.Advert.objects.all()