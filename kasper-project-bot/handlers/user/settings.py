from aiogram import types
from aiogram.filters import CommandStart, StateFilter
from aiogram.utils.markdown import hbold
from aiogram import Router
from states.default import Default
from aiogram.fsm.context import FSMContext
from keyboards.user import inline
from services.users import get_or_create_user
from services.defaults import default_state_update_data
from services.adverts import get_adverts


settings = Router()


@settings.message(StateFilter(None), CommandStart())
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
    

@settings.callback_query(StateFilter(Default.settings), inline.UniversityCallback.filter())
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


@settings.callback_query(StateFilter(Default.settings), inline.DormitoryCallback.filter())
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


@settings.callback_query(StateFilter(Default.settings), inline.CategoryCallback.filter())
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
    data = await state.get_data()
    adverts, total_adverts = await get_adverts(
            category=data.get('category'), 
            dormitory=data.get('dormitory'),
            page=1
        )
    await state.update_data(
        adverts=adverts[0],
        total_adverts=total_adverts,
        page=0
    )
    builder = await inline.view_adverts_start_keyboard()
    if total_adverts == 0:
        builder._markup.pop(0)
    await call.message.answer(
        text=f'Найдено {total_adverts} товаров',
        reply_markup=builder.as_markup()
    )


@settings.callback_query(StateFilter(Default.settings), inline.Cancel.filter())
async def cancel(
        call: types.CallbackQuery, 
        state: FSMContext
    ) -> None:
    await state.clear()
    await call.message.answer(
        text='cancel /start for restart'
    )