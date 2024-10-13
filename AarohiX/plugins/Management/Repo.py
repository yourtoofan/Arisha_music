from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AarohiX import app as bot
import requests
from config import BOT_USERNAME
from AarohiX.utils.errors import capture_err

start_txt = """**
➤ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴡᴏʀʟᴅ ᥫᩣ
 
 ⦿ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ɴ ᴠᴘs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ !
 
 ⦿ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ !
 
 ⦿ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ !
 
 ⦿ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴅᴍ ᴍᴇ !
**"""

@bot.on_message(filters.command(["repo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("⦿ ᴀᴅᴅ ᴍᴇ ⦿", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/doreamon_support_chat"),
          InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/legend_mickey"),
        ],
        [
          InlineKeyboardButton("ᴍᴜsɪᴄ ʙᴏᴛ 𝟷", url=f"https://t.me/XDz_MUSIC_BOT?startgroup=true"),
          InlineKeyboardButton("︎ᴍᴜsɪᴄ ʙᴏᴛ 𝟸", url=f"https://t.me/zoyumusicbot?startgroup=true"),
        ],
        [
          InlineKeyboardButton("ᴅᴘ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/DPS_WORLD_XD"),
          InlineKeyboardButton("ɢʀᴏᴜᴘ ʟɪɴᴋ", url=f"https://t.me/LINK_KA_GROUP"),
        ],
        [
          InlineKeyboardButton("sᴜɪᴘᴘʀᴛ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/the_incricible"),
          InlineKeyboardButton("ᴏᴡɴᴇʀ", url=f"https://t.me/legend_mickey"),
        ],
        [
          InlineKeyboardButton("ᴀʙᴏᴜᴛ ᴍɪᴄᴋᴇʏ", url="https://t.me/about_godfather"),
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url=f"https://t.me/doreamon_support_chat"),
        ],
        [
          InlineKeyboardButton("ᴍᴜsɪᴄ ʙᴏᴛ 𝟹", url=f"https://t.me/Arisha_musicbot?startgroup=true"),
          InlineKeyboardButton("ᴍᴜsɪᴄ ʙᴏᴛ 𝟺", url=f"https://t.me/XDz_MUSIC_BOT?startgroup=true"),
        ] 
     
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/nRb.jpg",
        caption=start_txt,
        reply_markup=reply_markup,
    )



#-------------------------------------------------------#


@bot.on_message(filters.command("repo", prefixes="@"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/yourtoofan/arisha_music/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[ʀᴇᴘᴏ](https://github.com/soja) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/doreamon_support_chat)
| ᴄᴏɴᴛʀɪʙᴜᴛᴏʀs |
----------------
{list_of_users}"""
        await bot.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await bot.send_message(message.chat.id, text="Failed to fetch contributors.")

