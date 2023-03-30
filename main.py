from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


bot = Bot("enter your telegram bot token here")
dp = Dispatcher(bot)

# write a simple function
# where will be the answer to the start and by pressing the button your site will open


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton(
        'Open web-page', web_app=WebAppInfo(url="in the url you can simply write the link of your site")))  #
    await message.answer('Hi, my friend!', reply_markup=markup)

executor.start_polling(dp)
