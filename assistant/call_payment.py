from pyrogram import *
from pyrogram.enums import *
from pyrogram.helpers import ikb
from pyrogram.types import *

from Mix import *


@ky.callback("payme.")
async def _(c, cq):
    cmd = cq.data.split(".")[1]
    kb = ikb([[("Kembali", "bace.markd")]])
    if cmd == "butformat":
        nan = cgr("mark_1")
        await cq.edit_message_text(text=nan, reply_markup=kb, parse_mode=ParseMode.HTML)


@ky.callback("bace")
async def _(c, cq):
    txt = cgr("mark_3")
    ke = ikb([[("Payment", "payme.butformat")]])
    await cq.edit_message_text(text=txt, reply_markup=ke)
