import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import handlers.Start
import handlers.Category
import handlers.Admin
from secret import API_KEY

logging.basicConfig(level=logging.INFO)
bot = Bot(API_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.message_handler(commands=['start'])(handlers.Start.start)
dp.message_handler(text='О нас')(handlers.Start.info)
dp.message_handler(commands=['help'])(handlers.Start.show_help)

dp.message_handler(text='Стоимость')(handlers.Category.price)
dp.callback_query_handler(text='medium')(handlers.Category.buy_m)
dp.callback_query_handler(text='big')(handlers.Category.buy_b)
dp.callback_query_handler(text='mega')(handlers.Category.buy_xl)
dp.callback_query_handler(text='other')(handlers.Category.buy_other)
dp.callback_query_handler(text='back_to_catalog')(handlers.Category.back)

dp.message_handler(commands=['admin'])(handlers.Admin.admin_func)
dp.callback_query_handler(text='users')(handlers.Admin.admin_users)
dp.callback_query_handler(text='stat')(handlers.Admin.admin_stat)
dp.callback_query_handler(text='block')(handlers.Admin.user_block)
dp.callback_query_handler(text='unblock')(handlers.Admin.user_unblock)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
