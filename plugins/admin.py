import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import ADMINS
from database.ia_filterdb import save_file

def is_admin(user) -> bool:
    return user and (user.id in ADMINS or (f"@{user.username}" in ADMINS if user.username else False))

@Client.on_message(filters.command("index") & filters.private)
async def manual_index(client, message):
    if not is_admin(message.from_user):
        return await message.reply("🚫 Unauthorized")
    
    if len(message.command) < 2:
        return await message.reply("Use: <code>/index -100xxxxxxxxx</code>")
    
    chat_id = int(message.command[1])
    m = await message.reply("⏳ Indexing in progress... scanning channel files.")
    
    count = 0
    # Hum yahan loop use kar rahe hain jo bot ke liye safe hai
    for i in range(1, 2000): # Aap yahan range badha sakte hain
        try:
            msg = await client.get_messages(chat_id, i)
            file = msg.document or msg.video or msg.audio
            if file:
                res = await save_file(file)
                if res: count += 1
        except Exception:
            continue
        
        if i % 20 == 0: await asyncio.sleep(1) # Flood wait se bachne ke liye

    await m.edit(f"✅ Indexing complete!\nTotal files added to DB: <b>{count}</b>")

@Client.on_message(filters.command("admin") & filters.private)
async def admin_panel(client, message):
    if not is_admin(message.from_user): return
    await message.reply("⚙️ Admin Panel is active.")
    
