# # main.py

from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Create the bot client
app = Client(
    "telegram_bot",
    api_id=28864821,
    api_hash=a3a7c48e39c5fca814e207829b3159dd,
    bot_token = "8188601797:AAEP-_fHZ0ByC08tIUqVcjmHWkJeVEHDAtY"

)

# Start message handler
@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    await message.reply_text(
        "👋 Hello! I am your Telegram bot.\n\n"
        "✅ I'm running perfectly.\n"
        "Type /help to see more commands!"
    )

# Help message handler
@app.on_message(filters.command("help") & filters.private)
async def help_handler(client, message):
    await message.reply_text(
        "ℹ️ **Available Commands:**\n"
        "/start - Start the bot\n"
        "/help - Show this help message"
    )

# Run the bot
if __name__ == "__main__":
    print("✅ Bot is starting...")
    app.run()
