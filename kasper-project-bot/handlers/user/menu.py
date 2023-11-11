from aiogram import types
from aiogram.filters import StateFilter
from aiogram import Router
from states.default import Default
from aiogram.fsm.context import FSMContext
from keyboards.user import inline


menu = Router()

@menu.callback_query(StateFilter(Default), inline.CategoryCallback.filter())
async def accept_settings(
        call: types.CallbackQuery, 
        callback_data: inline.CategoryCallback, 
        state: FSMContext
    ) -> None:
    await state.update_data(
        category=callback_data.id
    )
    await call.message.edit_text(
        f"Вы выбрали {callback_data.name}\nСмотрите товары:",
    )
    print(await state.get_data())