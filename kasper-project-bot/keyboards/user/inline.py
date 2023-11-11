from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.filters.callback_data import CallbackData
from services.universities import get_universities
from services.dormitory import get_dormitory_by_university
from services.categories import get_all_categories


class UniversityCallback(CallbackData, prefix="university"):
    id: int
    name: str


class DormitoryCallback(CallbackData, prefix="dormitory"):
    id: int
    name: str


class CategoryCallback(CallbackData, prefix="category"):
    id: int
    name: str


async def universities_choose_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    universities: list = await get_universities()
    for university in universities:
        builder.button(
            text=university['name'],
            callback_data=UniversityCallback(id=university['id'], name=university['name'])
        )
    builder.adjust(1)
    return builder


async def dormitories_choose_keyboard(id: int) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    dormitories: list = await get_dormitory_by_university(id=id)
    for dormitory in dormitories:
        builder.button(
            text=dormitory['name'],
            callback_data=DormitoryCallback(id=dormitory['id'], name=dormitory['name'])
        )
    builder.adjust(1)
    return builder


async def categories_choose_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    categories: list = await get_all_categories()
    for category in categories:
        builder.button(
            text=category['name'],
            callback_data=CategoryCallback(id=category['id'], name=category['name'])
        )
    builder.adjust(1)
    return builder