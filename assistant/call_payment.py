# call_payment.py
from pyrogram import *
from pyrogram.enums import *
from pyrogram.helpers import ikb
from pyrogram.types import *
from Mix import *

@ky.callback("payme.")
async def _(c, cq):
    cmd = cq.data.split(".")[1]
    kb = ikb([[("Kembali", "bek.payme")]])
    if cmd == "butformat":
        payment_message = udB.get_var(c.me.id, "payment_message", default="Silakan melakukan pembayaran.")
        await cq.edit_message_text(text=payment_message, reply_markup=kb, parse_mode=ParseMode.HTML)


@ky.callback("bek")
async def _(c, cq):
    txt = cgr("payme_1")
    ke = ikb([[("Payment", "payme.butformat")]])
    await cq.edit_message_text(text=txt, reply_markup=ke)
