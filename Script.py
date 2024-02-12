class script(object):
    START_TXT = """**Hey {}**👋🏻
    
Welcome To [{}](https://t.me/{})</b> 😇
Here You Can Find Episodes of Many Indian <b>Mythological</b> Serials In HD Qualities! 🔥
    
➺ **/serials** (list of all serials) •
**Check Help Button For More Info !!**.
"""
    LZTHMB_TEXT = """..."""
    LZLINK_TEXT = """..."""
    DNT_TEXT = """..."""
    REQ_AUTH_TEXT = """You are not authentic user to use this"""
    
    TEXT = "Send image to set custom thumbnail."

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\n\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."

    FORMAT_SELECTION = " "

    FORMAT_SELECTION2 = "⏯ **File Name:** {}\n\n🧬 **File Size:** {}\n**⩙ Upload Type:** {}"
    
    SET_CUSTOM_USERNAME_PASSWORD = """"""

    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"

    UPLOAD_START = "<b>Initiating Upload... ⚡</b>"

    LAZY_UPLOAD_START = """<b>● Trying to Upload File ●</b>\n\n⏯ **File Name:** `{}`"""

    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "▼ Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\n▲ Uᴘʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs\n\n★.•☆•.★𑁔𑁔★ D𝖾𝗍✫𝗂𝗅𝗌 ★𑁔𑁔★.•☆•.★\n\n🔗 <b>URL:</b> {}\n\n✩ 📂 <b>Old Name:</b> `{}`\n\n✩ 📝 <b>New Name:</b> `{}`\n\n🧬 **File Size:** `{}`\n\n🧡 Thank you 🧡"

    CUSTOM_CAPTION_UL_FILE = " "

    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Please provide me fast download url 👊"

    HELP_TXT = """Help text"""

    LAZY_URL_HELP_TXT = """
🧬 How to index database channel 
➪ Add me to your database channel as ADMIN and send me the last media from you db channel with quote. 

🧬 How to set thumbnail for renaming media
➪ Send me a photo and reply that photo with cmd /st or /set_thumb or /set_thumbnail

🧬 How to set thumbnail for URL Downloading
➪ Send me a photo and reply that photo with cmd /slt or /set_lazy_thumb or /set_lazy_thumbnail

🧬 How to show normal thumbnail
➪ Send /vt or /veiw_thumb or /view_thumbnail

🧬 How to show url thumbnail
➪ Send /vlt or /veiw_lazy_thumb or /view_lazy_thumbnail

🧬 How To Delete normal Thumbnail
➪ Send /dt or /del_thumb or /delete_thumb

🧬 How To Delete URL Thumbnail
➪ Send /dlt or /del_lazy_thumb or /delete_lazy_thumb

🧬 How to Rename any Media
➪ Send me a video or document i will provide you renaming function

🧬 How To Upload File Or Media using url
➪ Send me any direct download link of your file.

"""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/LazyDeveloper>LazyDeveloper</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v10.0.0 [ 𝙱𝙴𝚃𝙰 ]"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and LazyPriness will respond whenever that keyword hits the message

<b>NOTE:</b>
1. BOT should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. BOT supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/LazyDeveloper)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Lazy Princess

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    PROGRESS_BAR = """\n
╭━━━━❰ PROGRESS BAR ❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """
                  
    DISCLAIMER_TXT =  """<b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪᴅᴅᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.
</b>"""

    TELEGRAPH_TXT = """ Hᴇʟᴘ : <b>Tᴇʟᴇɢʀᴀᴘʜ</b>

<b>Nᴏᴛᴇ</b>: ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ᴘᴍꜱ. ᴀʟꜱᴏ ᴄᴀɴ ʙᴇ ᴜꜱᴇ ʙʏ ᴇᴠᴇʀʏᴏɴᴇ.

<b>Cᴏᴍᴍᴀɴᴅs & Usᴀɢᴇ :</b>
• /telegraph - sᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ 𝟻ᴍʙ"""

    FONT_TXT = """Hᴇʟᴘ : <b>Fᴏɴᴛ</b>

<b>Nᴏᴛᴇ</b>: ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜰᴏɴᴛꜱ ꜱᴛʏʟᴇ, ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴍᴇ ʟɪᴋᴇ ᴛʜɪꜱ ꜰᴏʀᴍᴀᴛ. 

<code>/font Text</code>"""
    
    ALRT_TXT = """<b>Not Your's</b>"""

    OLD_ALRT_TXT = """<b>Search Again!</b>"""

    CUDNT_FND = """<b>ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}
ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?</b>"""

    I_CUDNT = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 😕

