from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage= MemoryStorage())

# Задача "Цепочка вопросов":

class UserState(StatesGroup):
    # Внутри этого класса опишите 3 объекта класса State: age, growth, weight (возраст, рост, вес).
    age = State() # возраст
    growth = State() # рост
    weight = State() # вес

# Оберните её в message_handler, который реагирует на текстовое сообщение 'Calories'.
@dp.message_handler(text = 'Calories')
async def set_age(message):
    # Эта функция должна выводить в Telegram-бот сообщение 'Введите свой возраст:'.
    await message.answer('Введите свой возраст (полных лет):')

    # После ожидать ввода возраста в атрибут UserState.age при помощи метода set.
    await UserState.age.set()


# Оберните её в message_handler, который реагирует на переданное состояние UserState.age.
@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    # Эта функция должна обновлять данные в состоянии age на message.text (написанное пользователем сообщение).
    # Используйте метод update_data.
    await state.update_data(age = message.text)

    # Далее должна выводить в Telegram-бот сообщение 'Введите свой рост:'.
    await message.answer('Введите свой рост в см.:')

    # После ожидать ввода роста в атрибут UserState.growth при помощи метода set.
    await UserState.growth.set()


# Оберните её в message_handler, который реагирует на переданное состояние UserState.growth.
@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    # Эта функция должна обновлять данные в состоянии growth на message.text (написанное пользователем сообщение).
    # Используйте метод update_data.
    await state.update_data(growth = message.text)

    # Далее должна выводить в Telegram-бот сообщение 'Введите свой вес:'.
    await message.answer('Введите свой вес в кг.:')

    # После ожидать ввода роста в атрибут UserState.weight при помощи метода set.
    await UserState.weight.set()


# Оберните её в message_handler, который реагирует на переданное состояние UserState.weight.
@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    # Эта функция должна обновлять данные в состоянии weight на message.text (написанное пользователем сообщение).
    # Используйте метод update_data.
    await state.update_data(weight = message.text)

    # Далее в функции запомните в переменную data все ранее введённые состояния при помощи state.get_data().
    data = await state.get_data()

    # Используйте упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы калорий (для женщин или мужчин -
    # на ваше усмотрение).
    # Данные для формулы берите из ранее объявленной переменной data по ключам age, growth и weight соответственно.
    # Для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5.
    calories = int(round((10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5), 0))

    # Результат вычисления по формуле отправьте ответом пользователю в Telegram-бот.
    await message.answer(f'Ваша норма: {calories} калорий.')

    # Финишируйте машину состояний методом finish().
    await state.finish()


@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Введите "Calories" (без кавычек) для подсчёта нормы калорий по упрощённой '
                         'формуле Миффлина - Сан Жеора для мужчин.')


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы запустить расчёт.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)