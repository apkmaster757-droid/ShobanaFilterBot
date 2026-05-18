class script(object):
    START_TXT = """Hello {}.
I am an auto filter bot which can provide movies in your groups.
+ To get movies, join our channels and search here!"""
    
    HELP_TXT = """
<b>Hey {} 👋</b>

Use the buttons below to browse all features and commands.
Each help page contains a short list for easy reading.
"""
    HELP_PAGES = [
"""<b>📘 Help (1/6): Core Features</b>
• Auto filter and manual filter replies
• IMDB details with poster + metadata
• Spell-check suggestions for wrong queries
• File indexing from linked channels
• Multi-database support (Mongo + SQL)
• Hyperlink result mode support
• Connection manager for PM controls
• File auto-delete and protected delivery
• Multiple force-sub channels support
• Inline search and share support""",
"""<b>📘 Help (2/6): Public Commands</b>
• /start - Start the bot
• /movies - Latest added movies
• /series - Latest added series
• /connect - Connect group to PM
• /disconnect - Disconnect active chat
• /connections - Show your connections
• /settings - Open group settings
• /filter or /add - Create manual filter
• /filters or /viewfilters - List filters
• /del and /delall - Delete filters""",
"""<b>📘 Help (3/6): Utility Commands</b>
• /imdb and /mnsearch - Search movie info
• /id - Show user/chat id
• /info - Show user information
• /bug /bugs /feedback - Send feedback
• /search - Search from external sources
• /paste /pasty /tgpaste - Create paste link
• /short - Shorten URL
• /tr - Translate replied text
• /font - Style your text
• /genpassword or /genpw - Generate password""",
"""<b>📘 Help (4/6): Media/Extra Commands</b>
• /tts - Text to speech
• /carbon - Generate carbon image
• /stickerid - Get sticker file id
• /json /js /showjson - Message JSON
• /img /cup /telegraph - Image to link
• /share /share_text /sharetext - Share text
• /echo - Repeat text
• /pin - Pin replied message
• /unpin - Unpin a message
• /unpin_all - Unpin all messages""",
"""<b>📘 Help (5/6): Group/Admin Commands</b>
• /promote - Promote user in group
• /demote - Demote user in group
• /stats - Show database bot stats
• /invite - Generate group invite link
• /ban - Ban a user from bot
• /unban - Unban a user
• /leave - Leave a chat
• /disable - Disable a chat
• /enable - Enable a chat
• /deletefiles & /deleteall - Bulk file delete
• Channel send mode + auto-delete file delivery""",
"""<b>📘 Help (6/6): Owner/Admin-Only</b>
• /users - List bot users
• /chats - List connected chats
• /channel - List indexed channels
• /broadcast - Broadcast to users
• /grpbroadcast - Broadcast to groups
• /logs - Get recent logs
• /delete - Delete one indexed file
• /fsub - Update force-sub channels
• /restart, /ping, /usage - System tools
• /set_template, /setskip, /clear_join_users
• Bot commands auto-sync on startup
• Auto-update commands: /setupchat /movieupdates /getdlink /sendupnow /getlist"""
    ]
    
    ABOUT_TXT = """<b>
◎ Creator: MN - TG
◎ Language: Python 3
◎ Data Base: Mongo DB
◎ Bot Server: Render</b>"""
    
    SOURCE_TXT = """<b>NOTE:</b>
- This Filter Bot is an open-source project.

<b>DEVS:</b>
- MN - TG"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature where users can set automated replies for a particular keyword.
<b>NOTE:</b>
1. This Bot should have admin privileges.
2. Only admins can add filters in a chat.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat</code>"""
    
    BUTTON_TXT = """Help: <b>Buttons</b>
- This Bot Supports both url and alert inline buttons."""
    
    AUTOFILTER_TXT = """<b>Note: File Index</b>
1. Make me the admin of your channel if it's private.
2. Forward the last message to me with quotes. I'll add all the files in that channel to my DB.

<b>Note: AutoFilter</b>
1. Add the bot as admin on your group.
2. Use /connect and connect your group to the bot."""
    
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters to avoid spamming in groups.

<b>Commands and Usage:</b>
• /connect - <code>connect a particular chat to your PM</code>
• /disconnect - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
• /id - <code>get id of a specified user.</code>
• /info - <code>get information about a user.</code>
• /imdb - <code>get the film information from IMDb source.</code>
• /start - <code>Check I'm Alive.</code>
• /ping - <code>check ping.</code>
• /usage - <code>usage of bot.</code>"""
    
    ADMIN_TXT = """Help: <b>Admin mods</b>
• /logs - <code>to get the recent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of my chats and ids</code>
• /leave - <code>to leave from a chat.</code>
• /disable - <code>to disable a chat.</code>
• /ban - <code>to ban a user.</code>
• /unban - <code>to unban a user.</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    
    STATUS_TXT = """★ TOTAL FILES: <code>{}</code>
 TOTAL USERS: <code>{}</code>
 TOTAL CHATS: <code>{}</code>"""
    
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
"""
    
    RESULT_TXT = """Hey {mention}, 
Just See What I Found For Your Query:"""

    # ✨ Ekdum clean caption (Saare spam links aur Malayalam language permanent saaf)
    CUSTOM_FILE_CAPTION = """📂 <b>Filename:</b> <code>{file_name}</code>
♻️ <b>FileSize:</b> <code>{file_size}</code>

⚠️ <i>This file will be deleted automatically according to channel settings. Please forward it to your Saved Messages to keep it.</i>"""

    RESTART_GC_TXT = """<b>Bot Restarted Successfully!</b>"""
    
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    
    SPOLL_NOT_FND = """I couldn't find anything related to your request. Please check your spelling and try again."""
    
    ENG_SPELL = """Please Note: Ask with correct spelling."""
    MAL_SPELL = """Please Note: Ask with correct spelling."""
    HIN_SPELL = """कृपया सही वर्तनी (Spelling) में पूछें।"""
    TAM_SPELL = """Please Note: Ask with correct spelling."""

    CHK_MOV_ALRT = """♻️ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"""
    OLD_MES = """You are using one of my old messages, please send the request again."""
    MOV_NT_FND = """<b>This Movie is not found or not yet added to DB.</b>"""
    RESTART_TXT = """<b><u>Bot Restarted ✅</u></b>"""
    
