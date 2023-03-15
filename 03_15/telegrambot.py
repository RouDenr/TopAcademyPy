import aiogram

TOKEN = 'Токен из @BotFather'

bot = aiogram.Bot(token=TOKEN)
disp = aiogram.Dispatcher(bot)

@disp.message_handler(commands=['start'])
async def startCmd(message : aiogram.types.Message) :
    # await bot.send_message(message.from_user.id, "Hello")
    await message.answer("Hello")

@disp.message_handler(commands=['say_my_name'])
async def sayMyName(message : aiogram.types.Message) :
    await message.reply(f"Your name {message.from_user.first_name}!!")

@disp.message_handler(content_types='text')
async def textHandler(message:aiogram.types.Message) :
    # await message.answer(message.text)
    await message.answer("I see")

if __name__ == '__main__':
    aiogram.executor.start_polling(disp, skip_updates=True)
