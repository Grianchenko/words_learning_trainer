from aiogram.dispatcher.filters.state import State, StatesGroup


class MyState(StatesGroup):
    start = State()
    train = State()
    word_inp = State()
    lesson_inp = State()
