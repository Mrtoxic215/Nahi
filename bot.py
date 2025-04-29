import os
import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Bot Token from environment
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise Exception("BOT_TOKEN environment variable not set!")

# Function to fetch song link
async def get_song_link(song_name):
    try:
        response = requests.get(f"https://saavn.dev/api/search/songs?query={song_name}")
        data = response.json()
        song = data['data']['results'][0]
        song_title = song['name']
        song_link = song['downloadUrl']['high']
        return f"**{song_title}**\nDownload Link: {song_link}"
    except Exception as e:
        logging.error(f"Error fetching song: {e}")
        return "Sorry, could not fetch the song. Please try again."

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Send me the song name and I'll get you the download link!")

# Handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    song_name = update.message.text
    reply = await get_song_link(song_name)
    await update.message.reply_text(reply, parse_mode='Markdown')

# Main function
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == '__main__':
    main()
