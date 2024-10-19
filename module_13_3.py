import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализируем бот и диспетчер
bot = Bot(token="")
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

# Хэндлер на все остальные сообщения
@dp.message()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

# Главная функция
async def main():
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())