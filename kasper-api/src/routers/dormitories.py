from fastapi import APIRouter
from fastapi.responses import Response
from src.database import models
from src import schemas

router = APIRouter(prefix='/api/v1/dormitories', tags=['Общежития'])

@router.get('/')
async def get_dormitories():
  return await models.Dormitory.objects.all()