Mᴏᴠɪᴇs Nᴏᴛ Aᴠᴀɪʟᴀʙʟᴇ Rᴇᴀsᴏɴ:
𝟷. ᴏ.ᴛ.ᴛ ᴏʀ ᴅᴠᴅ ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ
𝟸. ᴛʏᴘᴇ ɴᴀᴍᴇ ᴡɪᴛʜ ʏᴇᴀʀ
𝟹. ᴍᴏᴠɪᴇ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs @TG_Bots_Supporter</b>"""

    I_CUD_NT = """<b>ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴏʀ ɪᴍᴅʙ...</b>"""

    MVE_NT_FND = """<b>Not available!</b>"""

    TOP_ALRT_MSG = """<b>Cʜᴇᴄᴋɪɴɢ Iɴ Dᴀᴛᴀʙᴀsᴇ...</b>"""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""
    
    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ᴀꜰᴛᴇʀ 5 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ"""

    

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>🥲"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

🧿 𝐓𝐈𝐓𝐋𝐄: <a href={url}>{title}</a>
🎭 𝐆𝐄𝐍𝐑𝐄𝐒: {genres}
📆 𝐘𝐄𝐀𝐑: <a href={url}/releaseinfo>{year}</a>
🌟 𝐑𝐀𝐓𝐈𝐍𝐆: <a href={url}/ratings>{rating}</a> / 10 (Based on {votes} user ratings)</b>
☀️ 𝐋𝐀𝐍𝐆𝐔𝐀𝐆𝐄 : <code>{languages}</code></a>
📀 𝐑𝐔𝐍𝐓𝐈𝐌𝐄: {runtime} Minutes</a>

<b>👨‍💼 Requested by : {message.from_user.mention}</b>"""

    
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """Hᴇʟᴘ : <b>Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs</b>
    
◈ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.
    
<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /gfilter - Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.
• /gfilters - Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.
• /delg - Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.
• /delallg - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ."""
    
    FILE_STORE_TXT = """Hᴇʟᴘ : <b>Fɪʟᴇ Sᴛᴏʀᴇ</b>
    
◈ Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /batch - ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.
• /link - ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.
• /pbatch - ᴊᴜsᴛ ʟɪᴋᴇ <code>/batch</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
• /plink - ᴊᴜsᴛ ʟɪᴋᴇ <code>/link</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ."""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>ᴠ𝟹.𝟶 [ Sᴛᴀʙʟᴇ ]</code></b>"""

# serials

    SERIALS_TXT = """<b>Select The Year To Get Serial !!</b>\n\n<b>For e.g Mahabharat Serial Released In 2013 You Can Select Year 2013 To Get That Serial</b> !! 🙆"""
    Y_TXT = """<b>Here Is Available Serials In These Year</b> !!📅\n\n<b>Click Below 👇 To Choose Serials</b>"""
    
    LUV_KUSH = """<b>Uttar Ramayan</b> - Luv Kush Leela ✨
    
<b>Total Episode :</b> <code>39</code>

<b>About :</b> Luv and Kush, the sons of Lord Rama and Sita, support their mother during her exile from Ayodhya. When they visit Ayodhya, a shocking truth is revealed to them.

<b>How To Search Episode ⁉️</b>
<code>Luv Kush S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    SHRI_KRISHNA = """<b>Shri Krishna</b> ✨
    
