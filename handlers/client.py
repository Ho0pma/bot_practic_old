from create_bot import dp, bot
from aiogram import types, Dispatcher
import db


async def command_start(message: types.Message):
    await bot.send_message(message.chat.id, 'hello!')


async def command_select_users(message: types.Message):
    users_list = await db.select_users()
    await bot.send_message(message.chat.id, 'users: ' + str(users_list))


def register_handlers_client(message: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_select_users, commands=['users'])
