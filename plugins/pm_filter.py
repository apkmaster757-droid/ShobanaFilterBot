# Kanged From @TroJanZheX
# hyper link mode by mn-bots
import asyncio
import re
import ast
import math
import logging
from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
import pyrogram
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, make_inactive
from info import (
    ADMINS, AUTH_USERS, CUSTOM_FILE_CAPTION, AUTH_GROUPS, P_TTI_SHOW_OFF, IMDB,
    SINGLE_BUTTON, SPELL_CHECK_REPLY, IMDB_TEMPLATE, DATABASE_URI, DATABASE_URI2, DATABASE_URI3, DATABASE_URI4, DATABASE_URI5,
    POSTGRES_STORAGE_LIMIT_BYTES, HYPER_MODE
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings, create_invite_links
from database.users_chats_db import db
from database.ia_filterdb import Media, get_file_details, get_search_results
from database.filters_mdb import del_all, find_filter, get_filters

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

BUTTONS = {}
MONGO_DB_CAP_BYTES = 536870912
MONGO_DB_COUNT = len([u for u in (DATABASE_URI, DATABASE_URI2, DATABASE_URI3, DATABASE_URI4, DATABASE_URI5) if u])
SPELL_CHECK = {}

def _format_search_time(seconds):
    return f"⏱ Results fetched in: {seconds:.2f}s"

# Safe declaration of manual_filters and auto_filter to prevent ImportError
async def manual_filters(client, message, text=None):
    try:
        group_id = message.chat.id
        name = text or message.text
        reply_text, btn, alert, fileid = await find_filter(group_id, name.lower())
        if reply_text:
            reply_text = reply_text.replace("\\n", "\n").replace("\\t", "\t")
            if btn is not None:
                try:
                    await message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)
                except Exception:
                    await message.reply_text(reply_text, disable_web_page_preview=True)
            else:
                await message.reply_text(reply_text, disable_web_page_preview=True)
            return True
        return False
    except Exception as e:
        logger.exception(e)
        return False

async def auto_filter(client, msg, spoll=False):
    if not spoll:
        message = msg
        search = message.text
    else:
        message = msg.message
        search = spoll[0]
    
    if not search:
        return
        
    search = re.sub(r'https?://\S+', '', search)
    search = re.sub(r'@\S+', '', search)
    search = search.strip()
    
    if not search:
        return

    files, offset, total_results, search_time = await get_search_results(search, offset=0, filter=True, fast=True, return_time=True)
    if not files:
        if SPELL_CHECK_REPLY:
            # Simple spellcheck fall-through logic
            pass
        return

    key = f"{message.id}-{message.chat.id}"
    BUTTONS[key] = search
    settings = await get_settings(message.chat.id)

    if HYPER_MODE:
        cap_lines = []
        for file in files:
            file_link = f"https://t.me/{temp.U_NAME}?start=file_{file.file_id}"
            cap_lines.append(f"📁 {get_size(file.file_size)} - [{file.file_name}]({file_link})")
        cap_text = "\n".join(cap_lines)
        cap_text = f"{cap_text}\n\n{_format_search_time(search_time)}"
        btn = []
    else:
        if settings.get('button', True):
            btn = [[InlineKeyboardButton(text=f"📂[{get_size(file.file_size)}] ➵ {file.file_name}", callback_data=f'files#{file.file_id}')] for file in files]
        else:
            btn = [[InlineKeyboardButton(text=f"{file.file_name}", callback_data=f'files#{file.file_id}'), InlineKeyboardButton(text=f"{get_size(file.file_size)}", callback_data=f'files_#{file.file_id}')] for file in files]

    if total_results > 10:
        btn.append([InlineKeyboardButton("📃 1 / " + str(math.ceil(total_results / 10)), callback_data="pages"), InlineKeyboardButton("NEXT ▶️", callback_data=f"next_{message.from_user.id if message.from_user else 0}_{key}_10")])

    if HYPER_MODE:
        await message.reply_text(text=cap_text, parse_mode=enums.ParseMode.MARKDOWN, disable_web_page_preview=True)
    else:
        await message.reply_text(text=f"<b>Found {total_results} results...</b>\n{_format_search_time(search_time)}", reply_markup=InlineKeyboardMarkup(btn))

@Client.on_message(filters.group | filters.private & filters.text & filters.incoming) 
async def give_filter(client, message):
    try:
        k = await manual_filters(client, message)
        if k == False:
            await auto_filter(client, message)
    except Exception as e:
        logger.exception(e)