<b>Total Episode :</b> <code>221</code>

<b>About :</b> When evil takes over the world, Lord Vishnu incarnates into the world as Shri Krishna for the protection of the righteous and the destruction of the wicked.

<b>How To Search Episode ⁉️</b>
<code>Shri Krishna S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    JAI_HANUMAN = """<b>Jai Hanuman</b> ✨
    
<b>Total Episode :</b> <code>89</code>

<b>About :</b> Jai Hanuman - Sankat Mochan Naam Tiharo is an Indian television mythology drama series that premiered from 23 August 2022 on Dangal TV. Produced by Alind Srivastava and Nissar Parvez under Peninsula Pictures, it stars Akshay Dogra, Madirakshi Mundle, Amar Upadhyay and Apara Mehta.

<b>How To Search Episode ⁉️</b>
<code>Jai Hanuman S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    MAHABHARAT_OLD = """<b>Mahabharat (1998)</b> ✨
    
<b>Total Episode :</b> <code>94</code>

<b>About :</b> When differences between the Kaurava and the Pandava clans, who belong to the same family line, lead them to the threshold of war, Lord Krishna decides to step in and take control of the situation.

<b>How To Search Episode ⁉️</b>
<code>Mahabharat 1988 S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    JAI_MAHALAKSHMI = """<b>Jai Mahalakshmi</b> ✨
    
<b>Total Episode :</b> <code>56</code>

<b>About :</b> Goddess Lakshmi is the supreme goddess of wealth and prosperity, Devi Durga took the intense form of Mahalakshmi to protect the world when Lakshmi disappeared preceding Samudra Manthan.

<b>How To Search Episode ⁉️</b>
<code>Jai Mahalakshmi S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    JAI_MAHALAKSHMI = """<b>Shiv Mahapuran</b> ✨
    
<b>Total Episode :</b> <code>61</code>

<b>About :</b> The story of Indian God Shiv. It includes various stories of demons and Gods involved in Hindu Mythology.

<b>How To Search Episode ⁉️</b>
<code>Shiv Mahapuran S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    MEERA = """<b>Meera 2008</b> ✨
    
<b>Total Episode :</b> <code>134</code>

<b>About :</b> Meera, a young Rajput princess, is overcome with love and devotion to Lord Krishna and sacrifices everything in her life to become a saint and poet.

<b>How To Search Episode ⁉️</b>
<code>Meera S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    LITTLE_KRISHNA = """<b>Little Krishna</b> ✨
    
<b>Total Episode :</b> <code>13</code>

<b>About :</b> Little Krishna, a mischievous child, lives in the village of Vrindavan. He decides to save the villagers from an evil king, Kamsa, who sends ferocious demons upon them.

<b>How To Search Episode ⁉️</b>
<code>Little Krishna S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    DWARKADHEESH = """<b>Dwarkadheesh</b> ✨
    
<b>Total Episode :</b> <code>204</code>

<b>About :</b> After becoming the king of Dwarka, Lord Krishna becomes a protector and maintains relationships with his family members and loved ones.

<b>How To Search Episode ⁉️</b>
<code>Dwarkadheesh S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    DKDM = """<b>Devon Ke Dev Mahadev</b> ✨
    
<b>Total Episode :</b> <code>820</code>

<b>About :</b> Lord Shiva, an ascetic, and his divine consort, Goddess Shakti, create the universe. However, they separate for the sake of it and are reunited when she is reincarnated as Goddess Parvati.

<b>How To Search Episode ⁉️</b>
<code>Devon ke Dev Mahadev S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    BUDDHA = """<b>Buddha</b> ✨
    
<b>Total Episode :</b> <code>55</code>

<b>About :</b> Prince Siddhartha's father shelters him from witnessing the sufferings of life. However, being curious by nature, he comes across the various stages of suffering and sets out to attain enlightenment.

<b>How To Search Episode ⁉️</b>
<code>Buddha S01 E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    MAHABHARAT_NEW = """<b>MahaBharat (2013)</b> ✨
    
