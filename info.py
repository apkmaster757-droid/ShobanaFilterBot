import re
from os import environ

id_pattern = re.compile(r'^\\b[+-]?\\d+\\b')

# ⚙️ Bot Credentials
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# 👑 Admin & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
AUTH_USERS = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_GROUPS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_GROUPS', '').split()]

# 🗄️ Database Config (Supports up to 5 Shards)
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

DATABASE_URI2 = environ.get('DATABASE_URI2', "")
DATABASE_NAME2 = environ.get('DATABASE_NAME2', "Cluster2")
DATABASE_URI3 = environ.get('DATABASE_URI3', "")
DATABASE_NAME3 = environ.get('CLUSTER3_NAME', "Cluster3")
DATABASE_URI4 = environ.get('DATABASE_URI4', "")
DATABASE_NAME4 = environ.get('CLUSTER4_NAME', "Cluster4")
DATABASE_URI5 = environ.get('DATABASE_URI5', "")
DATABASE_NAME5 = environ.get('CLUSTER5_NAME', "Cluster5")

# 📢 Links & Channel Promotion Settings (CONFIGURED TO YOUR CHANNEL)
BRANDING_LINK = "https://t.me/Moviepornindia"
FORCE_SUB = environ.get('FORCE_SUB', 'Moviepornindia') # Aapka Force Sub Channel Username
SUPPORT_CHAT = "Moviepornindia" # Buttons me link hone wala username

# 🖼️ Media Settings
START_IMG = environ.get('START_IMG', 'https://graph.org/file/7eb62c64db3be373b9e4b.jpg') # Safe default start image

# ⚙️ Bot Customization Features
P_TTI_SHOW_OFF = environ.get('P_TTI_SHOW_OFF', "False") == "True"
IMDB = environ.get('IMDB', "False") == "True"
SINGLE_BUTTON = environ.get('SINGLE_BUTTON', "True") == "True"
CUSTOM_FILE_CAPTION = environ.get('CUSTOM_FILE_CAPTION', "📁 <b>File Name:</b> {file_name}\n\n⚙️ <b>Size:</b> {file_size}\n\n🍿 <b>Join Here:</b> @Moviepornindia")
BATCH_FILE_CAPTION = environ.get('BATCH_FILE_CAPTION', "📁 <b>File Name:</b> {file_name}\n\n⚙️ <b>Size:</b> {file_size}\n\n🍿 <b>Join Here:</b> @Moviepornindia")
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', "<b>Title:</b> {title}\n<b>Rating:</b> {rating}")
SPELL_CHECK_REPLY = environ.get('SPELL_CHECK_REPLY', "True") == "True"
MAX_LIST_ELM = int(environ.get('MAX_LIST_ELM', 5))
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', '-100'))
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '').split()]
PROTECT_CONTENT = environ.get('PROTECT_CONTENT', "False") == "True"
PUBLIC_FILE_STORE = environ.get('PUBLIC_FILE_STORE', "False") == "True"

# 🚫 Safety & Limitations
POSTGRES_STORAGE_LIMIT_BYTES = int(environ.get('POSTGRES_STORAGE_LIMIT_BYTES', 536870912))
REQUEST_FSUB_MODE = environ.get('REQUEST_FSUB_MODE', "False") == "True"
HYPER_MODE = environ.get('HYPER_MODE', "False") == "True"
USE_CAPTION_FILTER = False # Strict clean files filter

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
# Welcome settings for new users
MELCOW_NEW_USERS = environ.get('MELCOW_NEW_USERS', "True") == "True"
# Missing settings required by bot.py
SESSION = environ.get('SESSION', 'Media_search')
LOG_STR = environ.get('LOG_STR', '')
KEEP_ALIVE_URL = environ.get('KEEP_ALIVE_URL', '')
DEFAULT_AUTH_CHANNELS = [int(ch) for ch in environ.get('DEFAULT_AUTH_CHANNELS', '').split()]
