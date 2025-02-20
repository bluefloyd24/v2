# call_payment.py
from pyrogram import *
from pyrogram.enums import *
from pyrogram.helpers import ikb
from pyrogram.types import *
from Mix import *

@ky.callback("payme.")
async def _(c, cq):
    em = Emojik()
    em.initialize()
    cmd = cq.data.split(".")[1]
    kb = ikb([[("Kembali", "bek.payme")]])

    if cmd == "butformat":
        puki = cgr("payme_3").format(em.payment)
        await cq.edit_message_text(puki, reply_markup=kb)


@ky.callback("bek")
async def _(c, cq):
    em = Emojik()
    em.initialize()
    txt = cgr("payme_1").format(em.payment)
    ke = ikb([[("Payment", "payme.butformat")]])
    await cq.edit_message_text(text=txt, reply_markup=ke)
