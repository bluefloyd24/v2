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
    udB.add_served_user(m.from_user.id)
    user_name = f"<a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name} {m.from_user.last_name or ''}</a>"
    user2 = f"<a href='tg://user?id={nlx.me.id}'>{nlx.me.first_name} {nlx.me.last_name or ''}</a>"
    ts_2 = cgr("asst_2").format(user_name, user2)
        button = ikb(
            [
                [(cgr("asst_9"), "clbk.buat"), (cgr("asst_6"), "clbk.rebot")],
                [(cgr("asst_8"), "clbk.fitur"), (cgr("asst_7"), "clbk.status"), (cgr("asst_3"), "clbk.bhsa")],
                [(cgr("asst_10"), "clbk.blue")],
            ]
        )
        return await m.reply(ts_1, reply_markup=button)
    else:
        tt = ikb([[(cgr("ttup"), "close_asst")]])
        return await m.reply(ts_2, reply_markup=tt)
