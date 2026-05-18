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

# 🚫 FORCE BYPASS SYSTEM (Database ke links aur Malayalam text ko overwrite karne ke liye)
# Yeh function database se aane wale kisi bhi purane text ko automatic override kar dega.
class CleanCaption:
    def format(self, *args, **kwargs):
        file_name = kwargs.get('file_name', 'Not Available')
        file_size = kwargs.get('file_size', 'Not Available')
        
        # Ekdum clean caption format bina kisi kachra ya spam link ke
        return f"📂 <b>Filename:</b> <code>{file_name}</code>\n♻️ <b>FileSize:</b> <code>{file_size}</code>\n\n⚠️ <i>This file will be deleted automatically according to channel settings. Please forward it to your Saved Messages to keep it.</i>"

    def __str__(self):
        # Agar bot bina format kiye direct use karega, tab bhi clean text hi jayega
        return "📂 <b>Filename:</b> {file_name}\n♻️ <b>FileSize:</b> {file_size}\n\n⚠️ <i>This file will be deleted automatically according to channel settings. Please forward it to your Saved Messages to keep it.</i>"

# Purane variables ko overwrite kar rahe hain
CUSTOM_FILE_CAPTION = CleanCaption()
BATCH_FILE_CAPTION = "📂 <b>File Name:</b> <code>{file_name}</code>\n\n♻️ <b>File Size:</b> <code>{file_size}</code>"
IMDB_TEMPLATE = "🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂нк: {rating}/ 10"

LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Customized Configurations are active.-\n"
