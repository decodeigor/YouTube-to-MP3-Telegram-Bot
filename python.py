import os
import yt_dlp
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters, CallbackQueryHandler

TOKEN = '7802435336:AAGwGJfCW7TNVDsdbROZYufBdZpSBkdv1pA'

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Надіслати посилання на YouTube", callback_data='send_link')],
        [InlineKeyboardButton("Інформація про бота", callback_data='info')],
        [InlineKeyboardButton("Автор бота", callback_data='author')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            text="Привіт! Я допоможу тобі перетворити відео з YouTube в MP3.",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            text="Привіт! Я допоможу тобі перетворити відео з YouTube в MP3.",
            reply_markup=reply_markup
        )

async def info(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Повернутися на головну", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="Цей бот перетворює відео з YouTube в аудіо MP3. Просто надішли посилання на відео і я зроблю все за тебе!",
        reply_markup=reply_markup
    )

async def author(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Telegram", url="https://t.me/igoraa001")],
        [InlineKeyboardButton("Instagram", url="https://www.instagram.com/_igoraa/")],
        [InlineKeyboardButton("GitHub", url="https://github.com/decodeigor")],
        [InlineKeyboardButton("Повернутися на головну", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="Автор бота: themercury.\nЦей бот був створений для зручності перетворення YouTube відео в MP3.\n"
        "Ось мої соцмережі :) :\n\n"
        "Telegram: [@igoraa001](https://t.me/igoraa001)\n"
        "Instagram: [@_igoraa](https://www.instagram.com/_igoraa/)\n"
        "GitHub: [decodeigor](https://github.com/decodeigor)\n",
        reply_markup=reply_markup
    )

async def send_link(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Надіслати посилання на YouTube", callback_data='send_link')],
        [InlineKeyboardButton("До головного меню", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        text="Надішліть посилання на відео YouTube і я перетворю його в MP3!",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: CallbackContext):
    url = update.message.text
    chat_id = update.message.chat_id

    if 'youtube.com' in url or 'youtu.be' in url:
        await update.message.reply_text("Завантажую аудіо, зачекай кілька секунд ...")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'download/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get('title', 'audio')
                filename = ydl.prepare_filename(info).replace('.webm', '.mp3')

            await context.bot.send_audio(chat_id=chat_id, audio=open(filename, 'rb'))

            os.remove(filename)

            keyboard = [
                [InlineKeyboardButton("Отримати ще аудіо", callback_data='send_link')],
                [InlineKeyboardButton("До головного меню", callback_data='start')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(
                text="Аудіо успішно перетворено! Що далі?",
                reply_markup=reply_markup
            )
        except Exception as e:
            await update.message.reply_text("Схоже сталася помилка:(")
    else:
        await update.message.reply_text("Це не схоже на посилання YouTube. Спробуй ще раз")

async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == 'send_link':
        await send_link(update, context)
    elif query.data == 'info':
        await info(update, context)
    elif query.data == 'author':
        await author(update, context)
    elif query.data == 'start':
        await start(update, context)

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()
