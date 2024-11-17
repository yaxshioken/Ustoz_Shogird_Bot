from aiogram.fsm.state import State, StatesGroup


class Vacancy(StatesGroup):
    name=State()
    age=State()
    technology=State()
    phone=State()
    country=State()
    cost=State()
    profession=State()
    time_to_apply=State()
    The_goal=State()
