from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import Message

from statelar import Vacancy


async def yordam(message: Message, bot: Bot, state: State):
    await  message.answer(text="""<b>/start botni ishga tushurish</b>
<b>/info foydalanuvchi ma'lumotlarini olish</b>
<b>/vacancy e'lon berish</b>""", parse_mode='HTML')


async def info(message: Message, bot: Bot, state: State):
    malumot = message.from_user
    xabar = message
    data = ""
    data += "Sizning ID Raqamingiz: " + str(malumot.id) + "\n"
    data += "Sizning Ismingiz: " + malumot.first_name + "\n"
    data += "is_bot:" + str(message.from_user.is_bot) + "\n"
    data += "language_code:" + str(message.from_user.language_code) + "\n"
    if malumot.username:
        data += f"Sizning usernameingiz: {malumot.username}\n"
    if malumot.last_name:
        data += f"Sizning Familiyangiz{malumot.last_name}\n"
    await message.answer(text=data, parse_mode='HTML')


async def vacancy(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Ism Sharifingizni kiriting!!!!")
    await state.set_state(Vacancy.name)


async def name(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Yoshingizni kiriting: ")
    await state.set_state(Vacancy.age)


async def age(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Technologiya kiriting Biladiganlaringiz Misol Python C#: ")
    await state.set_state(Vacancy.technology)


async def technology(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(technology=message.text)
    await message.answer("Telefon raqamingizni kiriting: ")
    await state.set_state(Vacancy.phone)


async def phone(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Hududni kiriting: ")
    await state.set_state(Vacancy.country)


async def country(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(country=message.text)
    await message.answer("Narxni  kiriting: ")
    await state.set_state(Vacancy.cost)


async def cost(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(cost=message.text)
    await message.answer("kasbingizni  kiriting: ")
    await state.set_state(Vacancy.profession)


async def profession(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(profession=message.text)
    await message.answer("Murojaat qilish vaqtini   kiriting: ")
    await state.set_state(Vacancy.time_to_apply)


async def time_to_apply(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(time_to_apply=message.text)
    await message.answer("Maqsadingizni kiriting:")
    await state.set_state(Vacancy.The_goal)


async def the_goal(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(The_goal=message.text)

    data = await state.get_data()
    name = data.get("name")
    age = data.get("age")
    technology = data.get("technology")
    phone = data.get("phone")
    country = data.get("country")
    cost = data.get("cost")
    profession = data.get("profession")
    time_to_apply = data.get("time_to_apply")
    the_goal = data.get("The_goal")
    formatted_data = f"""\n
        \t\t👨‍💼Ismingiz Sharifingiz: {name}\n
        🕑Yoshingiz: {age}\n
        📚Texnologiyalar: {technology}\n
        📞Telefon Raqam: {phone}\n
        🇺🇿Telegram: @{message.from_user.username}\n
        🌐Hudud: {country}\n
        💰Narx: {cost}\n
        👨🏻‍💻Kasbi: {profession}\n
        🕰 Murojaat qilish vaqti: {time_to_apply}\n
        🔎 Maqsadi: {the_goal}\n
        #{profession}
        """
    await message.answer(formatted_data)
