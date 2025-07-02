from telegram.ext import Updater, CommandHandler
import requests

def start(update, context):
    update.message.reply_text("👋 Hi! Use /song <name> to get music!")

def song(update, context):
    query = ' '.join(context.args)
    if not query:
        update.message.reply_text("❗ Song name likho: /song kesariya")
        return

    res = requests.get(f"https://saavn.me/search/songs?query={query}").json()
    try:
        song = res['data']['results'][0]
        title = song['name']
        link = song['downloadUrl'][-1]['link']
        update.message.reply_audio(audio=link, caption=f"🎵 {title}")
    except:
        update.message.reply_text("🚫 Song nahi mila")

def main():
    TOKEN = "🔒YOUR_BOT_TOKEN_HERE"  # yahan apna BotFather se mila token daalo
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("song", song))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
