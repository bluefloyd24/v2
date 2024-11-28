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
    
    args = m.text.split(maxsplit=2) 
    
    if len(args) < 2:
        return await m.reply(cgr("prem_2").format(em.gagal))
    
    try:
        duration = int(args[1])
    except ValueError:
        return await m.reply(cgr("prem_3").format(em.gagal))
    
    if not m.reply_to_message:
        return await m.reply("❌ Harap balas pesan pengguna yang ingin diberi premium.")
   
    target_user = m.reply_to_message.from_user
    target_id = target_user.id
    target_mention = f"<a href='tg://user?id={target_id}'>{target_user.first_name}</a>"
    
    udB.set_premium(target_id, duration)
    
    await m.reply(cgr("prem_4").format(target_mention, duration))
