from aiogram import types
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from aiogram import Router
import requests
from data.config import SERVER_URL
from states.default import Default
from aiogram.fsm.context import FSMContext

start = Router()

@start.message(CommandStart())
async def start_message(message: types.Message, state: FSMContext) -> None:
    requests.post(
            f'{SERVER_URL}users/create',
            json={
                'id': message.from_user.id,
                'username': message.from_user.username
            }
        )
    await state.set_state(Default.settings)
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")