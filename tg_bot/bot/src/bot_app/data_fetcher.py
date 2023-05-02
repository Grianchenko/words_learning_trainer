import aiohttp
from . local_settings import WORDS_API_URL, LESSONS_API_URL, NEW_WORD_API_URL, NEW_LESSON_API_URL


async def get(api):
    async with aiohttp.ClientSession() as session:
        async with session.get(api) as response:
            return await response.json()


async def post(api, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url=api,
                                data=data) \
                as response:
            return await response.json()


async def get_random():
    return await get(WORDS_API_URL)


async def get_lessons():
    return await get(LESSONS_API_URL)


async def post_new_word(data: dict):
    return await post(NEW_WORD_API_URL, data)


async def post_new_lesson(data: dict):
    return await post(NEW_LESSON_API_URL, data)
