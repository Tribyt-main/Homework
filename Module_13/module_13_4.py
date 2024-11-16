from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    set_age = State()
    set_growth = State()
    set_weight = State()


@dp.message_handler(commands='start')
async def out_message(message):
    await message.answer('Для начала работы напишите "Calories"')


@dp.message_handler(text='Calories')
async def set_age(message):
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
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    calories_norm_for_man = 10 * age + 6.25 * growth + 5 * weight + 5
    await message.answer(f"Норма калорий {calories_norm_for_man}")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
