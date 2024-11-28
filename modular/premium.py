from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from thegokil import DEVS
from Mix import *

@ky.ubot("premium|prem")
async def premium(c, m):
    em = Emojik()
    em.initialize()
    if m.from_user.id not in DEVS:
        return await m.reply(cgr("prem_1").format(em.gagal))

    args = m.text.split()
    if len(args) != 2:
        return await m.reply(cgr("prem_2").format(em.gagal))

    try:
        duration = int(args[1])
    except ValueError:
        return await m.reply(cgr("prem_3").format(em.gagal))

    udB.set_premium(m.from_user.id, duration)

    await m.reply(cgr("prem_4").format(m.from_user.first_name, duration))
