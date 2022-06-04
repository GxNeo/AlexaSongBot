
from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from AlexaSongBot.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from AlexaSongBot import app, LOGGER
from AlexaSongBot.mrdarkprince import ignore_blacklisted_users
from AlexaSongBot.sql.chat_sql import add_chat_to_db

start_text = """
⚜️Hey [{}](tg://user?id={}),

⚜️I'm Emma 🤗, A Song uploading bot

⚜️I Can Upload Music From YouTube

⚜️I Can Only Work In [MT Music Group]..

⚜️I am Created And Maintained By @amzmtaccount ..
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
  m=await message.reply_text("▰▱▱▱")
  n=await m.edit("▰▰▱▱")
  o=await n.edit("▰▰▰▱")
  p=await o.edit("▰▰▰▰")
  await p.edit(text=Config.START_MSG.format(message.from_user.mention),
    disable_web_page_preview=True,
    reply_markup=InlineKeyboardMarkup(
      [[
             InlineKeyboardButton("🎧 ᴍᴜsɪᴄ.ᴘᴀɴᴅᴀ", url="telegram.dog/musicspanda")
           ],[
             InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/Gxneo"),
             InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")
       ]]))

@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] in OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "[Please Use This Format To Get Music.]. \n -> /mt [Song-Name]\n\n -> /mt [You-Tube Link] "
    await message.reply(text)

OWNER_ID.append(1167010511)
app.start()
LOGGER.info("Your bot is now online.")
idle()
