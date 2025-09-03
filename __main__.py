from pyrogram import Client, filters
from config import api_id, api_hash, session_string, group_id

app = Client(session_string, api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(group_id) & filters.text & filters.command(["start"], prefixes=["", " "]))
async def start(client, message):
    await message.reply("🎶 ربات HAYATPLAY فعال است و آماده پخش موزیک!")

app.run()
