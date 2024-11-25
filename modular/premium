from pyrogram import *
from pyrogram.errors import *
from pyrogram.enums import *
from pyrogram.types import *
from Mix import *


@ky.ubot("premium")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if m.from_user.id == nlx.me.id:  # Pastikan hanya admin yang bisa mengatur premium
        try:
            duration = int(m.text.split()[1])  # Ambil durasi premium
            db.set_premium(m.from_user.id, duration)
            await m.reply(f"Premium telah diaktifkan untuk {m.from_user.first_name} selama {duration} hari!", .format(em.sukses))
        except Exception as e:
            await m.reply(f"Terjadi kesalahan: {e}")
    else:
        await m.reply("Anda tidak memiliki izin untuk menggunakan perintah ini.")
