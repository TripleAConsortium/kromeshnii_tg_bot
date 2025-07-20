#!./myvenv/bin/python3

import telebot
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

import instagram_fixup_telegram_bot.ins_to_tg
instagram_fixup_telegram_bot.ins_to_tg.setup(bot)

if __name__ == '__main__':
    if not TELEGRAM_BOT_TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN not found in .env file")
        exit(1)

    print("Bot running...")
    bot.infinity_polling()
