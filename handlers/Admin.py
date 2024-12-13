from keyboards import admin_panel


async def admin_func(message):
    await message.answer(text="Вы находитесь в панели администратора, выберите действие", reply_markup=admin_panel)


async def admin_users(message):
    print('admin_users')


async def admin_stat(message):
    print('admin_stat')


async def user_block(message):
    print('user_block')


async def user_unblock(message):
    print('user_unblock')


