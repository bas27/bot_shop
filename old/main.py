import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from secret import API_KEY
from keyboards import *
from texts import texts

logging.basicConfig(level=logging.INFO)
bot = Bot(API_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Добро пожаловать, {message.from_user.full_name}! ' + texts.start, reply_markup=start_keyboard)

@dp.message_handler(text='О нас')
async def info(message):
    with open('../files/2.jpg', 'rb') as f:
        await message.answer_photo(f, caption=texts.about, reply_markup=start_keyboard)

@dp.message_handler(text='Стоимость')
async def price(message):
    await message.answer('Что вас интересует?', reply_markup=catalog_keyboard)


@dp.callback_query_handler(text='medium')
async def buy_m(call):
    await call.message.answer(texts.Mgame, reply_markup=buy_keyboard)
    await call.answer()

@dp.callback_query_handler(text='big')
async def buy_b(call):
    await call.message.answer(texts.Lgame, reply_markup=buy_keyboard)
    await call.answer()

@dp.callback_query_handler(text='mega')
async def buy_xl(call):
    await call.message.answer(texts.XLgame, reply_markup=buy_keyboard)
    await call.answer()

@dp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(texts.other)
    await call.answer()


@dp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer('Что вас интересует?', reply_markup=catalog_keyboard)
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
