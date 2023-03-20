# import aiogram

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

TOKEN = 'Токен из @BotFather'

bot = Bot(token=TOKEN)
my_storage = MemoryStorage()
disp = Dispatcher(bot, storage=my_storage)

class MyStates(StatesGroup):
    readName = State()
    stable = State()

@disp.message_handler(commands=['start'])
async def startCmd(message : Message) :
    # await bot.send_message(message.from_user.id, "Hello")
    await message.answer("Привет! Как мне тебя называть?")
    await MyStates.readName.set()

@disp.message_handler(content_types='text', state=MyStates.readName)
async def readUserName(message : Message, state : FSMContext):
    name = message.text
    await message.answer(f"Еще раз привет {name}!")
    await state.update_data(username=name)
    await MyStates.stable.set()

@disp.message_handler(commands=['say_my_name'], state=MyStates.stable)
async def sayMyName(message : Message, state : FSMContext):
    user_data = await state.get_data()
    await message.reply(f"Your name {user_data['username']}!!")
    # await message.reply(f"Your name {message.from_user.first_name}!!")

@disp.message_handler(commands=['change_name'], state=MyStates.stable)
async def changeMyName(message : Message, state : FSMContext):
    await message.reply("Введите новое имя")
    await MyStates.readName.set()

@disp.message_handler(content_types='text')
async def textHandler(message:Message) :
    await message.answer(message.text)