<b>Total Episode :</b> <code>267</code>

<b>About :</b> The mother of all wars, the epitome of all rivalries, the cauldron of emotions, insecurities, jealousies, and power play - Mahabharat!

<b>How To Search Episode ⁉️</b>
<code>Mahabharat S01E01 HS</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    HATIM = """<b>The Adventures Of Hatim</b> ✨
    
<b>Total Episode :</b> <code>68</code>

<b>About :</b> Hatim, the Prince of Yemen, lives a graceful life. However, things change when he has to solve the seven riddles to defeat the wicked sorcerer Zargam.

<b>How To Search Episode ⁉️</b>
<code>Hatim S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    SURYAPUTRA_KARN = """<b>Suryaputra Karn</b> ✨
    
<b>Total Episode :</b> <code>307</code>

<b>About :</b> Karna, son of Surya and Kunti and the doyen of archers, endures a challenging journey on his way to becoming one of the greatest warriors of the Mahabharata.

<b>How To Search Episode ⁉️</b>
<code>Suryaputra karn E1</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    SIYA_KE_RAM = """<b>Siya Ke Ram</b> ✨
    
<b>Total Episode :</b> <code>304</code>

<b>About :</b> After their marriage, Rama and Shinta must go into exile because Queen Kaikeyi wants her son Bharata to assume the throne. Their relationship is tested again when Shinta is kidnapped by Rahwana.

<b>How To Search Episode ⁉️</b>
<code>Siya ke ram S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    KRISHNA_BALRAM = """<b>Krishna Balram</b> ✨
    
<b>Total Episode :</b> <code>65</code>

<b>About :</b> Follow through the thrilling capers and chilling escapades of Krishna and Balram, with Radha, and friends in this all new, action packed, adrenaline churning series.

<b>How To Search Episode ⁉️</b>
<code>Krishna Balram S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    MAA_SHAKTI = """<b>Maa Shakti</b> ✨
    
<b>Total Episode :</b> <code>78</code>

<b>About :</b> Take a look at the depiction of Maa Shakti who is known as the divine force in Hinduism. She is considered the source of power and creation and can transform herself into various forms.

<b>How To Search Episode ⁉️</b>
<code>Maa Shakti S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    KBM_GANESH_KI_SAVARI = """<b>Kaise Bane Mushak Ganeshji Ki Savari?</b> ✨
    
<b>Total Episode :</b> <code>08</code>

<b>About :</b> Ganesh arrives in Devlok and engages in a fierce battle with Mushikasur. Ganesh seeks Somnandi's help to fight Mushikasur and his army of mice...

<b>How To Search Episode ⁉️</b>
<code>KBMGKS S01 E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    RADHAKRISHN = """<b>Radhakrishn (2018)</b> ✨
    
<b>Total Episode :</b> <code>1145</code>

<b>About :</b> Lord Krishna and Radha share pure love for one another but things take a turn when Radha receives a curse that she will be separated from him.

<b>How To Search Episode ⁉️</b>
<code>Radhakrishn S1 E1</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    KARN_SANGINI = """<b>Karn Sangini</b> ✨
    
<b>Total Episode :</b> <code>90</code>

<b>About :</b> Urvi is a princess of noble birth and her parents want her to marry her childhood friend Arjun. However, she falls for the Karna, a man of low caste and invites a whole set of problems.

<b>How To Search Episode ⁉️</b>
<code>Karn Sangini S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    M_VADH = """<b>Mahishasura Vadh</b> ✨
    
<b>Total Episode :</b> <code>10</code>

<b>About :</b> Mahishasura Vadh is a mini-series based on the remarkable story of how Goddess Durga killed the powerful buffalo demon Mahishasura, exemplifying...

<b>How To Search Episode ⁉️</b>
<code>Mahishasur vadh S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    SB_MAHAPURAN = """<b>Shrimad Bhagwat Mahapuran</b> ✨
    
