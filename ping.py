from pyrogram import Client, filters
from config import group_id

@Client.on_message(filters.chat(group_id) & filters.text & filters.regex("پینگ"))
async def ping(client, message):
    await message.reply("✅ HAYATPLAY Online!")
