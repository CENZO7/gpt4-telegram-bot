from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import openai

openai.api_key = "77777⁷⁷777777"
BOT_TOKEN = "7777777⁷7⁷777"

def chat(update: Update, context: CallbackContext):
    user_msg = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_msg}]
        )
        update.message.reply_text(response['choices'][0]['message']['content'])
    except Exception as e:
        update.message.reply_text(f"Xatolik yuz berdi: {e}")

updater = Updater(BOT_TOKEN)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))
updater.start_polling()
updater.idle()