<b>Total Episode :</b> <code>00</code>

<b>About :</b> In a divine discourse with Radha, Lord Krishna takes it upon himself to explain texts from the ancient and fabled Srimad Bhagwat, sacred in Hinduism, which offers mankind profound spiritual knowledge.

<b>How To Search Episode ⁉️</b>
<code>Shrimad Bhagwat Mahapuran S01 E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    JJMV = """<b>Jag Jaanani Maa Vaishnodevi</b> ✨
    
<b>Total Episode :</b> <code>207</code>

<b>About :</b> The goddesses combine their powers to create Goddess Vaishnodevi and task her with the responsibility of destroying the forces of evil that threaten to destroy Earth.

<b>How To Search Episode ⁉️</b>
<code>Jag Jaanani Maa Vaishnodevi S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    NAMAH = """<b>Namah Lakshmi Narayan</b> ✨
    
<b>Total Episode :</b> <code>65</code>

<b>About :</b> Eternal friends Lord Mahadev and Lord Narayan are quite different from each other but maintain a harmonious relationship. Soon, things change as their bond is challenged by the arrival of Kalyug.

<b>How To Search Episode ⁉️</b>
<code>Namah Laxmi Narayan S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    DEVA_SHREE_GANESHA = """<b>Deva Shree Ganesha</b> ✨
    
<b>Total Episode :</b> <code>11</code>

<b>About :</b> People celebrate Ganesh Chaturthi, which is dedicated to Lord Ganesh, the remover of obstacles. Devotees bring home idols and adorn them with garlands, perform 'aartis' and distribute sweets.

<b>How To Search Episode ⁉️</b>
<code>Deva Shree Ganesha S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    DEV_ADI_PARASHAKTI = """<b>Devi Adi Parashakti</b> ✨
    
<b>Total Episode :</b> <code>87</code>

<b>About :</b> Devi Adi Parashakti, the goddess of the universe, takes various forms on Earth in order to guide mankind towards humanity and compassion.

<b>How To Search Episode ⁉️</b>
<code>Devi Adi Parashakti S01E01 </code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    KAHAT_HANUMAN_JSRAM = """<b>Kahat Hanuman Jaishree Ram</b> ✨
    
<b>Total Episode :</b> <code>120</code>

<b>About</b> : Hanuman, a beloved deity in Hinduism, conquers various obstacles and overcomes insurmountable challenges in his quest to rid the world of evil.

<b>How To Search Episode ⁉️</b>
<code>Kahat Hanuman S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    BAAL_SHIV = """<b>Baal Shiv</b> ✨
    
<b>Total Episode :</b> <code>215</code>

<b>About</b> : Lord Shiva in his younger avatar, faces several challenges as he strives to uphold justice in his realm and facilitates the destruction of evil forces.

<b>How To Search Episode ⁉️</b>
<code>Baal Shiv S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    JKLK = """<b>Jai Kanhaiya Lal Ki</b> ✨
    
<b>Total Episode :</b> <code>185</code>

<b>About</b> : Young Krishna grows up with a strong bond with his mother, Devaki, and his foster-mother, Yashoda. However, his power and strength are tested when he must protect his family and village from the evil Kans.

<b>How To Search Episode ⁉️</b>
<code>Jai kanhaiya Lal ki S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    KASHIBAI = """<b>Kashibai</b> ✨
    
<b>Total Episode :</b> <code>201</code>

<b>About</b> : Kashibai is raised as a spoiled child. She faces challenges as an adult when her husband Peshwa works to expand the Maratha empire and she must prove her capabilities to become an administrator.

