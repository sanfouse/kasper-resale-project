from aiogram import types
from aiogram.filters import CommandStart, StateFilter
from aiogram.utils.markdown import hbold
from aiogram import Router
from states.default import Default
from aiogram.fsm.context import FSMContext
from keyboards.user import inline
from services.users import get_or_create_user
from services.defaults import default_state_update_data

start = Router()

@start.message(CommandStart())
async def start_message(message: types.Message, state: FSMContext) -> None:
    await get_or_create_user(message=message)
    await state.set_state(Default.settings)
    await default_state_update_data(
        state=state
    )
    builder=await inline.universities_choose_keyboard()
    await message.answer(
            f"Привет, {hbold(message.from_user.full_name)}!\nВыбери свой вуз: ",
            reply_markup=builder.as_markup()
        )
    

@start.callback_query(StateFilter(Default), inline.UniversityCallback.filter())
async def choose_dormitory(
        call: types.CallbackQuery, 
        callback_data: inline.UniversityCallback, 
        state: FSMContext
    ) -> None:
    await state.update_data(
        university=callback_data.id
    )
    builder = await inline.dormitories_choose_keyboard(id=callback_data.id)
    await call.message.edit_text(
        f"Вы выбрали {callback_data.name}\nВыберите общежитие:",
        reply_markup=builder.as_markup()
    )


@start.callback_query(StateFilter(Default), inline.DormitoryCallback.filter())
async def choose_category(
        call: types.CallbackQuery, 
        callback_data: inline.DormitoryCallback, 
        state: FSMContext
    ) -> None:
    await state.update_data(
        dormitory=callback_data.id
    )
    builder = await inline.categories_choose_keyboard()
    await call.message.edit_text(
        f"Вы выбрали {callback_data.name}\nВыберите категорию:",
        reply_markup=builder.as_markup()
    )
