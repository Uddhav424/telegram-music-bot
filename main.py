from pyrogram import Client
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN
from helper import start_handler

app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(app)

@app.on_message()
async def handler(client, message):
    await start_handler(client, message, pytgcalls)

app.start()
pytgcalls.start()
print("Bot is running...")
app.idle()
