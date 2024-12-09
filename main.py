import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

from config import API_KEY
from keyboards import *
import texts


logging.basicConfig(level=logging.INFO)
bot = Bot(API_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(texts.start, reply_markup=start_keyboard)

@dp.message_handler(text='О нас')
async def info(message):
    await message.answer(texts.about, reply_markup=start_keyboard)

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

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
