from aiogram.utils.markdown import hbold, hitalic

WELCOME_MESSAGE = '''
Hello! I can help you to memorize English words.
Also I can be a diary for you to save the info about your lessons.
Commands are:\n
/train\n
/lessons\n
/new_word\n
/new_lesson\n
'''

NEW_LESSON_MESSAGE = f'''
Input theme of the lesson, your mark and homework. Each of them should be written on new line. 
Each of them is required.
Example:
{hbold("Women rights")}
{hbold("20")}
{hbold("Learn new words")}
'''

NEW_WORD_MESSAGE = f'''
Input new word and translation like it is shown in example:
{hbold("mother - мать")}.
'''
