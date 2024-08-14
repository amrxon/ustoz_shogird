from aiogram import Router, F
from aiogram.types import Message
from keyboards.keyboards import ustoz_shogird
from aiogram.fsm.context import FSMContext
from states.states import ArizaOlish
from keyboards.keyboards import xayuq
malumotlar = {}

mainRT : Router = Router()

@mainRT.message(F.text == "Sherik kerak")
async def sherik_handler(message : Message , state : FSMContext):
    await state.set_state(ArizaOlish.FISH) 
    await message.answer("Ism Familya kiriting")

@mainRT.message(ArizaOlish.FISH)
async def FISH_handler(message : Message , state : FSMContext):
    malumotlar["FISH"] = message.text
    await state.set_state(ArizaOlish.Texno)
    await message.answer("📚 Texnologiya: \n\n Talab qilinadigan texnologiyalarni kiriting? \nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\n Java, C++, C")



@mainRT.message(ArizaOlish.Texno)
async def FISH_handler(message : Message , state : FSMContext):
    malumotlar["Texno"] = message.text
    await state.set_state(ArizaOlish.Nomer)
    await message.answer("Boglanish uchun nomeringizni kiriting")
    

@mainRT.message(ArizaOlish.Nomer)
async def FISH_handler(message : Message , state : FSMContext):
    malumotlar["Nomer"] = message.text
    await state.set_state(ArizaOlish.Manzil)
    await message.answer("Manzilingizni kiriting")
    

@mainRT.message(ArizaOlish.Manzil)
async def FISH_handler(message : Message , state : FSMContext):
    malumotlar["Manzil"] = message.text
    await state.set_state(ArizaOlish.Narxi)
    await message.answer("qancha pulga ishlashizi kiriting")
    

@mainRT.message(ArizaOlish.Narxi)
async def FISH_handler(message : Message , state : FSMContext):
    malumotlar["Narxi"] = message.text
    await state.set_state(ArizaOlish.Kasb)
    await message.answer("qaysi yunalishta ishlashizi kiriting \n masalan:python")


@mainRT.message(ArizaOlish.Murojatvaqt)
async def FISH_handler(message : Message , state : FSMContext):
    malumotlar["Murojatvaqt"] = message.text
    await state.set_state(ArizaOlish.Maqsad)
    await message.answer("Maqsadingizni kiriting")
    

@mainRT.message(ArizaOlish.Kasb)
async def FISH_handler(message : Message , state : FSMContext):
    malumotlar["Kasb"] = message.text
    await state.set_state(ArizaOlish.Murojatvaqt)
    await message.answer("bush vaxtizi kiriting")
    

@mainRT.message(ArizaOlish.Maqsad)
async def FISH_handler(message : Message , state : FSMContext):
    malumotlar['Maqsad'] = message.text
    await state.set_state(ArizaOlish.Maqsad)
    await message.answer(f""" 

🏅 Sherik: {malumotlar['FISH']}
📚 Texnologiya: {malumotlar['Texno']} 
🇺🇿 Telegram: {message.from_user.username}
📞 Aloqa:  {malumotlar['Nomer']}
🌐 Hudud: {malumotlar['Manzil']} 
💰 Narxi: {malumotlar['Narxi']}
🕰 Murojaat qilish vaqti: {malumotlar['Murojatvaqt']} 
👨🏻‍💻 Kasbi: {malumotlar['Kasb']}
🔎Maqsad: 'Maqsad' {malumotlar['Maqsad']}

""" , reply_markup=xayuq)