from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):

    await message.reply_text(
        f"""[★](https://telegra.ph/file/8659dbdff98d2f4512b1f.jpg)I am **{bn}** A telegram voice chat bot for playing songs in your group voice chat
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SOURCE CODE👻", url="https://t.me/Miss_meenuus_bot"
                    ),
                    InlineKeyboardButton(
                        "DEV❤", url="https://t.me/danger_of_telegram"
                    )
                ]
            ]
        )
    )
