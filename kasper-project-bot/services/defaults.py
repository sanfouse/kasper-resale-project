from aiogram.fsm.context import FSMContext


async def default_state_update_data(
        state: FSMContext, university: int = 0, dormitory: int = 0, category: int = 0
    ) -> None:
    await state.update_data(
        university=university,
        dormitory=dormitory,
        category=category
    )