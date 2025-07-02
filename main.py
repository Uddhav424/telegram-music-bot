from pyrogram import Client
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, 8186601797:AAEP_-fHZO8yCO8tIUqYcjmHWKJeVEHDAtY
from helper import start_handler

app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=8186601797:AAEP_-fHZO8yCO8tIUqYcjmHWKJeVEHDAtY)
pytgcalls = PyTgCalls(app)

@app.on_message()
async def handler(client, message):
    await start_handler(client, message, pytgcalls)

app.start()
pytgcalls.start()
print("Bot is running...")
app.idle()
