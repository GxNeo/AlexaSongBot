from pyrogram import Client, filters
import asyncio
import os
from pytube import YouTube
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from youtubesearchpython import VideosSearch
from AlexaSongBot.mrdarkprince import ignore_blacklisted_users, get_arg
from AlexaSongBot import app, LOGGER
from AlexaSongBot.sql.chat_sql import add_chat_to_db


def yt_search(song):
    videosSearch = VideosSearch(song, limit=1)
    result = videosSearch.result()
    if not result:
        return False
    else:
        video_id = result["result"][0]["id"]
        url = f"https://youtu.be/{video_id}"
        return url


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("mt"))
async def song(client, message):
    chat_id = message.chat.id
    user_id = message.chat.id
    add_chat_to_db(str(chat_id))
    args = get_arg(message) + " " + "song"
    if args.startswith(" "):
        await message.reply("Enter a song name. Check /help")
        return ""
    status = await message.reply("`🔎I\'m Uploading Your Music.. 📺 Please wait some time ⏳️``  ")
    video_link = yt_search(args)
    if not video_link:
        await status.edit("😔Song not found.")
        return ""
    yt = YouTube(video_link)
    audio = yt.streams.filter(only_audio=True).first()
    try:
        download = audio.download(filename=f"{str(user_id)}")
    except Exception as ex:
        await status.edit("Failed to download song")
        LOGGER.error(ex)
        return ""
    rename = os.rename(download, f"{str(user_id)}.mp3")
    await app.send_chat_action(message.chat.id, "upload_audio")
    title = str(yt.title)
    aswin = f"✣ **Music** : [{title[:40]}]({video_link})\n✣ **Uploaded** : [MT Music\'s](https://t.me/mt_music_24)"
    await app.send_audio(
        caption = aswin,
        chat_id=message.chat.id,
        audio=f"{str(user_id)}.mp3",
        duration=int(yt.length),
        title=str(yt.title),
        performer=str('[MT Music\'s]'),
        reply_to_message_id=message.message_id,
    )
    await status.delete()
    os.remove(f"{str(user_id)}.mp3")
