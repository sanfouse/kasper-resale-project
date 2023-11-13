from aiogram import types
from aiogram.filters import StateFilter
from aiogram import Router
from states.default import Default
from aiogram.fsm.context import FSMContext
from keyboards.user import inline
from services.adverts import get_adverts


menu = Router()

async def view_advert(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    page: int = data.get('page')

    adverts, total_adverts = await get_adverts(
            category=data.get('category'), 
            dormitory=data.get('dormitory'),
            page=page + 1
        )
    builder = await inline.view_adverts_keyboard()
    if page == total_adverts - 1:
        builder._markup.pop(0)
    await call.message.answer_photo(
        caption=f"{adverts[0]['name']}\n{adverts[0]['price']}\n",
        reply_markup=builder.as_markup(),
        photo='https://i.pinimg.com/originals/f4/ea/93/f4ea935789d37ac9d025f29ecee00aa6.jpg'
    )
    return await state.update_data(page=page + 1, adverts=adverts[0])



@menu.callback_query(StateFilter(Default.settings), inline.ViewAdvertsStart.filter())
async def view_adverts_settings(call: types.CallbackQuery, callback_data: inline.ViewAdvertsStart, state: FSMContext):
    if callback_data.action == inline.ActionStart.start:
        await state.set_state(Default.view)
        return await view_advert(call=call, state=state)
    await call.message.answer("cancel /start for restart")
    return await state.clear()


@menu.callback_query(StateFilter(Default.view), inline.ViewAdverts.filter())
async def view_adverts_settings(call: types.CallbackQuery, callback_data: inline.ViewAdverts, state: FSMContext):
    if callback_data.action == inline.ActionAdvert.cancel:
        await call.message.answer("cancel /start for restart")
        return await state.clear()
    return await view_advert(call=call, state=state)