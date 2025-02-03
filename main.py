import asyncio
import random

from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher(bot)

random_user = ['Artur', 'Amir', 'Janat', 'Kairat']

@dp.message_handler(commands =['start'])
async def start_handler(message):
    user = message.from_user
    await message.answer(f'hello, {user.first_name}')

@dp.message_handler(commands =['myinfo'])
async def info_handler(message):
    user = message.from_user
    await message.answer(f'Your id: {message.from_user.id}\n'
                         f' Your First name: {message.from_user.first_name}\n'
                         f'Your username: {message.from_user.username} ')



@dp.message_handler(commands =['random'])
async def random_handler(message):
    random_name = random.choice(random_user)
    await message.answer(f" Случайное имя: {random_name}")


async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())