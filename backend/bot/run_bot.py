from aiogram import Bot, Dispatcher, Router     
from config import settings
import asyncio
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from handlers import rt

bot = Bot(settings.TOKEN)
dp = Dispatcher()


# async def on_startup(bot: Bot):
#     await bot.send_message(chat_id=settings.ADMIN_CHAT_ID, text="Бот запущен")

# async def on_shutdown(bot: Bot):
#     await bot.send_message(chat_id=settings.ADMIN_CHAT_ID, text="Бот выключен")

async def main():
    # dp.startup.register(on_startup)
    # dp.shutdown.register(on_shutdown)
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())