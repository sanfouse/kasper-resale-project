import asyncio
from aiogram import Bot, Dispatcher
from handlers import user, admin
from data.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_routers(admin.admin_router, user.user_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())