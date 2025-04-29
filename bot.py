from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Function to handle text translation
async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # User message (the text to be translated)
    text_to_translate = update.message.text

    # Default: Translate to English (change this to any language you want)
    translated_text = translator.translate(text_to_translate, src='auto', dest='en').text
    
    await update.message.reply_text(f"Original: {text_to_translate}
Translated: {translated_text}")

# Create Telegram bot application
app = ApplicationBuilder().token('7443022179:AAEme9o2mSMz9S6dAruVWpxcgBDj7xLfrdI').build()

# Add the handler for text messages
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

print("Bot is running...")
app.run_polling()
