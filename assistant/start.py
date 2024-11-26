################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.file_id import *
from pyrogram.helpers import ikb
from pyrogram.raw.functions.messages import *
from pyrogram.raw.functions.stickers import *
from pyrogram.raw.types import *
from pyrogram.types import *

from Mix import *


@ky.bots("start", human.pv)
async def _(c, m):
    # Log pengguna yang menggunakan bot
    udB.add_served_user(m.from_user.id)

    # Format nama pengguna dan pesan
    user_name = f"<a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name} {m.from_user.last_name or ''}</a>"
    user2 = f"<a href='tg://user?id={nlx.me.id}'>{nlx.me.first_name} {nlx.me.last_name or ''}</a>"
    ts_2 = cgr("asst_2").format(user_name, user2)

    # Membuat InlineKeyboardMarkup
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(cgr("asst_9"), callback_data="clbk.buat"),
                InlineKeyboardButton(cgr("asst_6"), callback_data="clbk.rebot"),
            ],
            [
                InlineKeyboardButton(cgr("asst_8"), callback_data="clbk.fitur"),
                InlineKeyboardButton(cgr("asst_7"), callback_data="clbk.status"),
                InlineKeyboardButton(cgr("asst_3"), callback_data="clbk.bhsa"),
            ],
            [
                InlineKeyboardButton(cgr("asst_10"), callback_data="clbk.blue"),
            ],
        ]
    )

    # Kirim pesan dengan InlineKeyboardMarkup
    return await m.reply(ts_2, reply_markup=buttons)
