from keyboards import *
from texts import texts


async def start(message):
    await message.answer(f'Добро пожаловать, {message.from_user.full_name}! ' + texts.start,
                         reply_markup=start_keyboard)


async def info(message):
    with open('files/2.jpg', 'rb') as f:
        await message.answer_photo(f, caption=texts.about, reply_markup=start_keyboard)


async def show_help(message):
    await message.answer(texts.help_text, reply_markup=start_keyboard)
