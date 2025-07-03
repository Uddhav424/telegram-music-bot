from pyrogram import Client

api_id = 28864821  # Replace with your actual API ID
api_hash = "a3a7c48e39c5fca814e207829b3159dd"  # Replace with your actual API hash
bot_token = "8186601797:AAEP-_AAG6RZYqpB62-L5b9mygzy8subfLFl7XR8o"  # Replace with your actual bot token

app = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message()
def hello(client, message):
    message.reply("Hello! Bot is running successfully ✅")

if __name__ == "__main__":
    app.run()  # ✅ 4 spaces
