from pyrogram import Client
from pytgcalls import PyTgCalls
from config import 28864821, AA
from helper import start_handler
from config import API_ID, API_HASH, BOT_TOKEN
app = Client("music_bot", api_id=28864821, api_hash=a3a7c48e39c5fca814e207829b3159dd, bot_token=8186601797:AAEP_-fHZO8yCO8tIUqYcjmHWKJeVEHDAtY)
pytgcalls = PyTgCalls(app)

@app.on_message()
async def handler(client, message):
    await start_handler(client, message, pytgcalls)

app.start()
pytgcalls.start()
print("Bot is running...")
app.idle()