<b>How To Search Episode ⁉️</b>
<code>Kashibai S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    THE_LEGEND_OF_HANUMAN = """<b>The Legend of Hanuman</b> ✨
    
<b>Total Episode :</b> <code>32</code>

<b>About</b> : Lord Mahadev is reborn as Hanuman to serve Lord Rama, and becomes a beacon of hope amidst the harrowing darkness.

<b>How To Search Episode ⁉️</b>
<code>The Legend of Hanuman S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    BRIJ_KE_GOPAL = """<b>Brij Ke Gopal</b> ✨
    
<b>Total Episode :</b> <code>48</code>

<b>About</b> : Lord Krishna incarnates as a human on Earth to end the agony of his devotees and battle against evil, restoring the faith of people in good.

<b>How To Search Episode ⁉️</b>
<code>Brij ke Gopal S1 Episode 1</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    GARUD = """<b>Dharm Yoddha Garud</b> ✨
    
<b>Total Episode :</b> <code>234</code>

<b>About</b> : Garud, a mighty warrior, strives to maintain peace and fights injustice. He faces off powerful adversaries while protecting and helping those in need.

<b>How To Search Episode ⁉️</b>
<code>Garud S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    PARSHURAM = """<b>Parshuram</b> ✨
    
<b>Total Episode :</b> <code>160</code>

<b>About</b> : Parashurama, the sixth incarnation of the God Vishnu, comes to Earth with the sole purpose of fighting off all evil and protecting humans.

<b>How To Search Episode ⁉️</b>
<code>Parshuram S01 E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    K_SHANIDEV = """<b>Karmadhikari Shanidev</b> ✨
    
<b>Total Episode :</b> <code>39</code>

<b>About</b> : Karmadhikari Shanidev is an Indian Mythology television series produced by Triangle Film Company and premiered on 11 December 2023 on Shemaroo TV.

<b>How To Search Episode ⁉️</b>
<code>Karmadhikari Shanidev S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    SHIV_SHAKTI = """<b>Shiv Shakti</b> ✨
    
<b>Total Episode :</b> <code>Running...</code>

<b>About</b> : Lord Shiva and his wife, Goddess Parvati, navigate their relationship and duties and offer sacrifices and brave separation to selflessly care for humanity.

<b>How To Search Episode ⁉️</b>
<code>Shiv Shakti S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    SHRIMAD_RAMAYAN = """<b>Shrimad Ramayan</b> ✨
    
<b>Total Episode :</b> <code>Running...</code>

<b>About</b> : A religious leader reads out the Ramayana and explains it to a large gathering of devotees in a brief, simple and easy-to-understand manner.

<b>How To Search Episode ⁉️</b>
<code>Shrimad Ramayan S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    P_ASHOK = """<b>Prachand Ashok</b> ✨
    
<b>Total Episode :</b> <code>Running...</code>

<b>About</b> : Prachand Ashoka is an upcoming historical soap opera produced by Balaji Telefilms. It stars Adnan Khan, Simba Nagpal, Tanusri Dasgupta and Mallika Singh. The serial story is based on the story of Emperor Ashoka. The show will be aired on Colors TV in January 2024.

<b>How To Search Episode ⁉️</b>
<code>Pracchand Ashok S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    C_HANUMAN = """<b>Chiranjeevi Hanuman</b> ✨
    
<b>Total Episode :</b> <code>Coming Soon...</code>

<b>About</b> : Coming Soon

<b>How To Search Episode ⁉️</b>
<code>Not Released Yet !!</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    SETTINGS_TXT = """Settings"""
    CHANNEL_TXT = """Channels"""
    RENAME_TXT = """Rename Help"""
    LOGO = """
 ____  ___    ____   __  ____  ____ 
(_  _)/ __)  (  _ \ /  \(_  _)(__  )
  )( ( (_ \   ) _ ((  O ) )(   / _/ 
 (__) \___/  (____/ \__/ (__) (____)"""