@Client.on_callback_query(filters.regex(r"^next"))
async def next_page(bot, query):
    ident, req, key, offset = query.data.split("_")
    if int(req) not in [query.from_user.id, 0]:
        return await query.answer("**Search for Yourself**🔎", show_alert=True)

    try:
        offset = int(offset)
    except:
        offset = 0

    search = BUTTONS.get(key)
    if not search:
        await query.answer(script.OLD_MES if hasattr(script, 'OLD_MES') else "Old Message!", show_alert=True)
        return

    files, n_offset, total, search_time = await get_search_results(search, offset=offset, filter=True, fast=True, return_time=True)
    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0

    if not files:
        return

    settings = await get_settings(query.message.chat.id)

    if HYPER_MODE:
        cap_lines = []
        for file in files:
            file_link = f"https://t.me/{temp.U_NAME}?start=file_{file.file_id}"
            cap_lines.append(f"📁 {get_size(file.file_size)} - [{file.file_name}]({file_link})")
        cap_text = "\n".join(cap_lines)
        cap_text = f"{cap_text}\n\n{_format_search_time(search_time)}"
        btn = []
    else:
        if settings.get('button', True):
            btn = [[InlineKeyboardButton(text=f"📂[{get_size(file.file_size)}] ➵ {file.file_name}", callback_data=f'files#{file.file_id}')] for file in files]
        else:
            btn = [[InlineKeyboardButton(text=f"{file.file_name}", callback_data=f'files#{file.file_id}'), InlineKeyboardButton(text=f"{get_size(file.file_size)}", callback_data=f'files_#{file.file_id}')] for file in files]

    if 0 < offset <= 10:
        off_set = 0
    elif offset == 0:
        off_set = None
    else:
        off_set = offset - 10

    if n_offset == 0:
        btn.append([InlineKeyboardButton("◀️ BACK", callback_data=f"next_{req}_{key}_{off_set}"), InlineKeyboardButton(f"📃 {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages")])
    elif off_set is None:
        btn.append([InlineKeyboardButton(f"📃 {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages"), InlineKeyboardButton("NEXT ▶️", callback_data=f"next_{req}_{key}_{n_offset}")])
    else:
        btn.append([InlineKeyboardButton("◀️ BACK", callback_data=f"next_{req}_{key}_{off_set}"), InlineKeyboardButton(f"📃 {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages"), InlineKeyboardButton("NEXT ▶️", callback_data=f"next_{req}_{key}_{n_offset}")])

    try:
        if HYPER_MODE:
            await query.edit_message_text(text=cap_text, reply_markup=InlineKeyboardMarkup(btn), parse_mode=enums.ParseMode.MARKDOWN, disable_web_page_preview=True)
        else:
            await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(btn))
    except MessageNotModified:
        pass
    await query.answer(_format_search_time(search_time))

@Client.on_callback_query(filters.regex(r"^spol")) 
async def advantage_spoll_choker(bot, query):
    _, user, movie_ = query.data.split('#')
    if int(user) != 0 and query.from_user.id != int(user):
        return await query.answer("Search for Yourself🔎", show_alert=True)
    if movie_ == "close_spellcheck":
        return await query.message.delete()
    movies = SPELL_CHECK.get(query.message.reply_to_message.id)
    if not movies:
        return await query.answer(script.OLD_MES if hasattr(script, 'OLD_MES') else "Old Message!", show_alert=True)
    movie = movies[(int(movie_))]
    await query.answer("Checking movie...")
    k = await manual_filters(bot, query.message, text=movie)
    if k == False:
        files, offset, total_results, search_time = await get_search_results(movie, offset=0, filter=True, fast=True, return_time=True)
        if files:
            await auto_filter(bot, query, (movie, files, offset, total_results, search_time))
        else:
            k = await query.message.edit("Movie Not Found!")
            await asyncio.sleep(10)
            await k.delete()

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
    elif query.data == "pages":
        await query.answer()     
    elif query.data == "start":
        buttons = [[InlineKeyboardButton('ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs', url=f'http://t.me/{temp.U_NAME}?startgroup=true')],[InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about')],[InlineKeyboardButton(f'ᴏᴛᴛ ᴜᴘᴅᴀᴛᴇs', url='https://t.me/Moviepornindia'),InlineKeyboardButton(f'ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ', url='https://t.me/Moviepornindia')],[InlineKeyboardButton('ʀᴇᴘᴏ', url='https://github.com/mn-bots/ShobanaFilterBot')]]
        await query.message.edit_text(text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME) if hasattr(script, 'START_TXT') else "Welcome!", reply_markup=InlineKeyboardMarkup(buttons), parse_mode=enums.ParseMode.HTML)
    elif query.data == "help":
        buttons = [[InlineKeyboardButton('◀️ Pʀᴇᴠ', callback_data='help_page_5'),InlineKeyboardButton('1/6', callback_data='pages'),InlineKeyboardButton('Nᴇxᴛ ▶️', callback_data='help_page_1')],[InlineKeyboardButton('Hᴏᴍᴇ', callback_data='start')]]
        await query.message.edit_text(text="Help Menu", reply_markup=InlineKeyboardMarkup(buttons), parse_mode=enums.ParseMode.HTML)
        
