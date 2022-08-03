import logging

import wikipedia
from aiogram import Bot, Dispatcher, executor, types
wikipedia.set_lang('uz')

API_TOKEN = '5487420195:AAEQgV6-CE-vTdhfalZDsumR8N7gz_V-9fw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalamu alaykum!\n Wikipedia botiga xush kelibsiz")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply('Sizga qanday yordam berishimiz mumkin')

@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)