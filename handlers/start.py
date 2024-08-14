from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message , callback_query
from loader import bot
from aiogram.fsm.context import FSMContext
from states.states import ArizaOlish
from keyboards.keyboards import ustoz_shogird

startRT : Router = Router()
@startRT.message(CommandStart())
async def start(msg: Message ):
    await msg.answer(f"Assalom alaykum {msg.from_user.username} kanalining rasmiy botiga xush kelibsiz! \n\n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!" , reply_markup=ustoz_shogird )