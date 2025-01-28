from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage= MemoryStorage())

# Задача "Меньше текста, больше кликов":

class UserState(StatesGroup):
    age = State() # возраст
    growth = State() # рост
    weight = State() # вес

# Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом:
# 'Рассчитать' и 'Информация'.
# Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи параметра resize_keyboard.
kb = ReplyKeyboardMarkup(resize_keyboard = True)
button_info = KeyboardButton(text = "Информация")
button_calc = KeyboardButton(text = "Рассчитать")
kb.add(button_info, button_calc)


# Измените massage_handler для функции  set_age.
# Теперь этот хэндлер будет реагировать на текст 'Рассчитать', а не на 'Calories'.
@dp.message_handler(text = 'Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст (полных лет):')
    await UserState.age.set()


@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост в см.:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес в кг.:')
    await UserState.weight.set()


@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    calories = int(round((10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5), 0))
    await message.answer(f'Ваша норма: {calories} калорий.')
    await state.finish()


@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

    # Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
    await message.answer('Нажмите на кнопку "Рассчитать" для подсчёта нормы калорий по упрощённой '
                         'формуле Миффлина - Сан Жеора для мужчин.', reply_markup = kb)


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы запустить расчёт.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)