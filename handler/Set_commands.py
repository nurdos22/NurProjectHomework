from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command="/start", description="Запуск бота"),
        types.BotCommand(command="/random", description="Случайное имя"),
        types.BotCommand(command="/pic", description="Картинка"),
        types.BotCommand(command="/myinfo", description="Информация про вас"),
        types.BotCommand(command="/review", description="Оставить отзыв"),
    ]
    await bot.set_my_commands(commands)


async def set_starting_commands(message: Message):
    await message.answer("hahaha")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(set_starting_commands, commands=['start'])


async def on_start(bot: Bot, dp: Dispatcher):
    await set_commands(bot)

    register_handlers(dp)

