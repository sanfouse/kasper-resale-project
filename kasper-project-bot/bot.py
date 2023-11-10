import asyncio
from aiogram import Bot, Dispatcher
from handlers import user
from data.config import BOT_TOKEN
from aiogram.enums.parse_mode import ParseMode

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

async def main():
    dp.include_routers(user.menu, user.start)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())