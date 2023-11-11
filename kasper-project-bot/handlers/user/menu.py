from aiogram import types
from aiogram.filters import StateFilter
from aiogram import Router
from states.default import Default
from aiogram.fsm.context import FSMContext
from keyboards.user import inline

menu = Router()

async def view_advert(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    page: int = data.get('page')
    adverts: list = data.get('adverts')
    builder = await inline.view_adverts_keyboard()
    if page == len(adverts) - 1:
        builder._markup.pop(0)
    await call.message.answer(
        text=f"{adverts[page]['name']}\n{adverts[page]['price']}\n",
        reply_markup=builder.as_markup()
    )
    return await state.update_data(page=page + 1)



@menu.callback_query(StateFilter(Default.settings), inline.ViewAdvertsStart.filter())
async def view_adverts_settings(call: types.CallbackQuery, callback_data: inline.ViewAdvertsStart, state: FSMContext):
    if callback_data.action == inline.ActionStart.start:
        await state.set_state(Default.view)
        return await view_advert(call=call, state=state)
    else:
        await call.message.answer("cancel")
        await state.clear()


@menu.callback_query(StateFilter(Default.view), inline.ViewAdverts.filter())
async def view_adverts_settings(call: types.CallbackQuery, callback_data: inline.ViewAdverts, state: FSMContext):
    if callback_data.action == inline.ActionAdvert.cancel:
        await call.message.answer("cancel")
        return await state.clear()
    await view_advert(call=call, state=state)