import asyncio
import logging

from aiogram import  Dispatcher

from aiogram import Dispatcher
from handlers.echo import router
from handlers.mainhandler import mainRT
from handlers.start import startRT
from loader import bot, db  

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
       
    )

    logger.info("Starting bot")


    dp: Dispatcher = Dispatcher()

    dp.include_routers(
         startRT,
         mainRT,
         router
    )



        
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
