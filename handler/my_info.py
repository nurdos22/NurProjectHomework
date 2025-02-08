from aiogram import  Dispatcher, types
from aiogram.types import Message


async def info_handler(message: Message):
    user = message.from_user
    user_id = message.from_user.id
    username = message.from_user.username if message.from_user.username else 'no'
    await message.answer(f'Hello{user.first_name}!'
                        f'Your id: {user_id}\n'
                         f' Your First name: {message.from_user.first_name}\n'
                         f'Your username: {username} ')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(info_handler, commands=['myinfo'])



