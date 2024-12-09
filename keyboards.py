from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Стоимость'),
            KeyboardButton(text='О нас'),
        ]
    ], resize_keyboard=True
)

catalog_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Средняя Игра', callback_data='medium')],
        [InlineKeyboardButton(text='Большая Игра', callback_data='big')],
        [InlineKeyboardButton(text='Очень большая игра', callback_data='mega')],
        [InlineKeyboardButton(text='Другие предложения', callback_data='other')]
    ]
)
buy_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить', url='https://mail.ru')],
    ]
)
