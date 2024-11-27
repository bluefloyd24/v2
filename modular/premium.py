from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Handler untuk perintah .premium
@ky.ubot("premium|prem", human.dev)
async def premium(c, m):
    if m.from_user.id != nlx.me.id:  # Pastikan hanya developer yang bisa menggunakannya
        return await m.reply("Anda tidak memiliki akses untuk perintah ini.")

    args = m.text.split()
    if len(args) != 2:
        return await m.reply("Format salah! Gunakan: `.premium <durasi> day`")

    try:
        duration = int(args[1])
    except ValueError:
        return await m.reply("Durasi harus berupa angka.")

    # Mengatur status premium di database
    udB.set_premium(m.from_user.id, duration)

    await m.reply(f"Berhasil menambahkan {m.from_user.first_name} ke premium selama {duration} hari.")
