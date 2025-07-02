from pyrogram.types import Message
from yt_dlp import YoutubeDL
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream, AudioPiped

def download_song(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'song.%(ext)s',
        'quiet': True
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=True)['entries'][0]
        return info['title'], ydl.prepare_filename(info)

async def start_handler(client, message: Message, pytgcalls: PyTgCalls):
    if message.text.startswith("/play "):
        query = message.text.split("/play ", 1)[1]
        title, file_path = download_song(query)
        await pytgcalls.join_group_call(
            message.chat.id,
            InputStream(AudioPiped(file_path)),
        )
        await message.reply(f"🎵 Playing: {title}")
