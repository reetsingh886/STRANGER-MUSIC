# -----------------------------------------------
# 🔸 StrangerMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# 📅 Copyright © 2022 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzShukla
# -----------------------------------------------
 from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from SHUKLAMUSIC import app

REPO_VIDEO = "https://files.catbox.moe/aoafwn.mp4"

# ❌ OLD REPO HANDLER KO BLOCK KAR DIYA
@app.on_message(filters.command(["repo", "source"]), group=-10)
async def stop_old_repo(_, message):
    return


# ✅ SIRF YE WALA CHALEGA
@app.on_message(filters.command(["repo", "source"]), group=0)
async def send_repo(_, message: Message):
    await message.reply_video(
        video=REPO_VIDEO,
        caption=(
            "<b>✨ ʜᴇʏ ᴅᴇᴀʀ, ʜᴇʀᴇ ɪꜱ ꜱᴛʀᴀɴɢᴇʀ ᴍᴜꜱɪᴄ ʀᴇᴘᴏ ✨</b>\n\n"
            "🚀 <b>ᴏɴᴇ ᴄʟɪᴄᴋ ᴅᴇᴘʟᴏʏ • ʟᴀɢ-ꜰʀᴇᴇ • 24x7 ʀᴜɴ</b>\n\n"
            "⭐ <b>ᴅᴏɴ’ᴛ ꜰᴏʀɢᴇᴛ ᴛᴏ ꜱᴛᴀʀ ᴛʜᴇ ʀᴇᴘᴏ</b>"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎵 ᴍᴜꜱɪᴄ ʙᴏᴛ 🎧",
                        url="https://github.com/NoxxOP/ShrutixMusic"
                    )
                ]
            ]
        ),
        supports_streaming=True,
        has_spoiler=True,
    )
