from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from crud_functions import *

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
man = KeyboardButton(text='Мужчина')
woman = KeyboardButton(text='Женщина')
keyboard.add(man)
keyboard.add(woman)


inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
formula = InlineKeyboardButton(text='Формула расчёта', callback_data='formula')
start = InlineKeyboardButton(text='Рассчитать', callback_data='start')
buy = InlineKeyboardButton(text='Купить', callback_data='buy')
registration = InlineKeyboardButton(text='Регистрация', callback_data='reg')
inline_keyboard.add(formula)
inline_keyboard.add(start)
inline_keyboard.add(buy)
inline_keyboard.add(registration)
in_kb_product = InlineKeyboardMarkup(resize_keyboard=True)
product1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
product2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
product3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
product4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
in_kb_product.add(product1)
in_kb_product.add(product2)
in_kb_product.add(product3)
in_kb_product.add(product4)


class UserState(StatesGroup):
    set_age = State()
    set_growth = State()
    set_weight = State()
    man = State()
    woman = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

@dp.callback_query_handler(text='reg')
async def reg(call):
    await call.message.answer('Введите имя пользователя (только латинский алфавит): ')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def check_username(message, state):
    if is_included(username=message.text) == False:
        await state.update_data(username= message.text)
        await message.answer('Введите свой email: ')
        await RegistrationState.email.set()
    else:
        await message.answer('Такой пользователь уже существует, введите другое имя: ')
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def update_email(message, state):
    await state.update_data(email= message.text)
    await message.answer('Введите свой возраст: ')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def update_age(message, state):
    await state.update_data(age= message.text)
    data = await state.get_data()
    username = data['username']
    email = data['email']
    age = data['age']
    add_user(username, email, age)
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Рады вас видеть! \n1. Нажмите "Формула расчёта" для показа формулы.\n'
                         '2. Нажмите "Рассчитать" для начала работы.\n'
                         '3. Для выбора наших продуктов нажмите "Купить"', reply_markup=inline_keyboard)


@dp.callback_query_handler(text='formula')
async def formula(call):
    await call.message.answer('1. Для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n'
                              '2. Для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.callback_query_handler(text='start')
async def starter(call):
    await call.message.answer('Для начала работы выберите пол:', reply_markup=keyboard)
    await UserState.man.set()
    await UserState.woman.set()
    await call.answer()


@dp.callback_query_handler(text='buy')
async def buy(call):
    with open('img_file/protein.jpg', 'rb') as img1:
        await call.message.answer_photo(img1, product_1)
    with open('img_file/creatine.jpg', 'rb') as img2:
        await call.message.answer_photo(img2, product_2)
    with open('img_file/amino.jpg', 'rb') as img3:
        await call.message.answer_photo(img3, product_3)
    with open('img_file/bca.jpg', 'rb') as img4:
        await call.message.answer_photo(img4, product_4, reply_markup=in_kb_product)
    await call.answer()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(state=UserState.man)
async def set_age(message, state):
    await state.update_data(gender=message.text)
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Напишите свой возраст(только цифры):')
    await UserState.set_age.set()


@dp.message_handler(state=UserState.woman)
async def set_age(message, state):
    await state.update_data(gender=message.text)
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Напишите свой возраст(только цифры):')
    await UserState.set_age.set()


@dp.message_handler(state=UserState.set_age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост(только цифры):')
    await UserState.set_growth.set()


@dp.message_handler(state=UserState.set_growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес(только цифры):')
    await UserState.set_weight.set()


@dp.message_handler(state=UserState.set_weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    gender = data['gender']
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    if gender == 'Мужчина':
        calories_normal = 10 * age + 6.25 * growth + 5 * weight + 5
    else:
        calories_normal = 10 * age + 6.25 * growth + 5 * weight - 161
    await message.answer(f"Норма калорий {calories_normal}")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    print('Нам пришло сообщение')
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
