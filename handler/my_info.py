from aiogram import  Dispatcher, types
from aiogram.types import Message


async def info_handler(message):
    user = message.from_user
    await message.answer(f'Your id: {message.from_user.id}\n'
                         f' Your First name: {message.from_user.first_name}\n'
                         f'Your username: {message.from_user.username} ')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(info_handler, commands=['myinfo'])
