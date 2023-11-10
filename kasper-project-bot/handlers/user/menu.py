from aiogram import types
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from aiogram import Router


menu = Router()

# @menu.message(CommandStart())
# async def menu_message(message: types.Message) -> None:
#     await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")