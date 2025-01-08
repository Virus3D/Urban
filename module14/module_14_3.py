# для решения использован
# python 3.12
# aiogram-3.17

from aiogram import Bot, Dispatcher, F, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, KeyboardButton
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

kb = ReplyKeyboardBuilder()
kb.button(text='Рассчитать')
kb.button(text='Информация')
kb.button(text='Купить')

kbi = InlineKeyboardBuilder()
kbi.button(text='Рассчитать норму калорий', callback_data='calories')
kbi.button(text='Формулы расчёта', callback_data='formulas')

kbi_buy = InlineKeyboardBuilder()
for i in range(1, 5):
    kbi_buy.button(text=f'Product{i}', callback_data='product_buying')


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb.as_markup(resize_keyboard=True))

@dp.message(F.text.casefold() == "информация")
async def set_age(message: types.Message, state: FSMContext):
    await message.answer('Я бот помогающий твоему здоровью.')

@dp.message(F.text.casefold() == "рассчитать")
async def main_menu(message: types.Message, state: FSMContext):
    await message.answer('Выберите опцию:', reply_markup=kbi.as_markup(resize_keyboard=True))

@dp.message(F.text.casefold() == "купить")
async def get_buying_list(message: types.Message, state: FSMContext):
    for i in range(1, 5):
        img = types.FSInputFile(f'img/Product{i}.jpeg')
        await message.answer_photo(img, caption=f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')

    await message.answer('Выберите продукт для покупки:', reply_markup=kbi_buy.as_markup(resize_keyboard=True))

@dp.callback_query(F.data.casefold() == "formulas")
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.callback_query(F.data.casefold() == "calories")
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)
    # await call.answer()

@dp.callback_query(F.data.casefold() == "product_buying")
async def send_confirm_message(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)

@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    growth = message.text
    await state.update_data(growth=growth)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)

@dp.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    weight = message.text
    await state.update_data(weight=weight)  # Сохраняем вес

    # Получаем данные
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
    await state.clear()  # Завершаем состояние

@dp.message()
async def all_massages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    import asyncio
    asyncio.run(dp.start_polling(bot, skip_updates=True))
