from random import shuffle
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hbold, hlink, hitalic, hspoiler, hunderline

from . app import dp, bot
from . import messages
from . keyboards import kb, inline_kb
from . states import MyState
from . data_fetcher import get_random, get_lessons, post_new_word, post_new_lesson


@dp.message_handler(commands=['start', 'help', 'exit'], state='*')
async def send_welcome(message: types.Message):
    await MyState.start.set()
    await message.answer(messages.WELCOME_MESSAGE, reply_markup=kb())


@dp.message_handler(commands=['train'], state='*')
async def train(message: types.Message, state: FSMContext):
    await MyState.train.set()
    buttons = []
    res = await get_random()
    async with state.proxy() as data:
        data['step'] = 1
        data['answer'] = res.get('translation')
        data['word'] = res.get('word')
        buttons.append(res.get('translation'))
    while len(buttons) < 3:
        new_res = await get_random()
        var = new_res.get('translation')
        if var not in buttons:
            buttons.append(var)
    shuffle(buttons)
    await message.answer(f"What is a {hbold(data['word'])}? "
                         f"Answer: {hspoiler(data['answer'])}",
                         reply_markup=inline_kb(buttons))


@dp.callback_query_handler(state=MyState.train)
async def answer_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    async with state.proxy() as data:
        if data['step'] % 5 == 0:
            data['step'] += 1
            await bot.send_message(callback_query.from_user.id,
                                   f"Do you want to stop?",
                                   reply_markup=inline_kb(['Yes', 'No']))
        elif answer == 'Yes':
            await MyState.start.set()
            await bot.send_message(callback_query.from_user.id,
                                   messages.WELCOME_MESSAGE, reply_markup=kb())
        elif answer == data.get('answer') or answer == 'No':
            buttons = []
            res = await get_random()
            data['step'] += 1
            data['answer'] = res.get('translation')
            data['word'] = res.get('word')
            buttons.append(res.get('translation'))
            while len(buttons) < 3:
                new_res = await get_random()
                var = new_res.get('translation')
                if var not in buttons:
                    buttons.append(var)
            shuffle(buttons)
            await bot.send_message(callback_query.from_user.id,
                                   f"Yes, let's go!\nWhat is a {hbold(data['word'])}? "
                                   f"Answer: {hspoiler(data['answer'])}",
                                   reply_markup=inline_kb(buttons))
        else:
            await callback_query.message.reply('Oh, no! Try again!')


@dp.message_handler(commands=['lessons'], state='*')
async def lessons(message: types.Message):
    res = await get_lessons()
    res = list(res)[-4:]
    lines = []
    for temp in res:
        line = f'It was a lesson on {hitalic(temp["date"])} on theme "{hbold(temp["theme"])}". You got mark' \
               f' {hunderline(temp["mark"])}, and you got "{hitalic(temp["homework"])}" for home.'
        lines.append(line)
    await message.answer(f'Look that were some lessons recently\n\n' + '\n'.join(lines) +
                         f'\n\nFor more info check {hlink("here", "http://127.0.0.1:8000/lessons/")}.',
                         reply_markup=kb())


@dp.message_handler(commands=['new_word'], state=MyState.start)
async def new_word(message: types.Message):
    await MyState.word_inp.set()
    await message.answer(messages.NEW_WORD_MESSAGE)


@dp.message_handler(state=MyState.word_inp)
async def get_new_word(message: types.Message):
    msg = message.text
    try:
        word, translation = msg.split(sep=' - ')
        data = {'word': word, 'translation': translation}
        await post_new_word(data)
        await message.answer('New word is added!', reply_markup=kb())
    except ValueError:
        await message.answer('Bad format, try again.')
    await MyState.start.set()


@dp.message_handler(commands=['new_lesson'], state=MyState.start)
async def new_lesson(message: types.Message):
    await MyState.lesson_inp.set()
    await message.answer(messages.NEW_LESSON_MESSAGE)


@dp.message_handler(state=MyState.lesson_inp)
async def get_new_lesson(message: types.Message):
    msg = message.text
    try:
        temp = msg.split(sep='\n')
        lesson = []
        for i in temp:
            if i == '':
                lesson.append(None)
            else:
                lesson.append(i)
        data = {'theme': lesson[0],
                'mark': lesson[1],
                'homework': lesson[2]}
        try:
            data['date'] = lesson[3]
        except IndexError:
            pass
        await post_new_lesson(data)
        await message.answer('Lesson info is added!', reply_markup=kb())
    except (ValueError, IndexError):
        await message.answer('Bad format, try again.')
    await MyState.start.set()
