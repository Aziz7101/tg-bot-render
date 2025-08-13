from aiogram import Bot, Dispatcher
import asyncio
import os

# Токен бота из переменной окружения (Render -> Environment)
TOKEN = os.getenv("BOT_TOKEN")

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    @dp.message()
    async def echo(message):
        await message.answer(message.text)

    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
