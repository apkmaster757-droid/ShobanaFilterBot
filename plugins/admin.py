import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import ADMINS
from database.users_chats_db import db
import plugins.new_updates as nu
from plugins.commands import build_fsub_details_text
from database.ia_filterdb import save_file

def is_admin(user) -> bool:
    return user and (user.id in ADMINS or (f"@{user.username}" in ADMINS if user.username else False))

# --- Admin Panel UI ---
def _updates_text():
    cfg = nu.get_runtime_update_config()
    return (
        "<b>Movie Updates Config</b>\n\n"
        f"PAGE_SIZE: <code>{cfg['PAGE_SIZE']}</code>\n"
        f"SEND_DELAY: <code>{cfg['SEND_DELAY']}</code>\n"
        f"GROUP_SIZE: <code>{cfg['GROUP_SIZE']}</code>\n"
        f"CHANNEL_SEND_MODE: <code>{cfg['CHANNEL_SEND_MODE']}</code>"
    )

def _updates_markup():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Refresh", callback_data="admin:updates"), InlineKeyboardButton("Back", callback_data="admin:back")],
    ])

# --- Indexing Core (The Fix) ---
@Client.on_message(filters.command("index") & filters.private)
async def manual_index(client, message):
    if not is_admin(message.from_user):
        return await message.reply("🚫 Unauthorized")
    
    if len(message.command) < 2:
        return await message.reply("Use: <code>/index -100xxxxxxxxx</code>")
    
    target_chat = int(message.command[1])
    m = await message.reply(f"⏳ Starting index for: <code>{target_chat}</code>\nPlease wait...")
    
    count = 0
    # Telegram bot limitations workaround: Using a direct iterator
    try:
        async for msg in client.get_chat_history(target_chat):
            file = msg.document or msg.video or msg.audio
            if file:
                try:
                    # Direct database save call
                    res = await save_file(file)
                    if res: count += 1
                except Exception:
                    continue
        await m.edit(f"✅ Indexing Success!\nTotal files added: <b>{count}</b>")
    except Exception as e:
        await m.edit(f"❌ Critical Error: <code>{str(e)}</code>\n\nMake sure bot is ADMIN in the channel.")

# --- Existing Admin UI Handlers ---
@Client.on_message(filters.command("admin") & filters.private)
async def admin_panel(client, message):
    if not is_admin(message.from_user): return
    await message.reply("⚙️ Admin Panel", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Updates", callback_data="admin:updates")]]))

@Client.on_callback_query(filters.regex(r"^admin:updates$"))
async def admin_updates(client, query):
    if not is_admin(query.from_user): return
    await query.message.edit_text(_updates_text(), reply_markup=_updates_markup())

@Client.on_callback_query(filters.regex(r"^admin:back$"))
async def admin_back(client, query):
    await admin_updates(client, query) # Simplified for now
