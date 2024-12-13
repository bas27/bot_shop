from keyboards import *
from texts import texts


async def price(message):
    await message.answer('Что вас интересует?', reply_markup=catalog_keyboard)


async def buy_m(call):
    await call.message.answer(texts.Mgame, reply_markup=buy_keyboard)
    await call.answer()


async def buy_b(call):
    await call.message.answer(texts.Lgame, reply_markup=buy_keyboard)
    await call.answer()


async def buy_xl(call):
    await call.message.answer(texts.XLgame, reply_markup=buy_keyboard)
    await call.answer()


async def buy_other(call):
    await call.message.answer(texts.other)
    await call.answer()


async def back(call):
    await call.message.answer('Что вас интересует?', reply_markup=catalog_keyboard)
    await call.answer()
