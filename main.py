from aiogram import Bot,Dispatcher,executor,types

bot = Bot('6517120796:AAGdHb6G7bUZ68RUc0r97C3aUjiCClA0Naw')
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def main(msg:types.Message):
    await msg.answer('Hello')

@dp.message_handler()
async def main(msg:types.Message):
    await msg.answer(msg.text)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)