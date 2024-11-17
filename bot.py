import os
from asyncio import run
from aiogram import Bot, Dispatcher
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from dotenv import load_dotenv

from functions import (info, yordam, vacancy, age, technology, phone,
                       country, cost, profession, time_to_apply, name, the_goal)
from statelar import Vacancy

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def echo(message: Message):
    await message.copy_to(chat_id=message.from_user.id)


async def start(message: Message, bot: Bot):
    await message.answer("<b>Xush Kelibsiz bizning Botimizga!!!</b>\n/help Yordam", parse_mode="HTML")
    await running(bot)


async def running(bot: Bot):
    await bot.send_message(chat_id=os.getenv("USER_ID"), text="Bot Ishga tushdi ✅")


async def stop(bot: Bot):
    await bot.send_message(chat_id=os.getenv("USER_ID"), text="Bot To'xtadi ⚠️")


async def set_commands(bot):
    await bot.set_my_commands([
        BotCommand(command='start', description="botni ishga tushurish "),
        BotCommand(command="info", description="foydalanuvchi ma'lumotlarini olish"),
        BotCommand(command='help', description="""Yordam """),
        BotCommand(command='vacancy', description="E'lon berish")
    ])


async def main():
    await set_commands(bot)

    # Register command handlers
    dp.message.register(start, Command('start'))  # Handle /start command
    dp.message.register(info, Command('info'))
    dp.message.register(yordam, Command('help'))
    dp.message.register(vacancy, Command('vacancy'))
    dp.message.register(name, Vacancy.name)
    dp.message.register(age, Vacancy.age)
    dp.message.register(technology, Vacancy.technology)
    dp.message.register(phone, Vacancy.phone)
    dp.message.register(country, Vacancy.country)
    dp.message.register(cost, Vacancy.cost)
    dp.message.register(profession, Vacancy.profession)
    dp.message.register(time_to_apply, Vacancy.time_to_apply)
    dp.message.register(the_goal, Vacancy.The_goal)
    dp.message.register(echo)

    # Start the bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())
