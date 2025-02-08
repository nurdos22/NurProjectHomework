from aiogram import  Dispatcher
from aiogram.types import Message


import random


random_user = ['Artur', 'Amir', 'Janat', 'Kaira']

async def random_handler(message: Message):
    random_name = random.choice(random_user)
    await message.answer(f" Случайное имя: {random_name}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(random_handler, commands=['random'])