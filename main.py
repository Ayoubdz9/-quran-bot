import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "السلام عليكم 👋\n"
        "انا بوت القرآن\n"
        "باه تجيب آية اكتب: /audio رقم_السورة رقم_الآية\n"
        "مثال: /audio 2 255"
    )

async def audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args)!= 2:
            await update.message.reply_text("اكتب هكذا: /audio 2 255")
            return

        surah = args[0]
        ayah = args[1]

        # نجيبو الصوت من API
        url = f"https://cdn.islamic.network/quran/audio/128/ar.alafasy/{surah}{ayah.zfill(3)}.mp3"
        response = requests.get(url)

        # نجيبو النص من API
        text_url = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/ar.alafasy"
        text_data = requests.get(text_url).json()
        text = text_data['data']['text']

        await update.message.reply_audio(audio=response.content)
        await update.message.reply_text(f"سورة {surah} آية {ayah}\n\n{text}")

    except:
        await update.message.reply_text("الآية غير موجودة. تأكد من الرقم")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("audio", audio))
    app.run_polling()

if __name__ == '__main__':
    main()
