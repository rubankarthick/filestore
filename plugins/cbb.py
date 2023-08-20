#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about": 
        await query.message.edit_text(
            text = f"<b> Bot Creator :</b> <a href='https://ruban96.online'> Ruban </a>",
            disable_web_page_preview = False,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("🎬 MAIN CHANNEL 🎬", url="https://t.me/+6pdw2jn048w1Zjg1"),
                        InlineKeyboardButton("🔒 CLOSE", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "morefromus": 
        await query.message.edit_text(
            text = f"<b>JOIN MORE CHANNEL TO DOWNLOAD MOVIE FAST❕</b>",
            disable_web_page_preview = False,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("📽️NEW TAMIL MOVIES🎬", url=f"https://t.me/+GiydT_oyMZE0MjZl")
                    ],
                    [
                        InlineKeyboardButton("📽️HOLLYWOOD DUBBED MOVIES🎬", url=f"https://t.me/+r7uCG7sSC-VmMGE9")
                    ],
                    [
                        InlineKeyboardButton("📽️MULTI LANGUAGE MOVIES🎬", url=f"https://t.me/+8pc1V0Mk8mM0Y2I1")
                    ],
                    [
                        InlineKeyboardButton("📽️ALL NEW SERIES🎬", url=f"https://t.me/+Md4DpWxJ7NlmOTI9")
                    ],
                    [
                        InlineKeyboardButton("🔉 DISCUSSION 🔉", url="https://t.me/+rucqp8Ao-soyMDU1"),
                        InlineKeyboardButton("🔒 CLOSE", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
