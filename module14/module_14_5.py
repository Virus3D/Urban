# для решения использован
# python 3.12
# aiogram-3.17

from crud_functions import *
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
initiate_db()
all_products = get_all_products()

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
kb.button(text='Регистрация')

kbi = InlineKeyboardBuilder()
kbi.button(text='Рассчитать норму калорий', callback_data='calories')
kbi.button(text='Формулы расчёта', callback_data='formulas')

kbi_buy = InlineKeyboardBuilder()
for product in all_products:
    kbi_buy.button(text=product['title'], callback_data='product_buying')


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

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
    for product in get_all_products():
        caption=f'Название: {product['title']} | Описание: описание {product['description']} | Цена: {product['price']}'
        img_path = f'img/Product{product['id']}.jpeg'
        if os.path.exists(img_path):
            img = types.FSInputFile(img_path)
            await message.answer_photo(img, caption=caption)
        else:
            await message.answer(caption)

    await message.answer('Выберите продукт для покупки:', reply_markup=kbi_buy.as_markup(resize_keyboard=True))


@dp.message(F.text.casefold() == "регистрация")
async def sing_up(message: types.Message, state: FSMContext):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await state.set_state(RegistrationState.username)


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

@dp.message(RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer('Пользователь существует, введите другое имя')
        return
        
    await state.update_data(username=username)
    await message.answer('Введите свой email:')
    await state.set_state(RegistrationState.email)

@dp.message(RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer('Введите свой возраст:')
    await state.set_state(RegistrationState.age)

@dp.message(RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)
    # Получаем данные
    data = await state.get_data()
    username = data['username']
    email = data['email']
    age = int(data['age'])
    add_user(username, email, age)

    await message.answer("Вы успешно зарегистрировались")
    await state.clear()  # Завершаем состояние

@dp.message()
async def all_massages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    import asyncio
    asyncio.run(dp.start_polling(bot, skip_updates=True))
