################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from pyrogram import *
from pyrogram.enums import *
from pyrogram.helpers import ikb
from pyrogram.types import *

from Mix import *


@ky.callback("markd.")
async def _(c, cq):
    cmd = cq.data.split(".")[1]
    kb = ikb([[("Kembali", "bace.markd")]])
    if cmd == "butformat":
        nan = cgr("mark_1")
        await cq.edit_message_text(text=nan, reply_markup=kb, parse_mode=ParseMode.HTML)
    elif cmd == "filing":
        nen = cgr("mark_2")
        await cq.edit_message_text(
            text=nen,
            reply_markup=kb,
            parse_mode=ParseMode.HTML,
        )


@ky.callback("bace")
async def _(c, cq):
    txt = cgr("mark_3")
    ke = ikb([[("Markdown Format", "markd.butformat"), ("Fillings", "markd.filing")]])
    await cq.edit_message_text(text=txt, reply_markup=ke)
