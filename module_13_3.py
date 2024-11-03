import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(token="")
dp = Dispatcher()

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())