from aiogram import types
from database import models
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from aiogram import Router
from filters.is_chat_member import IsChatMember


user_router = Router()

@user_router.message(IsChatMember(), CommandStart())
async def start(message: types.Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")