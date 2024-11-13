# call_payment.py
from pyrogram import *
from pyrogram.enums import *
from pyrogram.helpers import ikb
from pyrogram.types import *
from Mix import *

from modular.payment import payment_message  # Pastikan ini sesuai dengan lokasi file

@ky.callback("payme.")
async def _(c, cq):
    cmd = cq.data.split(".")[1]
    kb = ikb([[("Kembali", "bace.payme")]])
    if cmd == "butformat":
        await cq.edit_message_text(text=payment_message, reply_markup=kb, parse_mode=ParseMode.HTML)

@ky.callback("bace")
async def _(c, cq):
    txt = cgr("payme_1")
    ke = ikb([[("Payment", "payme.butformat")]])
    await cq.edit_message_text(text=txt, reply_markup=ke)
