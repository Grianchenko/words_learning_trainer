from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def kb(buttons=None):
    button_train = KeyboardButton('/train')
    button_lessons = KeyboardButton('/lessons')
    button_new_word = KeyboardButton('/new_word')
    button_new_lesson = KeyboardButton('/new_lesson')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.row(button_train, button_new_word)
    keyboard.row(button_lessons, button_new_lesson)
    return keyboard


def inline_kb(buttons):
    keyboard = InlineKeyboardMarkup()
    for button in buttons:
        keyboard.add(InlineKeyboardButton(button, callback_data=button))
    return keyboard
