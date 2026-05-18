import re
import asyncio
from os import environ
from Script import script
from time import time
from aiohttp import web

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

def parse_size_to_bytes(value: str, default: int = 0) -> int:
    if value is None:
        return default
    raw = str(value).strip().lower()
    if not raw:
        return default
    m = re.fullmatch(r"(\d+(?:\.\d+)?)\s*([kmgtp]?b?)?", raw)
    if not m:
        return default
    number = float(m.group(1))
    unit = (m.group(2) or "b").rstrip("b")
    scale = {"": 1, "k": 1024, "m": 1024**2, "g": 1024**3, "t": 1024**4, "p": 1024**5}
    return int(number * scale.get(unit, 1))

# --- RENDER WEB SERVER FIX ---
async def handle_ping(request):
    return web.Response(text="Bot is Alive and Running Perfectly!")

async def start_render_server():
    app = web.Application()
    app.router.add_get('/', handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(environ.get("PORT", "10000"))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"========== RENDER SERVER STARTED ON PORT {port} ==========")

# Running the server inside python's main event loop safely
try:
    loop = asyncio.get_event_loop()
    loop.create_task(start_render_server())
except Exception as e:
    print(f"Render server log error: {e}")
# ------------------------------

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '36598189'))
API_HASH = environ.get('API_HASH', 'd4610ba725a8fe3ae59ce7797ac097bc0')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Keep-Alive URL
KEEP_ALIVE_URL = environ.get("KEEP_ALIVE_URL", "")

# Hyperlink & FSub
HYPER_MODE = bool(environ.get('HYPER_MODE', False))
REQUEST_FSUB_MODE = bool(environ.get('REQUEST_FSUB_MODE', True))

# Bot settings
BOT_START_TIME = time()
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://graph.org/file/2ed90a79eb533d86f8a0f.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1090757383').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1003954609639').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
DEFAULT_AUTH_CHANNELS = [int(x) for x in environ.get("AUTH_CHANNEL", "").split() if x.lstrip('-').isdigit()]
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'mn_files')
DATABASE_URI2 = environ.get('DATABASE_URI2', "")
DATABASE_URI3 = environ.get('DATABASE_URI3', "")
DATABASE_URI4 = environ.get('DATABASE_URI4', "")
DATABASE_URI5 = environ.get('DATABASE_URI5', "")
DATABASE_NAME2 = environ.get('DATABASE_NAME2', DATABASE_NAME)
DATABASE_NAME3 = environ.get('DATABASE_NAME3', DATABASE_NAME)
DATABASE_NAME4 = environ.get('DATABASE_NAME4', DATABASE_NAME)
DATABASE_NAME5 = environ.get('DATABASE_NAME5', DATABASE_NAME)
POSTGRES_URI = environ.get('POSTGRES_URI', '')
POSTGRES_STORAGE_LIMIT_BYTES = parse_size_to_bytes(environ.get('POSTGRES_STORAGE_LIMIT_BYTES', '1GB'), 0)

# File Channel Settings
FILE_CHANNELS = [int(ch) for ch in environ.get('FILE_CHANNELS', '').split()]
FILE_CHANNEL_SENDING_MODE = is_enabled(environ.get('FILE_CHANNEL_SENDING_MODE', 'True'), False)
FILE_AUTO_DELETE_SECONDS = int(environ.get('FILE_AUTO_DELETE_SECONDS', 60))

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003935836816'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'mnbots_support')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', 'False')), False)
IMDB = is_enabled((environ.get('IMDB', 'False')), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', 'True')), True)

# Custom File Captions
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}") 
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "📂 <b>File Name:</b> <code>{file_name}</code>\n\n♻️ <b>File Size:</b> <code>{file_size}</code>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂нк: {rating}/ 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Customized Configurations are:-\n"
