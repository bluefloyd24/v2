from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from thegokil import DEVS
from Mix import *

@ky.ubot("premium|prem")
async def premium(c, m):
    em = Emojik()
    em.initialize()
    
    # Periksa apakah pengguna adalah developer
    if m.from_user.id not in DEVS:
        return await m.reply(cgr("prem_1").format(em.gagal))
    
    # Pisahkan teks dan validasi argumen
    args = m.text.split(maxsplit=2)  # Ambil hingga maksimal 3 bagian
    
    if len(args) < 2:
        return await m.reply(cgr("prem_2").format(em.gagal))
    
    try:
        # Ambil hanya angka durasi
        duration = int(args[1])
    except ValueError:
        return await m.reply(cgr("prem_3").format(em.gagal))
    
    # Set premium untuk pengguna
    udB.set_premium(m.reply_to_message.from_user.id, duration)

    await m.reply(cgr("prem_4").format(m.from_user.first_name, duration))

