# для решения использован
# python 3.12
# aiogram-3.17

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Получаем токен API Telegram
api = os.getenv('TELEGRAM_API_TOKEN')
bot = Bot(token=api)

# Создаем хранилище и инициализируем диспетчер
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message()
async def start(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    import asyncio
    asyncio.run(dp.start_polling(bot, skip_updates=True))
